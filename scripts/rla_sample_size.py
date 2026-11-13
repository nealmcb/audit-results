#!/usr/bin/env python3
"""Estimate the initial sample size of a ballot-comparison risk-limiting audit.

Purpose (2026-11-13): states such as Washington run ballot-comparison RLAs in Arlo but don't publish
the expected sample sizes ahead of the audit. This gives the standard estimate, so observers know
roughly how many ballots to expect: with no discrepancies, the Kaplan-Markov bound with error
inflation gamma reaches risk limit alpha after

    n = ceil(-2 * gamma * ln(alpha) / mu)

ballots, where mu is the diluted margin: (winner's votes - runner-up's votes) / ballots cast in the
audit's jurisdiction (all ballot cards there, not just those voting in the contest). Arlo and
ColoradoRLA use gamma = 1.03905. Discrepancies, multi-card ballots and Arlo's own rounding or
round-size choices make real samples larger; treat this as a floor.

Usage:
    python3 -I scripts/rla_sample_size.py --margin 764087 --ballots 3000000 --risk-limit 0.05
"""
import argparse
import math

GAMMA = 1.03905


def initial_sample_size(margin, ballots, risk_limit, gamma=GAMMA):
    """Ballots needed if none of them shows a discrepancy."""
    if margin <= 0:
        raise ValueError("margin must be positive")
    mu = margin / ballots
    return math.ceil(-2 * gamma * math.log(risk_limit) / mu), mu


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--margin", type=int, required=True, help="winner's votes minus runner-up's")
    ap.add_argument("--ballots", type=int, required=True, help="ballots cast in the audit's jurisdiction")
    ap.add_argument("--risk-limit", type=float, default=0.05)
    ap.add_argument("--gamma", type=float, default=GAMMA)
    a = ap.parse_args()
    n, mu = initial_sample_size(a.margin, a.ballots, a.risk_limit, a.gamma)
    print(f"diluted margin {mu:.4f}: about {n} ballots at a {a.risk_limit:.0%} risk limit, with no discrepancies")


if __name__ == "__main__":
    main()
