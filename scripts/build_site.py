#!/usr/bin/env python3
"""Build the audit-results GitHub Pages site from its sources.

Purpose (2026-11-10): the site tracks post-election audits of the November 3, 2026 US general
election. Three pages are generated so they never drift from their data:

- calendar.md, from calendar-source.md (the hand-maintained master calendar), with front matter
- states/<XX>.md, one page per state: any hand-written notes from state-notes/<XX>.md, its
  calendar rows, and its watched pages and their captures
- news.md, from news/news.jsonl (see scripts/news.py)
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


def calendar_md(src):
    """Render calendar-source.md for the site, readable on phones.

    The "Watch now" table becomes a list grouped by date (what a phone visitor most needs); the
    other, longer tables stay tables, wrapped in a box that scrolls sideways on narrow screens
    instead of squeezing every column (see .table-scroll in _includes/header.html).
    """
    out, block, section = [], [], ""

    def flush():
        if not block:
            return
        rows = [[c.strip() for c in l.strip().strip("|").split("|")] for l in block]
        body = [r for r in rows[2:]]
        if section.startswith("Watch now"):
            last = None
            for c in body:
                if c[0] != last:
                    out.append(f"\n### {c[0]}\n" if last is not None else f"### {c[0]}\n")
                    last = c[0]
                ev = linkify(c[2]).rstrip()
                ev += "" if ev.endswith((".", "?", "!")) else "."
                basis = f" · _{c[3]}_." if len(c) > 3 and c[3] else ""
                more = f" {linkify(c[4])}" if len(c) > 4 and c[4] else ""
                out.append(f"- **{c[1]}**: {ev}{basis}{more}")
            out.append("")
        else:
            out.append('<div class="table-scroll" markdown="1">\n')
            out.extend(block[:2])
            # bare URLs (the Source column) become short links named for their site, so a long
            # URL doesn't force the table wider than the page
            out.extend(re.sub(r"(?<![(<])\bhttps?://([^/\s|]+)[^\s|]*",
                              lambda m: f"[{m.group(1).removeprefix('www.')}]({m.group(0)})", l)
                       for l in block[2:])
            out.append("\n</div>\n")
        block.clear()

    for line in src.splitlines():
        if line.startswith("|"):
            block.append(line)
            continue
        flush()
        if line.startswith("## "):
            section = line[3:].strip()
        out.append(line)
    flush()
    return "\n".join(out) + "\n"


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


def linkify(text):
    """Turn bare URLs into kramdown autolinks, leaving markdown links and existing <...> alone."""
    return re.sub(r"(?<![(<])\bhttps?://[^\s)|>]+[^\s)|>.,;:]", lambda m: f"<{m.group(0)}>", text)


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
        # A list, not a table: a 4-column table is unreadable on a phone.
        last = None
        for s, c in mine:
            if s != last:
                out.append(f"### {s}\n" if last is None else f"\n### {s}\n")
                last = s
            basis = f" · _{c[3]}_." if len(c) > 3 and c[3] else ""
            more = f" {linkify(c[4])}" if len(c) > 4 and c[4] else ""
            ev = linkify(c[2]).rstrip()
            ev += "" if ev.endswith((".", "?", "!")) else "."
            out.append(f"- **{c[0]}**: {ev}{basis}{more}")
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
            out.append(f"- <{w['url']}> ({w['why']}; {note}; {n} saved {'copy' if n == 1 else 'copies'})")
        out.append("")
    else:
        out.append("None yet. Suggestions welcome.\n")
    return "\n".join(out) + "\n"


def news_md():
    log = ROOT / "news" / "news.jsonl"
    rows = [json.loads(l) for l in log.read_text().splitlines()] if log.exists() else []
    out = [front("News"), "# News about the 2026 audits\n",
           "Articles and official posts about post-election audits of the November 3, 2026 general "
           "election, newest first, from Google Alerts and our own searches. State tags link to the "
           "state pages.\n"]
    for date in sorted({r["date"] for r in rows}, reverse=True):
        out.append(f"## {date}\n")
        for r in [r for r in rows if r["date"] == date]:
            tags = " ".join(f"[{c}](states/{c}.md)" for c in r["states"])
            snip = f" {r['snippet']}" if r.get("snippet") else ""
            line = f"- **[{r['title']}]({r['url']})**, {r['source']}.{snip} {tags}".rstrip()
            out.append(line.replace("|", "\\|"))  # a bare | makes kramdown read the line as a table
        out.append("")
    return "\n".join(out) + "\n"


def main():
    src = (ROOT / "calendar-source.md").read_text()
    (ROOT / "calendar.md").write_text(front("Calendar") + calendar_md(src))
    rows = list(calendar_rows(src))
    watch = json.loads((ROOT / "watchlist.json").read_text())
    by = load_log()
    (ROOT / "captures.md").write_text(captures_md(watch, by))
    (ROOT / "news.md").write_text(news_md())
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
