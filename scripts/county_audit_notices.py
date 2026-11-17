#!/usr/bin/env python3
"""Look through county election-office websites for notices of an upcoming post-election audit.

Purpose (2026-11-16): Colorado's 64 counties each run their part of the statewide RLA in the week
after the seed (Nov 16 to Nov 24, 2026), and many post the time and place of their audit board's
public session only on their own site. Neal asked which counties document this week's RLA. Given a
list of county start pages (one "County<TAB>URL" per line, e.g. from the Colorado County Clerks
Association's directory at https://www.clerkandrecorder.org/find-your-county-clerk), this fetches
each start page, follows same-site links whose text or URL looks election-related (elections,
notices, news, audit, canvass), one level deep, and reports every passage that mentions the audit
words, with the URL. It finds what a county posts as HTML; notices posted only as PDFs or images,
or built by JavaScript, are reported as "no mention" and need a human look.

Bot-challenge pages (see capture.is_challenge) are counted as blocked and never saved.

Usage:
    python3 -I scripts/county_audit_notices.py counties.tsv [--out DIR] [--max-pages 25]
        [--pattern 'risk[- ]limit|\\bRLA\\b|post[- ]election audit']
"""
import argparse
import concurrent.futures
import html
import json
import re
import subprocess
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from capture import is_challenge  # noqa: E402

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36"
FOLLOW = re.compile(r"(?i)election|vote|voting|notice|news|audit|canvass|announce|alert|calendar|events|public[- ]?meeting")
SKIP = re.compile(r"(?i)\.(jpg|jpeg|png|gif|svg|zip|docx?|xlsx?|mp4|ics)$|facebook|twitter|instagram|youtube|linkedin|mailto:|tel:|javascript:")
DEFAULT_PATTERN = r"(?i)risk[- ]limit|\bRLA\b|post[- ]election audit"


def fetch(url):
    r = subprocess.run(["curl", "-sL", "--compressed", "--max-time", "30", "-A", UA, "-w", "\n%{http_code} %{url_effective}", url],
                       capture_output=True)
    body, _, tail = r.stdout.rpartition(b"\n")
    parts = tail.decode(errors="replace").split(" ", 1)
    code = int(parts[0]) if parts[0].isdigit() else 0
    return code, (parts[1] if len(parts) > 1 else url), body.decode("utf-8", errors="replace")


def text_of(s):
    s = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", s)
    s = re.sub(r"(?s)<!--.*?-->", " ", s)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


ELECTION_HOST = re.compile(r"(?i)vote|elect")


def host_of(u):
    return urllib.parse.urlsplit(u).netloc.lower().removeprefix("www.")


def links(base, s):
    """Election-looking links on the same site, plus any link to a separate elections site
    (many clerks run one, e.g. weldvotes.gov)."""
    host = host_of(base)
    out = []
    for href, label in re.findall(r'(?is)<a[^>]+href="([^"#]+)[^"]*"[^>]*>(.*?)</a>', s):
        u = urllib.parse.urljoin(base, html.unescape(href))
        if SKIP.search(u) or not u.startswith("http"):
            continue
        if host_of(u) != host and not ELECTION_HOST.search(host_of(u)):
            continue
        if FOLLOW.search(u) or FOLLOW.search(text_of(label)):
            out.append(u)
    return list(dict.fromkeys(out))


def scan_county(county, start, pattern, max_pages):
    rec = {"county": county, "start": start, "pages": 0, "blocked": 0, "errors": 0, "hits": []}
    # depth 0 is the start page; its links are depth 1; an election page or separate elections
    # site at depth 1 gets its own links followed once more (depth 2)
    seen, queue = set(), [(start, 0)]
    while queue and rec["pages"] < max_pages:
        u, depth = queue.pop(0)
        if u in seen:
            continue
        seen.add(u)
        code, final, s = fetch(u)
        if code != 200 or not s:
            rec["errors"] += 1
            continue
        if is_challenge(code, s.encode(errors="replace"), final):
            rec["blocked"] += 1
            continue
        rec["pages"] += 1
        if u.lower().endswith(".pdf") or s.startswith("%PDF"):
            continue
        t = text_of(s)
        for m in re.finditer(pattern, t):
            snip = t[max(0, m.start() - 200):m.end() + 300]
            if not any(snip[150:250] in h["text"] for h in rec["hits"]):
                rec["hits"].append({"url": final, "text": snip})
        if depth == 0 or (depth == 1 and (ELECTION_HOST.search(host_of(final)) or re.search(r"(?i)election", final))):
            queue += [(x, depth + 1) for x in links(final, s) if x not in seen]
    return rec


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("counties", help="TSV file: county name, tab, start URL")
    ap.add_argument("--out", default=None, help="write results as JSON lines here")
    ap.add_argument("--max-pages", type=int, default=40)
    ap.add_argument("--pattern", default=DEFAULT_PATTERN)
    ap.add_argument("--workers", type=int, default=8)
    a = ap.parse_args()
    rows = [l.rstrip("\n").split("\t") for l in open(a.counties) if l.strip() and not l.startswith("#")]
    pat = re.compile(a.pattern)
    with concurrent.futures.ThreadPoolExecutor(a.workers) as ex:
        results = list(ex.map(lambda r: scan_county(r[0], r[1], pat, a.max_pages), rows))
    out = open(a.out, "w") if a.out else None
    for r in sorted(results, key=lambda r: r["county"]):
        if out:
            out.write(json.dumps(r) + "\n")
        flag = f"{len(r['hits'])} mention(s)" if r["hits"] else "no mention"
        print(f"{r['county']:14} {flag:14} pages {r['pages']:2} blocked {r['blocked']} errors {r['errors']}  {r['start']}")
        for h in r["hits"][:4]:
            print(f"    {h['url']}\n      ...{h['text']}...")


if __name__ == "__main__":
    main()
