#!/usr/bin/env python3
"""Add the UTC time after each clock time in a calendar event, so readers anywhere know when it is.

Purpose (2026-11-18): calendar rows give times as their sources do ("2:30 pm CT", "10 am",
"9:00 am"), and readers in other time zones, and video sites that show a scheduled stream in the
viewer's own zone, made "when is it?" a recurring question (Texas's seed livestream showed "1:30 PM"
to a reader in Mountain time for a 2:30 pm Central event). build_site.py calls add_utc() on each
row's event text, so every time with a known zone gets "(20:30 UTC)" after it.

The zone is the one written after the time (ET, CT, MT, PT, AKT, HT, or Eastern, Central, ...),
else the state's zone, so that US readers get a local time and readers elsewhere UTC (Neal,
2026-11-18: "both UTC and a US-based timezone for the given state (pick one)"). A time with no zone
written gets the state's zone named after it ("9:00 am" becomes "9:00 am PT (17:00 UTC)"). For a
state that spans zones, the zone of most of its people is used: Central for Texas, Kansas,
Nebraska, the Dakotas and Tennessee, Eastern for Florida, Indiana, Kentucky and Michigan, Mountain
for Idaho, Pacific for Oregon. The date
is a "Mon DD" written next to the time ("Tue Nov 24, 2 pm", "5 pm Mon Nov 16"), else the first in the
row's date cell (2026, or 2027 for January); daylight saving is applied for that date. When the UTC
time falls on another day, its date is given too ("00:00 UTC Nov 17"). Times already followed by a
UTC time are left as they are.

    python3 -I scripts/eventtime.py "Wed Nov 18" TX "seed generated, 2:30 pm CT, livestreamed"
"""
import datetime
import re
import sys
from zoneinfo import ZoneInfo

ZONES = {"ET": "America/New_York", "EASTERN": "America/New_York", "CT": "America/Chicago",
         "CENTRAL": "America/Chicago", "MT": "America/Denver", "MOUNTAIN": "America/Denver",
         "PT": "America/Los_Angeles", "PACIFIC": "America/Los_Angeles", "AKT": "America/Anchorage",
         "HT": "Pacific/Honolulu"}

# States (and DC) that keep a single zone; Arizona has no daylight saving.
STATE_ZONE = {
    **dict.fromkeys("CT DE DC GA ME MD MA NH NJ NY NC OH PA RI SC VT VA WV".split(), "America/New_York"),
    **dict.fromkeys("AL AR IL IA LA MN MS MO OK WI".split(), "America/Chicago"),
    **dict.fromkeys("CO MT NM UT WY".split(), "America/Denver"),
    "AZ": "America/Phoenix", "CA": "America/Los_Angeles", "NV": "America/Los_Angeles",
    "WA": "America/Los_Angeles", "HI": "Pacific/Honolulu",
    # states that span zones: the zone of most of their people
    **dict.fromkeys("TX KS NE ND SD TN".split(), "America/Chicago"),
    **dict.fromkeys("FL IN KY MI".split(), "America/New_York"),
    "ID": "America/Denver", "OR": "America/Los_Angeles", "AK": "America/Anchorage",
}
ABBREV = {"America/New_York": "ET", "America/Chicago": "CT", "America/Denver": "MT",
          "America/Phoenix": "MST", "America/Los_Angeles": "PT", "America/Anchorage": "AKT",
          "Pacific/Honolulu": "HT"}
MONTHS = {m: i for i, m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(), 1)}

TIME = re.compile(
    r"\b(?P<h>1[0-2]|0?[1-9])(?::(?P<m>[0-5]\d))?\s*(?P<ap>[ap])\.?m\.?"
    r"(?P<zone>\s+(?:ET|CT|MT|PT|AKT|HT|Eastern|Central|Mountain|Pacific)\b)?"
    r"(?!\s*\(\d{1,2}:\d{2} UTC)", re.I)


def row_date(date_cell):
    m = re.search(r"\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+(\d{1,2})\b", date_cell)
    if not m:
        return None
    month = MONTHS[m.group(1)]
    return datetime.date(2027 if month == 1 else 2026, month, int(m.group(2)))


DATE_NEAR = r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+\d{1,2}\b"


def near_date(event, m):
    """A date written just before the time (in the same clause) or just after it."""
    before = re.split(r"[;(]", event[max(0, m.start() - 30):m.start()])[-1]
    after = event[m.end():m.end() + 16]
    found = re.findall(DATE_NEAR, before) or re.findall(rf"^[\s,]*(?:[A-Z][a-z]{{2}}\s+)?({DATE_NEAR})", after)
    return row_date(found[-1] if found else "") if found else None


def add_utc(event, date_cell, state):
    """The event text with " (HH:MM UTC)" after each time whose zone and date are known."""
    row_day = row_date(date_cell)
    if row_day is None:
        return event

    def one(m):
        day = near_date(event, m) or row_day
        zone = m.group("zone")
        tz = ZONES.get(zone.strip().upper()) if zone else STATE_ZONE.get(state.strip())
        if not tz:
            return m.group(0)
        h = int(m.group("h")) % 12 + (12 if m.group("ap").lower() == "p" else 0)
        local = datetime.datetime.combine(day, datetime.time(h, int(m.group("m") or 0)), ZoneInfo(tz))
        utc = local.astimezone(datetime.timezone.utc)
        other = f" {utc:%b} {utc.day}" if utc.date() != day else ""
        named = "" if zone else f" {ABBREV[tz]}"
        return f"{m.group(0)}{named} ({utc:%H:%M} UTC{other})"

    return TIME.sub(one, event)


if __name__ == "__main__":
    print(add_utc(sys.argv[3], sys.argv[1], sys.argv[2]))
