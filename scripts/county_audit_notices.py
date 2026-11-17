#!/usr/bin/env python3
"""Look through county election-office websites for notices of an upcoming post-election audit.

Purpose (2026-11-16): Colorado's 64 counties each run their part of the statewide RLA in the week
after the seed (Nov 16 to Nov 24, 2026), and many post the time and place of their audit board's
public session only on their own site. Neal asked which counties document this week's RLA. Given a
list of county start pages (one "County<TAB>URL" per line, e.g. from the Colorado County Clerks
Association's directory at https://www.clerkandrecorder.org/find-your-county-clerk), this fetches
each start page, follows same-site links whose text or URL looks election-related (elections,
notices, news, audit, canvass), one level deep, and reports every passage that mentions the audit
words, with the URL.

Many notices aren't in a page's HTML, so it also probes, per site (revised 2026-11-17, after
Arapahoe's Nov 18 RLA turned out to be only in its JavaScript event calendar):
- PDFs linked from election pages whose name or link text looks like a notice, calendar or audit
  (text extracted with pdftotext);
- Revize event calendars (their JSON data handler), CivicPlus calendar and news RSS feeds and site
  search, WordPress search and REST API (posts and The Events Calendar), Drupal site search;
- the site's sitemap.xml, for URLs that name an audit, canvass or RLA.
Hits that also mention a date in the audit window (--window, default Nov 16-25) are flagged "DATED".
Images (flyers, calendar graphics) and Facebook posts are still out of reach.

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


PDF_WANT = re.compile(r"(?i)notice|audit|canvass|rla|calendar|dates|timeline|schedule|public")
NAMEISH = re.compile(r"(?i)audit|canvass|rla|risk")


def pdf_text(url):
    r = subprocess.run(["curl", "-sL", "--max-time", "40", "-A", UA, url], capture_output=True)
    if not r.stdout.startswith(b"%PDF"):
        return ""
    t = subprocess.run(["pdftotext", "-q", "-", "-"], input=r.stdout, capture_output=True)
    return re.sub(r"\s+", " ", t.stdout.decode(errors="replace"))


def revize_events(base, s):
    m = re.search(r'RZ\.webspace\s*=\s*"([^"]+)"', s)
    if not m:
        return []
    root = "{0.scheme}://{0.netloc}".format(urllib.parse.urlsplit(base))
    u = (f"{root}/_assets_/plugins/revizeCalendar/calendar_data_handler.php?webspace={m.group(1)}"
         "&relative_revize_url=//cms2.revize.com&protocol=https:")
    code, _, body = fetch(u)
    try:
        ev = json.loads(body) if code == 200 else []
    except ValueError:
        return []
    out = []
    for e in ev:
        if (e.get("start") or "") < "2026-10":
            continue
        desc = text_of(urllib.parse.unquote(e.get("desc") or ""))
        out.append((f"{root}/calendar.php (event {e.get('id')})", f"{e.get('start')} {e.get('title')}: {desc}"))
    return out


def probe_urls(base, s):
    """Platform-specific places notices hide: feeds, calendars, search results, sitemaps."""
    root = "{0.scheme}://{0.netloc}".format(urllib.parse.urlsplit(base))
    q = "risk+limiting+audit"
    us = [root + "/sitemap.xml"]
    if re.search(r"(?i)civicplus|/DocumentCenter/|/AgendaCenter|CivicAlerts", s):
        us += [root + "/RSSFeed.aspx?ModID=58&CID=All-calendar.xml", root + "/RSSFeed.aspx?ModID=1&CID=All-newsflash.xml",
               root + "/RSSFeed.aspx?ModID=63&CID=All-0", root + f"/Search?searchPhrase={q}"]
    if re.search(r"(?i)wp-content|wordpress", s):
        us += [root + f"/?s={q}", root + "/wp-json/wp/v2/posts?search=audit&per_page=20",
               root + "/wp-json/wp/v2/pages?search=audit&per_page=20",
               root + "/wp-json/tribe/events/v1/events?start_date=2026-11-10&per_page=50"]
    if re.search(r"(?i)drupal", s):
        us += [root + f"/search?keys={q}", root + f"/search/node?keys={q}", root + f"/search?search_api_fulltext={q}"]
    return us


def add_hits(rec, url, t, pattern):
    for m in re.finditer(pattern, t):
        snip = t[max(0, m.start() - 200):m.end() + 300]
        if not any(snip[150:250] in h["text"] for h in rec["hits"]):
            rec["hits"].append({"url": url, "text": snip})


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
        add_hits(rec, final, text_of(s), pattern)
        if depth == 0:
            for pu in probe_urls(final, s):
                pc, pf, ps = fetch(pu)
                if pc != 200 or not ps or is_challenge(pc, ps.encode(errors="replace"), pf):
                    continue
                rec["probes"] = rec.get("probes", 0) + 1
                if pu.endswith("sitemap.xml"):
                    queue += [(x, 2) for x in re.findall(r"<loc>([^<]+)</loc>", ps) if NAMEISH.search(x)][:15]
                    continue
                add_hits(rec, pu, text_of(ps) if "<" in ps else ps, pattern)
                queue += [(x, 2) for x in links(pf, ps) if NAMEISH.search(x)][:10]
            for eu, et in revize_events(final, s):
                add_hits(rec, eu, et, pattern)
        for pdf, label in re.findall(r'(?is)<a[^>]+href="([^"#]+\.pdf[^"]*)"[^>]*>(.*?)</a>', s):
            pu = urllib.parse.urljoin(final, html.unescape(pdf))
            if pu in seen or not (PDF_WANT.search(pu) or PDF_WANT.search(text_of(label))) or rec.get("pdfs", 0) >= 12:
                continue
            seen.add(pu)
            rec["pdfs"] = rec.get("pdfs", 0) + 1
            add_hits(rec, pu, pdf_text(pu), pattern)
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
    ap.add_argument("--window", default=r"(?i)\b(nov(ember)?\.?\s*(1[6-9]|2[0-5])|11/(1[6-9]|2[0-5]))\b",
                    help="regex for dates in the audit window")
    a = ap.parse_args()
    window = re.compile(a.window)
    rows = [l.rstrip("\n").split("\t") for l in open(a.counties) if l.strip() and not l.startswith("#")]
    pat = re.compile(a.pattern)
    with concurrent.futures.ThreadPoolExecutor(a.workers) as ex:
        results = list(ex.map(lambda r: scan_county(r[0], r[1], pat, a.max_pages), rows))
    out = open(a.out, "w") if a.out else None
    for r in sorted(results, key=lambda r: r["county"]):
        for h in r["hits"]:
            h["dated"] = bool(window.search(h["text"]))
        dated = [h for h in r["hits"] if h["dated"]]
        flag = f"DATED {len(dated)}" if dated else (f"{len(r['hits'])} mention(s)" if r["hits"] else "no mention")
        print(f"{r['county']:14} {flag:14} pages {r['pages']:2} pdfs {r.get('pdfs', 0):2} probes {r.get('probes', 0)} "
              f"blocked {r['blocked']} errors {r['errors']}  {r['start']}")
        for h in (dated or r["hits"])[:4]:
            print(f"    {h['url']}\n      ...{h['text']}...")
        if out:
            out.write(json.dumps(r) + "\n")


if __name__ == "__main__":
    main()
