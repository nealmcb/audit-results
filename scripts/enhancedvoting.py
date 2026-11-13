#!/usr/bin/env python3
"""Fetch contest results and ballots cast from an Enhanced Voting public results site.

Purpose (2026-11-13): many counties (in Washington, at least Kitsap and Thurston) publish results
through app.enhancedvoting.com, whose pages are built by JavaScript. Its JSON API is public:

    https://app.enhancedvoting.com/results/public/api/elections/<jurisdiction>/<election>/ballot-items
    https://app.enhancedvoting.com/results/public/api/elections/<jurisdiction>/<election>/turnout

where <jurisdiction> is a slug such as thurston-county-wa and <election> is YYYYMMDD. This prints the
contests matching a pattern, with each choice's votes, the margin between the top two, the
county's total ballots cast (the sum over precincts, when the county publishes them), and the
initial sample size a ballot-comparison RLA would need at the given risk limit (see
rla_sample_size.py), over two denominators: all the county's ballots, or only the contest's.

Usage:
    python3 -I scripts/enhancedvoting.py thurston-county-wa 20261103 --match 'sheriff' [--risk-limit 0.05]
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rla_sample_size import initial_sample_size  # noqa: E402

API = "https://app.enhancedvoting.com/results/public/api/elections"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36"


def get(url):
    r = subprocess.run(["curl", "-sS", "-L", "--max-time", "60", "-A", UA, url], capture_output=True, check=True)
    return json.loads(r.stdout)


def paged(url, limit=500):
    """All records from an endpoint that pages with limit/offset/totalRecordCount."""
    out, offset = [], 0
    while True:
        sep = "&" if "?" in url else "?"
        d = get(f"{url}{sep}limit={limit}&offset={offset}")
        out += d["data"]
        offset += len(d["data"])
        if not d["data"] or offset >= d.get("totalRecordCount", 0):
            return out


def text(field):
    return " ".join(x["text"] for x in field or [] if x.get("text"))


def contests(jurisdiction, election):
    return paged(f"{API}/{jurisdiction}/{election}/ballot-items")


def ballots_cast(jurisdiction, election):
    return int(sum(p.get("ballotsCast") or 0 for p in paged(f"{API}/{jurisdiction}/{election}/turnout")))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("jurisdiction")
    ap.add_argument("election")
    ap.add_argument("--match", default=".", help="regex for contest names (case-insensitive)")
    ap.add_argument("--risk-limit", type=float, default=0.05)
    a = ap.parse_args()
    cast = ballots_cast(a.jurisdiction, a.election)
    print(f"{a.jurisdiction} {a.election}: {cast:,} ballots cast")
    for c in contests(a.jurisdiction, a.election):
        name = text(c.get("name"))
        if not re.search(a.match, name, re.I):
            continue
        opts = sorted(((o.get("voteCount") or 0, text(o.get("name"))) for o in (c.get("summaryResults") or {}).get("ballotOptions", [])), reverse=True)
        asof = (c.get("reportingStatus") or {}).get("asOf", "")
        print(f"\n{name} (as of {asof})")
        for v, n in opts:
            print(f"  {v:>9,}  {n}")
        if len(opts) < 2 or opts[1][0] == 0:
            print("  uncontested or only one choice with votes: nothing for an audit to check")
            continue
        margin = opts[0][0] - opts[1][0]
        votes = sum(v for v, _ in opts)
        # The denominator depends on the audit's setup: all ballots in the county's manifest (a
        # larger sample), or only ballots carrying the contest, approximated here by its votes
        # (a smaller one). Show both; the truth lies between unless the setup is known.
        print(f"  margin {margin:,}")
        for label, d in (("all ballots cast in the county", cast), ("votes in the contest (a lower bound on its ballots)", votes)):
            if d:
                n, mu = initial_sample_size(margin, d, a.risk_limit)
                print(f"  over {label}, {d:,}: diluted margin {mu:.4f}, about {n} ballots at {a.risk_limit:.0%}")


if __name__ == "__main__":
    main()
