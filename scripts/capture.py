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
    python3 -I scripts/capture.py --loop 1800 --until 2026-11-22T00:00Z   # every 30 min
"""
import argparse
import datetime
import hashlib
import html
import json
import pathlib
import re
import subprocess
import time

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36"


def utcnow():
    return datetime.datetime.now(datetime.timezone.utc)


def fetch(url):
    r = subprocess.run(["curl", "-sS", "-L", "--compressed", "--max-time", "90", "-A", UA,
                        "-o", "-", "-w", "\n__META__%{http_code}\t%{content_type}\t%{url_effective}", url],
                       capture_output=True)
    if r.returncode != 0:
        return None, None, None, None, r.stderr.decode(errors="replace").strip()[:200]
    out = r.stdout
    i = out.rfind(b"\n__META__")
    body, meta = out[:i], out[i + 9:].decode(errors="replace")
    code, ctype, final = (meta.split("\t") + ["", "", ""])[:3]
    return body, int(code or 0), ctype, final, None


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


def one_round(watch, out):
    log = out / "log.jsonl"
    last = {}
    if log.exists():
        for line in log.read_text().splitlines():
            r = json.loads(line)
            if r.get("text_sha256"):
                last[r["slug"]] = r["text_sha256"]
            elif r.get("file") and (out.parent / r["file"]).exists():
                # older entries have only the raw hash: derive the text hash from the saved copy
                f = out.parent / r["file"]
                last[r["slug"]] = text_hash(f.read_bytes(), r.get("content_type") or "")
    with log.open("a") as lf:
        for w in watch:
            t = utcnow()
            body, code, ctype, final, err = fetch(w["url"])
            rec = {"time": t.isoformat(timespec="seconds").replace("+00:00", "Z"), "slug": w["slug"],
                   "state": w["state"], "url": w["url"], "status": code, "error": err}
            if body is not None:
                blocked = code == 403 or b"challenges.cloudflare.com" in body[:20000] or b"cf-mitigated" in body[:4000]
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
        one_round(watch, out)
        print(f"{utcnow().isoformat(timespec='seconds')} round done ({len(watch)} URLs)", flush=True)
        if not a.loop or (until and utcnow() >= until):
            break
        time.sleep(a.loop)


if __name__ == "__main__":
    main()
