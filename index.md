---
layout: home
title: Audit Results 2026
---

# Post-election audits of the November 3, 2026 general election

**A provisional proposal, started 2026-11-10.** Many dates are computed from statute and not
yet confirmed, and errors are likely. See the
[README](https://github.com/nealmcb/audit-results#readme) for what this is, who it is for and
how to help.

This site tracks the audits that states run after the November 3, 2026 US general election: when
they happen, what each state published before its random selection, the audit data as it
appears, and what still needs doing by people who can make a phone call, file a records request
or watch an audit in person.

- **[Calendar](calendar.md)**: audit dates for all 50 states and DC, each marked official,
  computed from statute, news, precedent or unverified, with its source.
- **[States](states/index.md)**: one page per state, with its dates and the pages we watch.
- **[Captures](captures.md)**: timestamped, hashed copies of state audit pages, taken every 30
  minutes, so anyone can see what was public before each random draw.
- **[News](news.md)**: articles and official posts about the 2026 audits, tagged by state.
- **[Help wanted](help-wanted.md)**: confirmations, records requests and observations that need
  a person.

## Why capture before the draw?

A risk-limiting audit compares a random sample of paper ballots with the machine count. Its
evidence is strongest when the ballot manifests, the vote records it checks against and the list
of audited contests are fixed in public before the random seed is drawn. Then nobody can adjust
them after learning which ballots will be checked. Few states publish these in advance. Some,
like Georgia, post cryptographic hashes after the draw but before the hand count. These captures
record what each state had published, and when.

## Related work

- [Citizen Election Verification](https://sites.google.com/view/auditenhancement): how
  citizen verifiers in Colorado obtain and timestamp the audit's evidence before the random draw
  and check the audit as it happens. A model of what can be achieved.
- [Reviews of Georgia's Arlo audits](https://nealmcb.github.io/rla-review-arlo/): hash
  commitments, sample reproduction and discrepancy analysis.
- [auditAnation](https://auditanation.org/): Tom Ryan's comparison of the 2024 audits in all
  50 states and DC.
- [Verified Voting audit law database](https://verifiedvoting.org/auditlaw/).
