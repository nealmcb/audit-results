#!/usr/bin/env python3
"""List Colorado contests close enough to trigger a mandatory recount.

Purpose (2026-11-20): Neal asked which recounts to expect after the November 3, 2026 general
election, since a recount delays the end of the records-act stay on ballots and CVRs (C.R.S.
24-72-205.5) and the CVR redaction deadline (Election Rule 25.2.4). Under C.R.S. 1-10.5-101(1)(b) a
recount is held if the difference between the highest and next highest vote in a contest is at most
one-half of one percent of the highest vote; with several seats, the difference between the
lowest-voted winner and the highest-voted loser is compared with 0.5% of the lowest-voted winner's
votes. A recount happens only after the canvass board certifies the original count, and interested
parties may also request one at their own expense (1-10.5-106).

Inputs are the Secretary of State's Audit Center files: the candidate vote totals summary
(tabulatePlurality.csv: contest_name, choice, votes) and a round contest list (contest.csv, for
winners_allowed). They come from the counties' uploads for the audit, before the canvass, so the
final certified totals may differ slightly; contests near the line are worth rechecking then.

    python3 -I scripts/co_recounts.py TABULATE_PLURALITY.csv CONTEST.csv [--near 0.01]
"""
import argparse
import csv
from collections import defaultdict


def contests(tabulate_csv, contest_csv):
    """Yield (contest, seats, sorted [(votes, choice)]) for every contest."""
    seats = {}
    with open(contest_csv, encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            seats[r["contest_name"]] = int(r.get("winners_allowed") or 1)
    votes = defaultdict(list)
    with open(tabulate_csv, encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            votes[r["contest_name"]].append((int(r["votes"] or 0), r["choice"]))
    for name, vs in votes.items():
        yield name, seats.get(name, 1), sorted(vs, reverse=True)


def closeness(seats, vs):
    """(difference, base, ratio): the recount test's difference, the vote it is compared with, and
    their ratio; None when there is no losing choice to compare with."""
    if len(vs) <= seats:
        return None
    winner, loser = vs[seats - 1][0], vs[seats][0]
    base = winner if seats > 1 else vs[0][0]
    if base == 0:
        return None
    return winner - loser, base, (winner - loser) / base


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("tabulate_csv")
    ap.add_argument("contest_csv")
    ap.add_argument("--near", type=float, default=0.01, help="also list contests within this ratio")
    a = ap.parse_args()
    rows = []
    for name, seats, vs in contests(a.tabulate_csv, a.contest_csv):
        c = closeness(seats, vs)
        if c and c[2] <= a.near:
            rows.append((c[2], name, seats, c[0], c[1], vs[seats - 1], vs[seats]))
    for ratio, name, seats, diff, base, w, l in sorted(rows):
        tag = "RECOUNT" if ratio <= 0.005 else "near"
        print(f"{tag:7} {ratio:7.3%}  diff {diff:>6,} of {base:>9,}  {name}"
              f"{f' ({seats} seats)' if seats > 1 else ''}: {w[1]} {w[0]:,} vs {l[1]} {l[0]:,}")


if __name__ == "__main__":
    main()
