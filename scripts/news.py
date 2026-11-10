#!/usr/bin/env python3
"""Keep a log of news about 2026 post-election audits, for the site's news page.

Purpose (2026-11-10): Neal's Google Alerts ("risk-limiting audits", "Verified voting") and our own
periodic web searches turn up news about state audits: kickoffs, dates, discrepancies, results.
This keeps one de-duplicated log, news/news.jsonl (one JSON object per article: date, title,
source, snippet, url, via, states), which scripts/build_site.py renders as news.md.

Commands:
    # parse a Google Alert email saved as plain text (raw alert files stay out of the repo:
    # they carry personal unsubscribe links)
    python3 -I scripts/news.py add-alert ALERT.txt --date 2026-11-10 --alert "risk-limiting audits"
    # add an article found by a web search
    python3 -I scripts/news.py add --url URL --title TITLE --source SOURCE --date 2026-11-10 \
        [--snippet TEXT] [--via "web search: QUERY"] [--states GA,PA]

States are tagged automatically from state names in the title and snippet; --states adds more.
"""
import argparse
import json
import pathlib
import re
import urllib.parse

LOG = pathlib.Path("news/news.jsonl")
STATE_NAMES = {
    "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR", "California": "CA",
    "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE", "District of Columbia": "DC",
    "Florida": "FL", "Georgia": "GA", "Hawaii": "HI", "Idaho": "ID", "Illinois": "IL",
    "Indiana": "IN", "Iowa": "IA", "Kansas": "KS", "Kentucky": "KY", "Louisiana": "LA",
    "Maine": "ME", "Maryland": "MD", "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN",
    "Mississippi": "MS", "Missouri": "MO", "Montana": "MT", "Nebraska": "NE", "Nevada": "NV",
    "New Hampshire": "NH", "New Jersey": "NJ", "New Mexico": "NM", "New York": "NY",
    "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH", "Oklahoma": "OK", "Oregon": "OR",
    "Pennsylvania": "PA", "Rhode Island": "RI", "South Carolina": "SC", "South Dakota": "SD",
    "Tennessee": "TN", "Texas": "TX", "Utah": "UT", "Vermont": "VT", "Virginia": "VA",
    "Washington": "WA", "West Virginia": "WV", "Wisconsin": "WI", "Wyoming": "WY",
}


def tag_states(text):
    found = []
    for name, code in STATE_NAMES.items():
        if re.search(rf"\b{re.escape(name)}\b", text):
            if name == "Virginia" and re.search(r"\bWest Virginia\b", text) and not re.search(r"(?<!West )\bVirginia\b", text):
                continue
            if name == "Kansas" and re.search(r"\bArkansas\b", text) and not re.search(r"(?<!Ar)\bKansas\b", text):
                continue
            found.append(code)
    return sorted(set(found))


def real_url(u):
    q = urllib.parse.urlparse(u)
    if q.netloc.endswith("google.com") and q.path == "/url":
        return urllib.parse.parse_qs(q.query).get("url", [u])[0]
    return u


def load():
    rows = [json.loads(l) for l in LOG.read_text().splitlines()] if LOG.exists() else []
    return rows, {r["url"] for r in rows}


def append(entries):
    rows, seen = load()
    LOG.parent.mkdir(parents=True, exist_ok=True)
    n = 0
    with LOG.open("a") as f:
        for e in entries:
            if e["url"] in seen:
                continue
            seen.add(e["url"])
            f.write(json.dumps(e) + "\n")
            n += 1
            print(f"+ {e['date']} [{','.join(e['states'])}] {e['title'][:90]}")
    print(f"{n} new, {len(entries) - n} already logged")


def parse_alert(text, date, alert):
    body = text.split("- - - - -")[0]
    out = []
    for chunk in re.split(r"\n\s*\n", body):
        m = re.search(r"<(https?://[^>]+)>", chunk)
        if not m or "google.com/alerts" in m.group(1):
            continue
        lines = [l.strip() for l in chunk[:m.start()].strip().splitlines() if l.strip() and not l.startswith("===")]
        if len(lines) < 2:
            continue
        title, source, snippet = lines[0], lines[1], " ".join(lines[2:])
        out.append({"date": date, "title": title, "source": source, "snippet": snippet,
                    "url": real_url(m.group(1)), "via": f"Google Alert: {alert}",
                    "states": tag_states(title + " " + snippet)})
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add-alert")
    a.add_argument("file")
    a.add_argument("--date", required=True)
    a.add_argument("--alert", required=True)
    b = sub.add_parser("add")
    for k in ("url", "title", "source", "date"):
        b.add_argument("--" + k, required=True)
    b.add_argument("--snippet", default="")
    b.add_argument("--via", default="web search")
    b.add_argument("--states", default="")
    args = ap.parse_args()
    if args.cmd == "add-alert":
        append(parse_alert(pathlib.Path(args.file).read_text(), args.date, args.alert))
    else:
        st = tag_states(args.title + " " + args.snippet)
        st = sorted(set(st) | {s.strip() for s in args.states.split(",") if s.strip()})
        append([{"date": args.date, "title": args.title, "source": args.source, "snippet": args.snippet,
                 "url": args.url, "via": args.via, "states": st}])


if __name__ == "__main__":
    main()
