#!/usr/bin/env python3
"""Timestamp the evidence we hold: versioned SHA256SUMS files, OpenTimestamps proofs, Sigstore signatures.

Purpose (2026-11-11): the captures and other evidence in this repository only show what states
published before their random draws if we can prove when we had each file. Git commit dates
prove nothing (the committer sets them) and a push to GitHub is not a trusted time. So this
writes a SHA256SUMS file listing the hash of every evidence file and timestamps it two
independent ways:

- **OpenTimestamps** (``ots stamp``): anchors the SUMS file's hash in a Bitcoin block, provable to
  anyone without trusting us or any server. Pending until a calendar's transaction confirms,
  usually within an hour or two; ``upgrade`` then fetches the complete proof.
- **Sigstore** (``cosign sign-blob --bundle``): a signature recorded in the public Rekor
  transparency log, whose signed entry time is a second timestamp. Keyless (bound to an OIDC
  login such as a GitHub or Google account, which needs a browser or device-code login) or with a
  key file whose public key is published.

Ported from corla-observer's ``timestamp.py`` (the July 2026 Colorado observer procedure, see its
docs/TIMESTAMPING.md), keeping its rules: SUMS versions are ``SHA256SUMS.txt``, then
``SHA256SUMS.v2.txt`` and so on; a version that exists or ever existed in the repository's history
is never reused, and the file is created exclusively, so no commitment is ever overwritten. Each
step's outcome is printed (DONE, PENDING, SKIPPED or FAILED); nothing is skipped silently.

Signing: by default each new SUMS file is signed with the repository's cosign key, kept outside
the repository at ~/Private/audit-evidence/cosign.key (no password: it relies on that directory
being private), whose public key is published as timestamps/cosign.pub. That signature proves only
that the same key signed each version, but cosign also records it in the public Rekor log, which
gives a signed time. A keyless signature (``--keyless``), bound to a person's GitHub or Google
login, needs that person at a browser; it is stored beside the key-file one as
``<sums>.keyless.cosign-bundle``. ``sign`` adds either kind to an existing SUMS file.

Unlike corla-observer, this does not commit or push: Neal approves every commit, so the SUMS file
and proofs are left in timestamps/ for the usual commit.

The evidence set is every file git would track under captures/ and evidence/ (ignored files such
as the capture loop's log and PID file are left out). evidence/ is for files obtained other ways,
such as a Cowork download or a browser save, kept under evidence/<STATE>/.

Usage:
    python3 -I scripts/stamp.py stamp [--note TEXT] [--keyless] [--no-key]
    python3 -I scripts/stamp.py sign [timestamps/SHA256SUMS.v2.txt] [--keyless]   # sign an existing one
    python3 -I scripts/stamp.py upgrade          # fetch completed OpenTimestamps proofs
    python3 -I scripts/stamp.py verify [timestamps/SHA256SUMS.v2.txt]
        [--certificate-identity EMAIL --certificate-oidc-issuer URL]

Anyone can check a commitment without this script:
    sha256sum --check --ignore-missing timestamps/SHA256SUMS.v2.txt   (run from the repo root)
    ots verify timestamps/SHA256SUMS.v2.txt.ots                       (or opentimestamps.org)
    cosign verify-blob --key timestamps/cosign.pub --bundle timestamps/SHA256SUMS.v2.txt.cosign-bundle \
        timestamps/SHA256SUMS.v2.txt
"""
import argparse
import datetime
import hashlib
import os
import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = "timestamps"
EVIDENCE_DIRS = ("captures", "evidence")
SUMS_NAME_RE = re.compile(r"^SHA256SUMS(?:\.v([1-9][0-9]*))?\.txt$")
SUMS_LINE_RE = re.compile(r"^([0-9a-f]{64}) [ *](.+)$")
OTS_BITCOIN_TAG = bytes.fromhex("0588960d73d71901")  # OpenTimestamps Bitcoin block attestation
REKOR_INDEX_RE = re.compile(r"index:?\s*(\d+)", re.I)
TIMEOUT = 300
KEY = pathlib.Path("~/Private/audit-evidence/cosign.key").expanduser()
PUB = ROOT / OUT / "cosign.pub"


# --- the evidence set and SUMS files ---------------------------------------------------------

def git(*args, check=True):
    r = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True, timeout=600)
    if check and r.returncode:
        sys.exit(f"git {' '.join(args[:2])} failed: {r.stderr.strip()}")
    return r.stdout


def evidence_files():
    """Paths (relative to the repo root) of every non-ignored file under the evidence directories."""
    dirs = [d for d in EVIDENCE_DIRS if (ROOT / d).is_dir()]
    out = git("ls-files", "--cached", "--others", "--exclude-standard", "-z", "--", *dirs)
    return sorted(p for p in out.split("\0") if p and (ROOT / p).is_file())


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def sums_name(version):
    return "SHA256SUMS.txt" if version == 1 else f"SHA256SUMS.v{version}.txt"


def sums_version(name):
    m = SUMS_NAME_RE.match(name)
    return None if m is None else int(m.group(1) or 1)


def existing_versions():
    """Every SUMS version in timestamps/ now, or ever added there in the repository's history."""
    found = {v for p in (ROOT / OUT).glob("SHA256SUMS*.txt") if (v := sums_version(p.name))}
    for line in git("log", "--all", "--format=", "--name-only", "--", OUT, check=False).splitlines():
        p = pathlib.PurePosixPath(line.strip())
        if str(p.parent) == OUT and (v := sums_version(p.name)):
            found.add(v)
    return found


def render_sums(files, version, moment, note):
    head = git("rev-parse", "HEAD", check=False).strip() or "none"
    dirty = " (plus uncommitted files)" if git("status", "--porcelain", "--", *EVIDENCE_DIRS, check=False).strip() else ""
    lines = [
        "# SHA-256 digests of the evidence held in github.com/nealmcb/audit-results, written by scripts/stamp.py.",
        f"# version: {version}",
        f"# time: {moment.strftime('%Y-%m-%dT%H:%M:%SZ')}",
        f"# repository-head: {head}{dirty}",
        f"# files: {len(files)}",
    ]
    if note:
        lines.append(f"# note: {' '.join(note.split())}")
    lines.append(f"# check (from the repository root): sha256sum --check --ignore-missing {OUT}/{sums_name(version)}")
    for path in files:
        if "\n" in path or "\\" in path:
            sys.exit(f"unsafe path {path!r}")
        lines.append(f"{sha256_file(ROOT / path)}  {path}")
    return ("\n".join(lines) + "\n").encode()


def parse_sums(text):
    entries, malformed = [], []
    for line in text.splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        m = SUMS_LINE_RE.match(line)
        (entries.append((m.group(1), m.group(2))) if m else malformed.append(line[:200]))
    return entries, malformed


# --- the proofs ----------------------------------------------------------------------------

def run_tool(argv, cwd, interactive=False, env=None):
    """Run a tool, showing its output as it comes (a cosign login URL must be seen); return (code, output)."""
    try:
        p = subprocess.Popen(argv, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
                             errors="replace", stdin=None if interactive else subprocess.DEVNULL,
                             env=None if env is None else {**os.environ, **env})
    except OSError as e:
        return 1, str(e)
    out = []
    for line in p.stdout:
        out.append(line)
        print("    " + line.rstrip())
    try:
        return p.wait(timeout=TIMEOUT), "".join(out)
    except subprocess.TimeoutExpired:
        p.kill()
        return None, "".join(out)


def short(text):
    text = text.strip()
    return text if len(text) <= 400 else "..." + text[-400:]


def stamp_ots(path):
    ots = shutil.which("ots")
    if not ots:
        return "SKIPPED", "the ots command (pip install opentimestamps-client) is not installed"
    code, out = run_tool([ots, "stamp", path.name], path.parent)
    proof = path.with_name(path.name + ".ots")
    if code == 0 and proof.is_file():
        if OTS_BITCOIN_TAG in proof.read_bytes():
            return "DONE", "complete"
        return "PENDING", "submitted to the calendars; run `stamp.py upgrade` after an hour or two"
    return "FAILED", f"ots stamp {'timed out' if code is None else f'exit {code}'}: {short(out)}"


def sign_cosign(path, keyless=False):
    """Sign ``path`` with cosign: with the repository's key file, or keyless (an OIDC login)."""
    cosign = shutil.which("cosign")
    if not cosign:
        return "SKIPPED", "the cosign command is not installed"
    if keyless:
        bundle, mode, extra, env = path.with_name(path.name + ".keyless.cosign-bundle"), "keyless", [], None
    else:
        if not KEY.is_file():
            return "SKIPPED", f"no key file at {KEY}"
        bundle, mode = path.with_name(path.name + ".cosign-bundle"), "with the repository's key"
        extra, env = ["--key", str(KEY)], {"COSIGN_PASSWORD": ""}
    if bundle.exists():
        return "SKIPPED", f"{bundle.name} already exists"
    code, out = run_tool([cosign, "sign-blob", "--yes", "--bundle", bundle.name, *extra, path.name],
                         path.parent, interactive=keyless, env=env)
    if code == 0 and bundle.is_file() and bundle.stat().st_size:
        m = REKOR_INDEX_RE.search(out)
        return "DONE", f"signed {mode}" + (f"; Rekor log index {m.group(1)}" if m else "")
    bundle.unlink(missing_ok=True)
    return "FAILED", f"cosign sign-blob {mode} {'timed out' if code is None else f'exit {code}'}: {short(out)}"


# --- commands ------------------------------------------------------------------------------

def cmd_stamp(a):
    files = evidence_files()
    if not files:
        sys.exit("no evidence files found")
    out = ROOT / OUT
    out.mkdir(exist_ok=True)
    version = max(existing_versions(), default=0) + 1
    path = out / sums_name(version)
    moment = datetime.datetime.now(datetime.timezone.utc)
    with open(path, "xb") as f:  # exclusive: never overwrite a commitment
        f.write(render_sums(files, version, moment, a.note))
    print(f"wrote {path.relative_to(ROOT)}: {len(files)} files, sha256 {sha256_file(path)}")
    steps = [("opentimestamps", *stamp_ots(path))]
    steps.append(("sigstore key", *(("SKIPPED", "--no-key given") if a.no_key else sign_cosign(path))))
    if a.keyless:
        steps.append(("sigstore keyless", *sign_cosign(path, keyless=True)))
    for name, status, detail in steps:
        print(f"{status:8} {name}: {detail}")
    print(f"Commit {OUT}/ (the SUMS file and its proofs) to publish the commitment.")
    return 1 if any(s == "FAILED" for _, s, _ in steps) else 0


def latest_sums():
    return max((ROOT / OUT).glob("SHA256SUMS*.txt"), key=lambda p: sums_version(p.name) or 0)


def cmd_sign(a):
    path = pathlib.Path(a.sums).resolve() if a.sums else latest_sums()
    status, detail = sign_cosign(path, keyless=a.keyless)
    print(f"{status:8} sigstore {'keyless' if a.keyless else 'key'} {path.name}: {detail}")
    return 1 if status == "FAILED" else 0


def cmd_upgrade(a):
    ots = shutil.which("ots")
    if not ots:
        sys.exit("the ots command is not installed")
    rc = 0
    for proof in sorted((ROOT / OUT).glob("*.ots")):
        if OTS_BITCOIN_TAG in proof.read_bytes() and not a.all:
            continue
        code, out = run_tool([ots, "upgrade", proof.name], proof.parent)
        done = OTS_BITCOIN_TAG in proof.read_bytes()
        print(f"{'DONE' if done else 'PENDING' if code in (0, 1) else 'FAILED':8} {proof.relative_to(ROOT)}")
        if code not in (0, 1):
            rc = 1
    return rc


def cmd_verify(a):
    sums = pathlib.Path(a.sums).resolve() if a.sums else latest_sums()
    entries, malformed = parse_sums(sums.read_text())
    counts = {"OK": 0, "MISMATCH": 0, "MISSING": 0}
    for digest, rel in entries:
        p = pathlib.PurePosixPath(rel)
        if p.is_absolute() or ".." in p.parts:
            print(f"REFUSED  {rel}")
            malformed.append(rel)
            continue
        f = ROOT / rel
        status = "MISSING" if not f.is_file() else "OK" if sha256_file(f) == digest else "MISMATCH"
        counts[status] += 1
        if status != "OK" or not a.quiet:
            print(f"{status:8} {rel}")
    print(f"files: {counts['OK']} OK, {counts['MISMATCH']} MISMATCH, {counts['MISSING']} MISSING"
          + (f", {len(malformed)} malformed lines" if malformed else ""))
    rc = 1 if counts["MISMATCH"] or malformed else 0
    proof = sums.with_name(sums.name + ".ots")
    if proof.is_file() and shutil.which("ots"):
        code, out = run_tool(["ots", "verify", proof.name], sums.parent)
        print(f"opentimestamps: {'OK' if code == 0 else 'PENDING or needs a Bitcoin node (see opentimestamps.org)'}")
    for suffix, keyless in ((".cosign-bundle", False), (".keyless.cosign-bundle", True)):
        bundle = sums.with_name(sums.name + suffix)
        if not (bundle.is_file() and shutil.which("cosign")):
            continue
        argv = ["cosign", "verify-blob", "--bundle", bundle.name]
        if not keyless:
            argv += ["--key", str(PUB)]
        elif a.certificate_identity:
            argv += ["--certificate-identity", a.certificate_identity,
                     "--certificate-oidc-issuer", a.certificate_oidc_issuer]
        else:
            argv += ["--certificate-identity-regexp", ".*", "--certificate-oidc-issuer-regexp", ".*"]
            print("sigstore keyless: no expected identity given, so the signer is not checked")
        code, _ = run_tool(argv + [sums.name], sums.parent)
        print(f"sigstore {'keyless' if keyless else 'key'}: {'OK' if code == 0 else 'FAILED'}")
        rc |= code != 0
    return rc


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("stamp", help="write a new SUMS file and timestamp it")
    s.add_argument("--keyless", action="store_true", help="also sign keyless with Sigstore (needs a login)")
    s.add_argument("--no-key", action="store_true", help="don't sign with the repository's key file")
    g = sub.add_parser("sign", help="sign an existing SUMS file (default: the latest)")
    g.add_argument("sums", nargs="?")
    g.add_argument("--keyless", action="store_true", help="keyless (needs a login) instead of the key file")
    s.add_argument("--note", help="a line for the SUMS header, e.g. what event this precedes")
    u = sub.add_parser("upgrade", help="fetch completed OpenTimestamps proofs")
    u.add_argument("--all", action="store_true", help="re-run on proofs that are already complete")
    v = sub.add_parser("verify", help="check a SUMS file's hashes and proofs (default: the latest)")
    v.add_argument("sums", nargs="?")
    v.add_argument("--certificate-identity")
    v.add_argument("--certificate-oidc-issuer", default="https://github.com/login/oauth")
    v.add_argument("--quiet", action="store_true", help="list only files that are not OK")
    a = ap.parse_args()
    sys.exit({"stamp": cmd_stamp, "sign": cmd_sign, "upgrade": cmd_upgrade, "verify": cmd_verify}[a.cmd](a))


if __name__ == "__main__":
    main()
