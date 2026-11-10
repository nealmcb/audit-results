#!/usr/bin/env python3
"""Build the audit-results GitHub Pages site from its sources.

Purpose (2026-11-10): the site tracks post-election audits of the November 3, 2026 US general
election. Three pages are generated so they never drift from their data:

- calendar.md, from calendar-source.md (the hand-maintained master calendar), with front matter
- states/<XX>.md, one page per state: any hand-written notes from state-notes/<XX>.md, its
  calendar rows, and its watched pages and their captures
- captures.md, from watchlist.json and captures/log.jsonl: for every watched page, the first and
  latest fetch, each change with its UTC time and sha256, and whether it is blocked to scripts

Run from the repo root after editing calendar-source.md or after a capture round:
    python3 -I scripts/build_site.py
"""
import collections
import json
import pathlib
import re

ROOT = pathlib.Path(".")
STATES = {
    "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas", "CA": "California",
    "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware", "DC": "District of Columbia",
    "FL": "Florida", "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois",
    "IN": "Indiana", "IA": "Iowa", "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana",
    "ME": "Maine", "MD": "Maryland", "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota",
    "MS": "Mississippi", "MO": "Missouri", "MT": "Montana", "NE": "Nebraska", "NV": "Nevada",
    "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico", "NY": "New York",
    "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma", "OR": "Oregon",
    "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina", "SD": "South Dakota",
    "TN": "Tennessee", "TX": "Texas", "UT": "Utah", "VT": "Vermont", "VA": "Virginia",
    "WA": "Washington", "WV": "West Virginia", "WI": "Wisconsin", "WY": "Wyoming",
}


def front(title):
    return f"---\nlayout: default\ntitle: {title}\n---\n\n"


def calendar_rows(text):
    """Yield (section, cells) for every table row whose State cell names known states."""
    section = ""
    for line in text.splitlines():
        if line.startswith("## "):
            section = line[3:].strip()
        if not line.startswith("|") or set(line) <= set("|- "):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 3 and any(code in STATES for code in re.split(r"[ ,]+", cells[1])):
            yield section, cells


def load_log():
    log = ROOT / "captures" / "log.jsonl"
    rows = [json.loads(l) for l in log.read_text().splitlines()] if log.exists() else []
    by = collections.defaultdict(list)
    for r in rows:
        by[r["slug"]].append(r)
    return by


def captures_md(watch, by):
    out = [front("Captures"), "# Captures of state audit pages\n",
           "Each watched page is fetched every 30 minutes. A copy is kept whenever its content changes; "
           "the time is when we fetched it (UTC), and the sha256 identifies the exact bytes. "
           "Pages marked blocked refuse automated fetches and need a browser capture.\n"]
    for w in sorted(watch, key=lambda w: (w["state"], w["slug"])):
        rs = by.get(w["slug"], [])
        out.append(f"## {w['state']}: {w['slug']}\n\n{w['url']}\n\n{w['why']}\n")
        if not rs:
            out.append("Not fetched yet.\n")
            continue
        blocked = sum(1 for r in rs if r.get("blocked"))
        out.append(f"Fetched {len(rs)} times, {rs[0]['time']} to {rs[-1]['time']}"
                   + (f"; blocked {blocked} times" if blocked else "") + ".\n")
        changes = [r for r in rs if r.get("file")]
        if changes:
            out.append("| Changed at (UTC) | sha256 | Copy |\n|---|---|---|")
            for r in changes:
                out.append(f"| {r['time']} | `{r['sha256'][:16]}…` | [{pathlib.Path(r['file']).name}]({r['file']}) |")
            out.append("")
    return "\n".join(out) + "\n"


def state_md(code, rows, watch, by):
    name = STATES[code]
    out = [front(name), f"# {name}\n", "[← All states](index.md) · [Calendar](../calendar.md) · "
           "[Captures](../captures.md)\n"]
    note = ROOT / "state-notes" / f"{code}.md"
    if note.exists():
        out.append(note.read_text().strip() + "\n")
    out.append("## 2026 audit dates\n")
    mine = [(s, c) for s, c in rows if code in re.split(r"[ ,]+", c[1])]
    if mine:
        out.append("| Section | Date | Event | Basis |\n|---|---|---|---|")
        for s, c in mine:
            out.append(f"| {s} | {c[0]} | {c[2]} | {c[3] if len(c) > 3 else ''} |")
        out.append("")
    else:
        out.append("No 2026 dates found yet.\n")
    ws = [w for w in watch if w["state"] == code]
    out.append("## Watched pages\n")
    if ws:
        for w in ws:
            rs = by.get(w["slug"], [])
            last = rs[-1] if rs else None
            note = ("blocked to scripts" if last and last.get("blocked")
                    else f"last fetched {last['time']}" if last else "not fetched yet")
            n = sum(1 for r in rs if r.get("file"))
            out.append(f"- {w['url']} ({w['why']}; {note}; {n} saved {'copy' if n == 1 else 'copies'})")
        out.append("")
    else:
        out.append("None yet. Suggestions welcome.\n")
    return "\n".join(out) + "\n"


def main():
    src = (ROOT / "calendar-source.md").read_text()
    (ROOT / "calendar.md").write_text(front("2026 audit calendar") + src)
    rows = list(calendar_rows(src))
    watch = json.loads((ROOT / "watchlist.json").read_text())
    by = load_log()
    (ROOT / "captures.md").write_text(captures_md(watch, by))
    sd = ROOT / "states"
    sd.mkdir(exist_ok=True)
    idx = [front("States"), "# States\n", "| State | 2026 dates listed | Watched pages |", "|---|---|---|"]
    for code, name in sorted(STATES.items(), key=lambda kv: kv[1]):
        (sd / f"{code}.md").write_text(state_md(code, rows, watch, by))
        n = sum(1 for s, c in rows if code in re.split(r"[ ,]+", c[1]))
        nw = sum(1 for w in watch if w["state"] == code)
        idx.append(f"| [{name}]({code}.md) | {n} | {nw} |")
    (sd / "index.md").write_text("\n".join(idx) + "\n")
    print(f"built calendar.md, captures.md, states/ ({len(STATES)} pages) from {len(rows)} calendar rows")


if __name__ == "__main__":
    main()
