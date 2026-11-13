#!/usr/bin/env python3
"""Turn a YouTube auto-caption file (WebVTT) into plain timestamped lines, without the repeats.

Purpose (2026-11-13): to read what was said at a recorded dice-roll ceremony (Washington's Nov 6
seed roll) when the video itself can't be downloaded. YouTube's auto-captions repeat each phrase
as it scrolls and embed per-word timing tags; this keeps each new piece of text once, with the
time it first appeared, offset into the video and, given --start, as UTC wall-clock time.

Usage:
    python3 -I scripts/vtt_text.py FILE.vtt [--start 2026-11-06T23:02:09Z] [--grep REGEX]
"""
import argparse
import datetime
import html
import re
import sys

CUE = re.compile(r"^(\d+):(\d\d):(\d\d)\.(\d+) --> ")


def cues(text):
    """Yield (seconds, text) for each cue, with timing tags and markup removed."""
    t, buf = None, []
    for line in text.splitlines() + [""]:
        m = CUE.match(line)
        if m:
            t = int(m[1]) * 3600 + int(m[2]) * 60 + int(m[3]) + int(m[4]) / 1000
            buf = []
        elif line.strip() == "" and t is not None:
            yield t, " ".join(buf)
            t = None
        elif t is not None:
            buf.append(html.unescape(re.sub(r"<[^>]+>", "", line)).strip())


def dedup(items):
    """YouTube rolls captions: each cue repeats the previous line. Keep only the new text."""
    seen, last = "", None
    for t, s in items:
        s = re.sub(r"\s+", " ", s).strip()
        # skip only exact back-to-back repeats: a short line like ">> Nine." can recur legitimately
        if not s or s == last:
            continue
        last = s
        new = s
        for k in range(min(len(s), len(seen)), 0, -1):  # longest overlap with what we have
            if seen.endswith(s[:k]):
                new = s[k:].strip()
                break
        if new:
            seen += " " + new
            yield t, new


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("file")
    ap.add_argument("--start", help="UTC time the video starts, e.g. 2026-11-06T23:02:09Z")
    ap.add_argument("--grep", help="only lines matching this regex (case-insensitive)")
    a = ap.parse_args()
    start = datetime.datetime.fromisoformat(a.start.replace("Z", "+00:00")) if a.start else None
    for t, s in dedup(cues(open(a.file, encoding="utf-8", errors="replace").read())):
        if a.grep and not re.search(a.grep, s, re.I):
            continue
        wall = f" {(start + datetime.timedelta(seconds=t)).strftime('%H:%M:%SZ')}" if start else ""
        print(f"{int(t // 60):2d}:{t % 60:04.1f}{wall}  {s}")


if __name__ == "__main__":
    sys.exit(main())
