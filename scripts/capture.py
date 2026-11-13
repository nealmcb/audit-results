#!/usr/bin/env python3
"""Capture state audit pages repeatedly, keeping a timestamped, hashed copy each time they change.

Purpose (2026-11-10): to show what each state had published before its audit's random seed was
drawn, we need copies of the relevant pages captured before the draw, with times. This fetches
every URL in watchlist.json, stores a new copy under captures/<slug>/ only when its content
changes (for HTML, its visible text, since many sites embed random IDs in their markup), and appends one line per fetch to captures/log.jsonl (UTC time, slug, URL, HTTP status,
sha256, bytes, whether it changed, and "blocked" when a bot challenge or 403 was returned).
Blocked URLs need a browser save, archive.ph, or a Cowork/Grok/Gemini prompt instead.

Committing captures/log.jsonl to the public repo after each round gives an independent,
timestamped record (git history plus GitHub's push time) of what was seen when.

Usage:
    python3 -I scripts/capture.py [--watchlist watchlist.json] [--out captures]
    python3 -I scripts/capture.py --loop 1800 --until 2026-11-22T00:00Z   # adaptive, from every 30 min

With --loop, pages are fetched on an adaptive schedule (see interval_for): unchanged pages back off
to every 12 hours, pages that always refuse to once a day, and "hot_until" in a watchlist entry keeps
a page at the base interval through an event. Requests are conditional (ETag, Last-Modified) where
the server supports it, and a 304 Not Modified is logged as unchanged.
"""
import argparse
import datetime
import hashlib
import html
import json
import os
import pathlib
import re
import subprocess
import tempfile
import time
import urllib.parse

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36"


def utcnow():
    return datetime.datetime.now(datetime.timezone.utc)


def fetch(url, etag=None, last_modified=None):
    """GET url, conditionally if we have its ETag or Last-Modified. Returns body (None on a 304
    or an error), status, content type, final URL, error, and the response's ETag and Last-Modified."""
    hdr = tempfile.NamedTemporaryFile(delete=False)
    hdr.close()
    argv = ["curl", "-sS", "-L", "--compressed", "--max-time", "90", "-A", UA, "-D", hdr.name,
            "-o", "-", "-w", "\n__META__%{http_code}\t%{content_type}\t%{url_effective}"]
    if etag:
        argv += ["-H", f"If-None-Match: {etag}"]
    if last_modified:
        argv += ["-H", f"If-Modified-Since: {last_modified}"]
    r = subprocess.run(argv + [url], capture_output=True)
    heads = pathlib.Path(hdr.name).read_text(errors="replace")
    os.unlink(hdr.name)
    # the last response's headers (after redirects)
    block = heads.strip().split("\r\n\r\n")[-1]
    h = {k.strip().lower(): v.strip() for k, _, v in (l.partition(":") for l in block.splitlines()[1:]) if _}
    if r.returncode != 0:
        return None, None, None, None, r.stderr.decode(errors="replace").strip()[:200], None, None
    out = r.stdout
    i = out.rfind(b"\n__META__")
    body, meta = out[:i], out[i + 9:].decode(errors="replace")
    code, ctype, final = (meta.split("\t") + ["", "", ""])[:3]
    code = int(code or 0)
    return (None if code == 304 else body), code, ctype, final, None, h.get("etag"), h.get("last-modified")


# Adaptive schedule. The loop wakes every --loop seconds (the base interval); a page is fetched
# only when due. Each fetch that finds no change doubles its interval, up to MAX_INTERVAL; a change
# resets it to the base. A page that has refused every fetch drops to once a day. A watchlist entry's
# "hot_until" (UTC) keeps it at the base interval until then, e.g. through a seed draw.
MAX_INTERVAL = 12 * 3600
REFUSED_INTERVAL = 24 * 3600


def parse_time(s):
    return datetime.datetime.fromisoformat(s.replace("Z", "+00:00"))


def interval_for(w, history, base, now):
    """Seconds between fetches for watchlist entry w, given its log records (oldest first)."""
    if w.get("hot_until") and now < parse_time(w["hot_until"]):
        return base
    ok = lambda r: r.get("status") in (304,) or (r.get("status") and 200 <= r["status"] < 300 and not r.get("blocked"))
    if len(history) >= 3 and not any(ok(r) for r in history):
        return REFUSED_INTERVAL
    quiet = 0
    for r in reversed(history):
        if r.get("file"):
            break
        quiet += 1
    return min(base * 2 ** quiet, MAX_INTERVAL)


def is_due(w, history, base, now):
    if not history:
        return True
    elapsed = (now - parse_time(history[-1]["time"])).total_seconds()
    return elapsed >= interval_for(w, history, base, now) - 120  # two minutes' slack for round timing


# Per-load noise seen in visible text: UUID-like IDs, cache-busting "digits-digits" tokens and
# clock times. Plain 20-digit numbers are deliberately NOT filtered: a seed appearing on a page is
# exactly the change we want to catch.
NOISE = [
    re.compile(r"\b[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}\b", re.I),
    re.compile(r"\b\d{15,}-\d{10,}\b"),
    re.compile(r"\b\d{1,2}:\d{2}:\d{2}\b"),
    # a date with a clock time, as on live results pages ("Updated 11/12/2026 04:30 PM", a county's
    # "11/12/26 12:03 PM"); dates alone, and seeds, still count as changes
    re.compile(r"\b\d{1,2}/\d{1,2}/\d{2,4} +\d{1,2}:\d{2}(?::\d{2})? *[AP]M\b", re.I),
    # South Carolina's live count of registered voters
    re.compile(r"\b\d{1,3}(?:,\d{3})+ Current number of registered voters", re.I),
    # a spam-trap form field whose label rotates between loads ("CAPTCHA Comments", "CAPTCHA Email")
    re.compile(r"CAPTCHA \w+ This field is for validation purposes"),
]


def text_hash(body, ctype):
    """Hash of the visible text for HTML pages (so random IDs in markup don't count as changes);
    the raw bytes for everything else."""
    if "html" not in (ctype or ""):
        return hashlib.sha256(body).hexdigest()
    s = body.decode("utf-8", errors="replace")
    s = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", s)
    s = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()
    for rx in NOISE:
        s = rx.sub("~", s)
    return hashlib.sha256(s.encode()).hexdigest()


def ext_for(ctype, url):
    if "pdf" in (ctype or ""):
        return ".pdf"
    if "html" in (ctype or ""):
        return ".html"
    m = re.search(r"\.(xlsx?|csv|zip|json|txt|docx?)(?:$|\?)", url, re.I)
    return "." + m.group(1).lower() if m else ".bin"


# Bot-challenge pages served instead of the real page (sometimes with HTTP 200). They are not
# evidence, so they count as blocked and are never saved.
CHALLENGE_MARKERS = (b"challenges.cloudflare.com", b"cf-mitigated", b"Radware Captcha Page",
                     b"botmanager_support@radware.com", b"think that you are a bot",
                     b"Incapsula incident ID", b"_Incapsula_Resource")


def is_challenge_host(url):
    host = (urllib.parse.urlsplit(url).hostname or "").lower()
    return "radware" in host or "perfdrive" in host


def redact_url(url):
    """A challenge redirect's URL without its query, which is only session data."""
    u = urllib.parse.urlsplit(url)
    return f"{u.scheme}://{u.netloc}{u.path}"


def is_challenge(code, body, final_url=""):
    if code == 403:
        return True
    if final_url and is_challenge_host(final_url):
        return True
    head = body[:60000]
    return any(m in head for m in CHALLENGE_MARKERS)


def one_round(watch, out, base=None):
    """Fetch every watched page (or, with base, every page that is due under the schedule)."""
    log = out / "log.jsonl"
    last, history, validators = {}, {}, {}
    if log.exists():
        for line in log.read_text().splitlines():
            r = json.loads(line)
            history.setdefault(r["slug"], []).append(r)
            if r.get("etag") or r.get("last_modified"):
                validators[r["slug"]] = (r.get("etag"), r.get("last_modified"))
            if r.get("text_sha256"):
                last[r["slug"]] = r["text_sha256"]
            elif r.get("file") and (out.parent / r["file"]).exists():
                # older entries have only the raw hash: derive the text hash from the saved copy
                f = out.parent / r["file"]
                last[r["slug"]] = text_hash(f.read_bytes(), r.get("content_type") or "")
    with log.open("a") as lf:
        fetched = 0
        for w in watch:
            t = utcnow()
            if base and not is_due(w, history.get(w["slug"], []), base, t):
                continue
            fetched += 1
            etag, lastmod = validators.get(w["slug"], (None, None))
            body, code, ctype, final, err, new_etag, new_lastmod = fetch(w["url"], etag, lastmod)
            if final and is_challenge_host(final):
                final = redact_url(final)
            rec = {"time": t.isoformat(timespec="seconds").replace("+00:00", "Z"), "slug": w["slug"],
                   "state": w["state"], "url": w["url"], "status": code, "error": err}
            if new_etag or new_lastmod:
                rec.update(etag=new_etag, last_modified=new_lastmod)
            if code == 304:
                rec.update(changed=False, not_modified=True)
            if body is not None:
                blocked = is_challenge(code, body, final)
                sha = hashlib.sha256(body).hexdigest()
                tsha = text_hash(body, ctype)
                changed = tsha != last.get(w["slug"])
                rec.update(sha256=None if blocked else sha, text_sha256=None if blocked else tsha,
                           bytes=len(body), content_type=ctype,
                           final_url=final, blocked=blocked, changed=changed and not blocked)
                if changed and not blocked and code and 200 <= code < 300:
                    d = out / w["slug"]
                    d.mkdir(parents=True, exist_ok=True)
                    f = d / (t.strftime("%Y%m%dT%H%M%SZ") + ext_for(ctype, w["url"]))
                    f.write_bytes(body)
                    rec["file"] = str(f.relative_to(out.parent))
                    last[w["slug"]] = tsha
            lf.write(json.dumps(rec) + "\n")
            lf.flush()
            time.sleep(2)
    return fetched


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--watchlist", default="watchlist.json")
    ap.add_argument("--out", default="captures")
    ap.add_argument("--loop", type=int, help="repeat every N seconds")
    ap.add_argument("--until", help="stop looping after this UTC time, e.g. 2026-11-22T00:00Z")
    a = ap.parse_args()
    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    until = datetime.datetime.fromisoformat(a.until.replace("Z", "+00:00")) if a.until else None
    while True:
        watch = json.loads(pathlib.Path(a.watchlist).read_text())  # re-read so edits apply
        n = one_round(watch, out, base=a.loop)
        print(f"{utcnow().isoformat(timespec='seconds')} round done ({n} of {len(watch)} URLs due)", flush=True)
        if not a.loop or (until and utcnow() >= until):
            break
        time.sleep(a.loop)


if __name__ == "__main__":
    main()
