#!/usr/bin/env python3
"""Keep a private log of news about 2026 post-election audits, and publish the items Neal chooses.

Purpose (2026-11-10, revised 2026-11-14): Neal's Google Alerts ("risk-limiting audits", "Verified
voting") and our own periodic web searches turn up news about state audits. Every item found goes
into the private, gitignored log extra-news-log/news.jsonl. The site prefers official sources;
Neal triages the private log and publishes chosen items with `promote`, which copies them into
news/news.jsonl, the log scripts/build_site.py renders as news.md. Each line is one JSON object:
date, title, source, snippet, url, via, states.

Commands:
    # parse a Google Alert email saved as plain text (raw alert files stay out of the repo:
    # they carry personal unsubscribe links)
    python3 -I scripts/news.py add-alert ALERT.txt --date 2026-11-10 --alert "risk-limiting audits"
    # add an article found by a web search
    python3 -I scripts/news.py add --url URL --title TITLE --source SOURCE --date 2026-11-10 \
        [--snippet TEXT] [--via "web search: QUERY"] [--states GA,PA]
    # list private items not yet published; publish chosen ones by URL (or a unique substring)
    python3 -I scripts/news.py list [--state GA]
    python3 -I scripts/news.py promote URL [URL ...]

States are tagged automatically from state names in the title and snippet; --states adds more.
"""
import argparse
import json
import pathlib
import re
import urllib.parse

LOG = pathlib.Path("extra-news-log/news.jsonl")   # private: everything found
PUBLIC = pathlib.Path("news/news.jsonl")          # published: items Neal promotes
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


def load(log=None):
    log = log or LOG
    rows = [json.loads(l) for l in log.read_text().splitlines()] if log.exists() else []
    return rows, {r["url"] for r in rows}


def promote(keys):
    rows, _ = load()
    _, published = load(PUBLIC)
    with PUBLIC.open("a") as f:
        for k in keys:
            hits = [r for r in rows if r["url"] == k] or [r for r in rows if k in r["url"]]
            if len(hits) != 1:
                print(f"? {k}: {len(hits)} matches in the private log")
                continue
            r = hits[0]
            if r["url"] in published:
                print(f"= already published: {r['title'][:80]}")
                continue
            f.write(json.dumps(r) + "\n")
            published.add(r["url"])
            print(f"+ published: {r['date']} {r['title'][:80]}")


def unpublished(state=None):
    rows, _ = load()
    _, published = load(PUBLIC)
    for r in rows:
        if r["url"] not in published and (not state or state in r["states"]):
            print(f"{r['date']} [{','.join(r['states'])}] {r['source'][:28]:28} {r['title'][:70]}\n    {r['url']}")


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
    c = sub.add_parser("promote")
    c.add_argument("keys", nargs="+")
    d = sub.add_parser("list")
    d.add_argument("--state")
    args = ap.parse_args()
    if args.cmd == "promote":
        promote(args.keys)
    elif args.cmd == "list":
        unpublished(args.state)
    elif args.cmd == "add-alert":
        append(parse_alert(pathlib.Path(args.file).read_text(), args.date, args.alert))
    else:
        st = tag_states(args.title + " " + args.snippet)
        st = sorted(set(st) | {s.strip() for s in args.states.split(",") if s.strip()})
        append([{"date": args.date, "title": args.title, "source": args.source, "snippet": args.snippet,
                 "url": args.url, "via": args.via, "states": st}])


if __name__ == "__main__":
    main()
