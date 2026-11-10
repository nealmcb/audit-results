#!/usr/bin/env python3
"""Capture state audit pages repeatedly, keeping a timestamped, hashed copy each time they change.

Purpose (2026-11-10): to show what each state had published before its audit's random seed was
drawn, we need copies of the relevant pages captured before the draw, with times. This fetches
every URL in watchlist.json, stores a new copy under captures/<slug>/ only when the content hash
changes, and appends one line per fetch to captures/log.jsonl (UTC time, slug, URL, HTTP status,
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
            if r.get("sha256"):
                last[r["slug"]] = r["sha256"]
    with log.open("a") as lf:
        for w in watch:
            t = utcnow()
            body, code, ctype, final, err = fetch(w["url"])
            rec = {"time": t.isoformat(timespec="seconds").replace("+00:00", "Z"), "slug": w["slug"],
                   "state": w["state"], "url": w["url"], "status": code, "error": err}
            if body is not None:
                blocked = code == 403 or b"challenges.cloudflare.com" in body[:20000] or b"cf-mitigated" in body[:4000]
                sha = hashlib.sha256(body).hexdigest()
                changed = sha != last.get(w["slug"])
                rec.update(sha256=None if blocked else sha, bytes=len(body), content_type=ctype,
                           final_url=final, blocked=blocked, changed=changed and not blocked)
                if changed and not blocked and code and 200 <= code < 300:
                    d = out / w["slug"]
                    d.mkdir(parents=True, exist_ok=True)
                    f = d / (t.strftime("%Y%m%dT%H%M%SZ") + ext_for(ctype, w["url"]))
                    f.write_bytes(body)
                    rec["file"] = str(f.relative_to(out.parent))
                    last[w["slug"]] = sha
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
