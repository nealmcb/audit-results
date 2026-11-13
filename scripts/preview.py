#!/usr/bin/env python3
"""Build the site locally with GitHub Pages' own Jekyll, and screenshot pages at phone and desktop widths.

Purpose (2026-11-10): to check layout (header menu, state bar, footer) before pushing, instead of
pushing and screenshotting the live site. Needs ruby-dev and the gems from the Gemfile
(`bundle config set --local path vendor/bundle && bundle install`, with bundler from
`gem install --user-install bundler -v '~> 2.4.0'`).

Usage:
    python3 -I scripts/preview.py                      # build, screenshot the home page
    python3 -I scripts/preview.py states/WY/ calendar/ # also these pages
    python3 -I scripts/preview.py --full               # whole page, trimmed to its length
    python3 -I scripts/preview.py --tail 700           # just the bottom 700 px (the footer)
    python3 -I scripts/preview.py --widths calendar/   # does the page or a table scroll sideways?
    python3 -I scripts/preview.py --serve              # build, then serve until Ctrl-C

Screenshots go to _site/shots/<page>-<width>.png (phone 390 px and desktop 1200 px, both at 2x).
Note: headless Chrome lays out --widths pages at least ~485 px wide, a bit wider than a phone;
screenshots do use the true 390 px.
The site is served at http://127.0.0.1:PORT/audit-results/ to match its GitHub Pages baseurl;
screenshots use a free port, so they work while a --serve is running.
"""
import argparse
import functools
import http.server
import io
import os
import pathlib
import re
import subprocess
import threading

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "_site"
WIDTHS = {"phone": (390, 1400), "desktop": (1200, 1000)}


def build():
    env = dict(os.environ, PATH=f"{pathlib.Path.home()}/.gem/ruby/3.0.0/bin:" + os.environ["PATH"])
    subprocess.run(["bundle", "exec", "jekyll", "build", "-q", "-d", str(SITE / "audit-results"),
                    "--baseurl", "/audit-results"], cwd=ROOT, env=env, check=True)


# minima sets body { min-height: 100vh }, which pins the footer to the bottom of the very tall
# window used for --full and --tail screenshots, leaving a big blank gap above it.
TALL_FIX = b"<style>body { min-height: 0 !important; }</style></head>"
# For --widths: report the page's and each scroll box's content width vs. visible width.
WIDTH_JS = (b"<script>document.title = 'page ' + document.documentElement.scrollWidth + '/' +"
            b" document.documentElement.clientWidth + ' ' + [...document.querySelectorAll("
            b"'.table-scroll')].map(d => 'box ' + d.scrollWidth + '/' + d.clientWidth).join(' ') +"
            # elements whose own content overflows them (text that can't wrap doesn't widen its
            # box, so compare each element's scrollWidth with its clientWidth), innermost first
            b" [...document.querySelectorAll('body *')].filter(e => !e.closest('.table-scroll') &&"
            b" ![e, ...(function a(x) { const r = []; while ((x = x.parentElement)) r.push(x); return r; })(e)]"
            b".some(x => ['auto', 'scroll'].includes(getComputedStyle(x).overflowX)) &&"
            b" e.clientWidth && e.scrollWidth > e.clientWidth + 1 && ![...e.children].some(c =>"
            b" c.clientWidth && c.scrollWidth > c.clientWidth + 1)).slice(0, 3).map(e =>"
            b" ' | too wide: ' + e.tagName + ' ' + (e.textContent || '').trim().slice(0, 50)).join('')"
            b"</script></body>")


class Handler(http.server.SimpleHTTPRequestHandler):
    tall = False

    def log_message(self, *a):
        pass

    def send_head(self):
        path = pathlib.Path(self.translate_path(self.path))
        if path.is_dir() and self.path.endswith("/"):
            path = path / "index.html"
        widths = self.path.endswith("?widths")
        if widths:
            path = pathlib.Path(self.translate_path(self.path.removesuffix("?widths")))
            if path.is_dir():
                path = path / "index.html"
        if not ((self.tall or widths) and path.suffix == ".html" and path.is_file()):
            return super().send_head()
        data = path.read_bytes()
        data = data.replace(b"</body>", WIDTH_JS, 1) if widths else data.replace(b"</head>", TALL_FIX, 1)
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        return io.BytesIO(data)


def serve(port, tall=False):
    Handler.tall = tall
    handler = functools.partial(Handler, directory=str(SITE))
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", port), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


def trim(path, tail=None):
    """Cut the blank space below a tall screenshot; with tail, keep only the bottom TAIL css px."""
    from PIL import Image, ImageChops
    im = Image.open(path).convert("RGB")
    bg = Image.new("RGB", im.size, im.getpixel((0, im.height - 1)))
    box = ImageChops.difference(im, bg).getbbox()
    if box:
        im = im.crop((0, 0, im.width, min(im.height, box[3] + 40)))
    if tail:
        im = im.crop((0, max(0, im.height - 2 * tail), im.width, im.height))
    im.save(path)


def widths(base, page):
    """Print content/visible widths at each screen width: content wider than visible means the
    page (or that scroll box) scrolls sideways."""
    for label, (w, _) in WIDTHS.items():
        r = subprocess.run(["google-chrome", "--headless=new", "--disable-gpu", f"--window-size={w},800",
                            "--dump-dom", base + page + "?widths"], capture_output=True, text=True, timeout=90)
        m = re.search(r"<title>([^<]*)", r.stdout)
        print(f"{page or 'home'} {label}: {m.group(1) if m else 'no result'}")


def shoot(base, page, shots, full=False, tail=None):
    name = page.strip("/").replace("/", "_") or "home"
    for label, (w, h) in WIDTHS.items():
        h = 12000 if (full or tail) else h
        out = shots / f"{name}-{label}.png"
        subprocess.run(["google-chrome", "--headless=new", "--disable-gpu", "--hide-scrollbars",
                        f"--window-size={w},{h}", "--force-device-scale-factor=2",
                        f"--screenshot={out}", base + page],
                       check=True, capture_output=True, timeout=90)
        if full or tail:
            trim(out, tail)
        print(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("pages", nargs="*", default=[""], help="paths under the site, e.g. states/WY/")
    ap.add_argument("--port", type=int, help="default 4001 with --serve, else any free port")
    ap.add_argument("--serve", action="store_true", help="keep serving after the build")
    ap.add_argument("--full", action="store_true", help="screenshot the whole page")
    ap.add_argument("--tail", type=int, help="keep only the bottom N css px of the page")
    ap.add_argument("--widths", action="store_true",
                    help="instead of screenshots, report content vs. visible widths (sideways scrolling)")
    a = ap.parse_args()
    build()
    port = a.port if a.port is not None else (4001 if a.serve else 0)
    srv = serve(port, tall=bool(a.full or a.tail) and not a.serve)
    base = f"http://127.0.0.1:{srv.server_address[1]}/audit-results/"
    if a.serve:
        print(f"serving {base} (Ctrl-C to stop)", flush=True)
        threading.Event().wait()
    shots = SITE / "shots"
    shots.mkdir(exist_ok=True)
    for p in a.pages:
        if a.widths:
            widths(base, p)
        else:
            shoot(base, p, shots, a.full, a.tail)
    srv.shutdown()


if __name__ == "__main__":
    main()
