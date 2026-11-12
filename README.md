# audit-results

Tracking the post-election audits of the November 3, 2026 US general election: when each state
audits, what it published before its random draw, the audit data as it appears, and the calls,
records requests and observations that need a person.

**Site:** https://nealmcb.github.io/audit-results/

## Status: a proposal

This is a working proposal, started 2026-11-10, not a finished resource. The goal is a shared,
open record of the 2026 audits that people across the audit community can build together:
volunteers in groups such as the State Audit Working Group, Verified Voting, the League of Women
Voters and Common Cause, and the authors of related projects such as
[auditAnation](https://auditanation.org/). How it is organized, what it covers and who maintains
it are all open questions. Suggestions are as welcome as corrections.

What exists so far:

- **A calendar** of audit dates for all 50 states and DC, many of them computed from statute and
  still to be confirmed.
- **Captures** of about 30 state and county audit pages every 30 minutes, keeping a timestamped,
  hashed copy whenever a page changes.
- **A page per state**, generated from the calendar and the captures.
- **A help-wanted list.**

Planned:

- The 2026 audit data itself as states publish it: manifests, cast vote records, batch tallies,
  seeds, samples and results. Where possible, samples will be reproduced and hash commitments
  verified.
- Draft public-records requests for audit data that is not published.
- Call lists for confirming dates with election offices.
- Reviews of individual audits, like the existing
  [reviews of Georgia's Arlo audits](https://nealmcb.github.io/rla-review-arlo/).

## Why capture before the draw

A risk-limiting audit compares a random sample of paper ballots with the machine count. Its
evidence is strongest when the ballot manifests, the vote records it checks against and the list
of audited contests are fixed in public before the random seed is drawn. Then nobody can adjust
them after learning which ballots will be checked. Few states publish these in advance. The
captures here, and the git history that timestamps them, record what each state had published
and when.

## How it works

| Path | What it is |
|---|---|
| `calendar-source.md` | The master calendar, edited by hand. Each row says whether its date is official, computed, from the news, from precedent or unverified, and gives a source |
| `state-notes/<XX>.md` | Hand-written notes that appear at the top of a state's page |
| `watchlist.json` | The pages to capture, with state and reason |
| `scripts/capture.py` | Fetches every watched page and saves a copy under `captures/<slug>/` when its content changes. Every fetch is logged in `captures/log.jsonl` (UTC time, HTTP status, sha256, whether it was blocked) |
| `scripts/build_site.py` | Generates `calendar.md`, `states/` and `captures.md` from the files above |
| `help-wanted.md` | Tasks that need a person |
| `evidence/` | Files obtained other ways (a browser save, a Cowork download), with their sources in `evidence/SOURCES.md` |
| `scripts/stamp.py`, `timestamps/` | Commitments: a versioned `SHA256SUMS` file listing the hash of every file in `captures/` and `evidence/`, timestamped with OpenTimestamps (Bitcoin) and signed with the repository's cosign key (public key: `timestamps/cosign.pub`), which records each signature in Sigstore's public Rekor log. Anyone can check them with `sha256sum --check --ignore-missing`, `ots verify` and `cosign verify-blob --key timestamps/cosign.pub` |

To capture and rebuild:

```
python3 -I scripts/capture.py
python3 -I scripts/build_site.py
```

`capture.py --loop 1800 --until 2026-11-22T00:00Z` repeats every 30 minutes.

Some state sites refuse automated fetches. Copies of those come from a browser instead: a person
saving the page, or a browser-driving agent such as Claude Cowork or Claude in Chrome. Agents with
first-party access to a platform can reach what scripts cannot: Grok reads posts on X directly,
and Gemini can watch YouTube videos, such as recordings of dice-roll ceremonies. Log entries for
copies made this way say how in a `via` field.

## Contributing

Open an [issue](https://github.com/nealmcb/audit-results/issues) or send a pull request. The
most useful contributions right now:

- confirmed dates, with who said so and when
- browser-saved copies of pages that block automated fetches, with the time you saved them
- notes from audits you observed
- pages that should be on the watchlist

Please give a source for every fact. Edit `calendar-source.md`, `state-notes/` or
`watchlist.json` rather than the generated pages.

Much of the research and code here was done with Claude (Anthropic's AI, through Claude Code),
directed and reviewed by Neal McBurnett. Errors are likely; please report them.
