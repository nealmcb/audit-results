#!/usr/bin/env python3
"""Keep a log of news about 2026 post-election audits, and publish it on the site's news page.

Purpose (2026-11-10, revised 2026-11-16): Neal's Google Alerts ("risk-limiting audits", "Verified
voting") and our own periodic web searches turn up news about state audits. Every item found goes
into the private, gitignored log extra-news-log/news.jsonl, and is published by copying it into
news/news.jsonl, the log scripts/build_site.py renders as news.md and the state pages' "In the
news" lists. While PUBLISH_ALL is True every new item is published as it is added; once Neal is
sorting the items, set it to False and publish chosen ones with `promote`. Each line is one JSON
object: date, title, source, snippet, url, via, states.

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
    python3 -I scripts/news.py promote --all
    # set an item's states (in both logs), e.g. when no state name appears in its title or snippet
    python3 -I scripts/news.py tag URL PA[,NJ]
    # fetch each article not yet copied: save a private copy as evidence, and record our fetch time,
    # the copy's SHA-256 and the article's own published/modified times (both logs)
    python3 -I scripts/news.py times [--refetch]

Article copies (`times`, added 2026-11-17 at Neal's request: "save copies as evidence, but don't
republish them") go to extra-news-log/copies/, which is gitignored and never published. The public
log carries only the fetch time, published/modified times and the copy's SHA-256, so a commitment
(scripts/stamp.py) over news/news.jsonl fixes what each article said when we fetched it without
redistributing the article. Bot-challenge pages (capture.is_challenge) are never saved.

States are tagged automatically from state names in the title and snippet; --states adds more.
"""
import argparse
import datetime
import hashlib
import html
import json
import pathlib
import re
import sys
import urllib.parse

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

LOG = pathlib.Path("extra-news-log/news.jsonl")   # private: everything found
COPIES = pathlib.Path("extra-news-log/copies")    # private: saved copies of the articles
PUBLIC = pathlib.Path("news/news.jsonl")          # published: items Neal promotes
PUBLISH_ALL = True   # publish every item as it is added, until Neal is sorting them
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


def find(rows, k):
    """Rows matching k: its exact URL, else any URL containing it."""
    return [r for r in rows if r["url"] == k] or [r for r in rows if k in r["url"]]


def promote(keys=None):
    """Publish the private items named by keys (URLs or unique substrings), or all unpublished ones."""
    rows, _ = load()
    _, published = load(PUBLIC)
    if keys is None:
        keys = [r["url"] for r in rows if r["url"] not in published]
    with PUBLIC.open("a") as f:
        for k in keys:
            hits = find(rows, k)
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


def tag(key, states):
    """Set the states of the item matching key, in both logs."""
    states = sorted({s.strip().upper() for s in states.split(",") if s.strip()})
    for log in (LOG, PUBLIC):
        rows, _ = load(log)
        hits = find(rows, key)
        if len(hits) != 1:
            print(f"? {log}: {len(hits)} matches")
            continue
        hits[0]["states"] = states
        log.write_text("".join(json.dumps(r) + "\n" for r in rows))
        print(f"{log}: {hits[0]['title'][:70]} -> {','.join(states)}")


TIME_KEYS = {
    "published": ("article:published_time", "datepublished", "og:published_time", "pubdate",
                  "publishdate", "date", "dc.date", "dc.date.issued", "sailthru.date", "parsely-pub-date"),
    "modified": ("article:modified_time", "datemodified", "og:updated_time", "lastmod", "last-modified"),
}


def page_times(text):
    """The article's own published and modified times, from meta tags, JSON-LD or <time datetime>."""
    found = {}
    metas = {}
    for tag in re.findall(r"(?is)<meta\b[^>]*>", text):
        k = re.search(r'(?i)\b(?:property|name|itemprop)\s*=\s*["\']([^"\']+)', tag)
        v = re.search(r'(?i)\bcontent\s*=\s*["\']([^"\']+)', tag)
        if k and v:
            metas.setdefault(k.group(1).lower(), v.group(1).strip())
    for blob in re.findall(r'(?is)<script[^>]+application/ld\+json[^>]*>(.*?)</script>', text):
        for k, key in (("datepublished", "datePublished"), ("datemodified", "dateModified")):
            m = re.search(rf'"{key}"\s*:\s*"([^"]+)"', blob)
            if m:
                metas.setdefault(k, m.group(1))
    for which, keys in TIME_KEYS.items():
        for k in keys:
            if metas.get(k):
                found[which] = html.unescape(metas[k])
                break
    if "published" not in found:
        m = re.search(r'(?is)<time\b[^>]*\bdatetime\s*=\s*["\']([^"\']+)', text)
        if m:
            found["published"] = m.group(1)
    return found


def copy_name(r):
    host = urllib.parse.urlsplit(r["url"]).netloc.removeprefix("www.")
    slug = re.sub(r"[^A-Za-z0-9]+", "-", urllib.parse.urlsplit(r["url"]).path).strip("-")[-60:] or "index"
    return f"{r['date']}_{host}_{slug}"


def times(refetch=False):
    """Fetch each article, save a private copy, record times and hash in both logs."""
    from capture import fetch, is_challenge
    rows, _ = load()
    pub_rows, _ = load(PUBLIC)
    COPIES.mkdir(parents=True, exist_ok=True)
    done = {}
    for r in rows:
        if r.get("copy") and not refetch:
            continue
        now = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0)
        body, code, ctype, final, err, _, lastmod = fetch(r["url"])
        rec = {"fetched": now.isoformat().replace("+00:00", "Z"), "status": code}
        if err or not body or code != 200:
            rec["error"] = err or f"HTTP {code}"
        elif is_challenge(code, body, final or ""):
            rec["error"] = "blocked by a bot challenge; not saved"
        else:
            ext = ".pdf" if "pdf" in (ctype or "") else ".html"
            f = COPIES / (copy_name(r) + "_" + now.strftime("%Y%m%dT%H%M%SZ") + ext)
            f.write_bytes(body)
            rec.update({"sha256": hashlib.sha256(body).hexdigest(), "bytes": len(body), "file": f.name})
            if final and final != r["url"]:
                rec["final_url"] = final
            if lastmod:
                rec["last_modified_header"] = lastmod
            if ext == ".html":
                rec.update(page_times(body.decode("utf-8", errors="replace")))
        r["copy"] = rec
        done[r["url"]] = rec
        print(f"{'ok ' if 'sha256' in rec else 'ERR'} {r['date']} {r['title'][:60]:60} "
              f"published {rec.get('published', '-')}{'  ' + rec['error'] if 'error' in rec else ''}")
    LOG.write_text("".join(json.dumps(r) + "\n" for r in rows))
    # the public log gets the times and hash, not the private file name
    for r in pub_rows:
        if r["url"] in done:
            r["copy"] = {k: v for k, v in done[r["url"]].items() if k != "file"}
    PUBLIC.write_text("".join(json.dumps(r) + "\n" for r in pub_rows))
    print(f"{len(done)} fetched; copies in {COPIES}/")


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
    if PUBLISH_ALL and n:
        promote()


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
    c.add_argument("keys", nargs="*")
    c.add_argument("--all", action="store_true", help="publish every unpublished item")
    t = sub.add_parser("tag")
    t.add_argument("key")
    t.add_argument("states", help="comma-separated, e.g. PA,NJ")
    d = sub.add_parser("list")
    d.add_argument("--state")
    tm = sub.add_parser("times")
    tm.add_argument("--refetch", action="store_true", help="fetch again even if a copy exists")
    args = ap.parse_args()
    if args.cmd == "promote":
        if args.all == bool(args.keys):
            ap.error("promote: give URLs or --all, not both")
        promote(None if args.all else args.keys)
    elif args.cmd == "tag":
        tag(args.key, args.states)
    elif args.cmd == "list":
        unpublished(args.state)
    elif args.cmd == "times":
        times(args.refetch)
    elif args.cmd == "add-alert":
        append(parse_alert(pathlib.Path(args.file).read_text(), args.date, args.alert))
    else:
        st = tag_states(args.title + " " + args.snippet)
        st = sorted(set(st) | {s.strip() for s in args.states.split(",") if s.strip()})
        append([{"date": args.date, "title": args.title, "source": args.source, "snippet": args.snippet,
                 "url": args.url, "via": args.via, "states": st}])


if __name__ == "__main__":
    main()
