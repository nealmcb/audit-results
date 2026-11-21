Georgia's risk-limiting audit of the November 3, 2026 general election covers 20 contests, which
the office says makes Georgia the first state to do more than two: governor, lieutenant governor,
attorney general, secretary of state, U.S. Senate, all 14 congressional seats, and one more state
office drawn at random. The
Secretary of State rolled the dice for the seed in public, at 10 am ET on November 12 on the south
steps of the State Capitol, and counties began their hand counts that afternoon and the next day.
The office also retallies the scanned images of every ballot, and its reconciliation of check-ins
against ballots counted caught 388 uncounted ballots in Seminole County, enough to change a State
House race.

The "first state" claim does not hold, though. Colorado has run statewide risk-limiting audits of
many contests for years. In the 2020 general election, for example, its audits targeted 60 real
contests at a 3% risk limit: 3 statewide (Presidential Electors, U.S. Senator and Proposition 114)
and 57 chosen county by county, such as county commissioners, ballot measures and State House and
Senate districts, each wholly within its county. Colorado reported the risk limit achieved for
every one. Its statewide audits since then have each targeted dozens of contests, and it checks
hundreds more opportunistically on the same ballots.

Colorado's own list for 2020 shows 66 targeted contests, because it also counts six counties' own
portions of statewide contests, each audited in that county alone, such as "Teller - Amendment 77
(CONSTITUTIONAL)". That is not an audit of the contest, so the count above leaves those out.
(Source: the Colorado Secretary of State's Audit Center
[`contest.csv` for round 3](https://github.com/nealmcb/auditcenter/blob/main/2020/general/round_3/contest.csv),
mirrored: the rows whose `audit_reason` is `state_wide_contest` or `county_wide_contest`, less the
county-only portions.)

## Hashes of the audit's inputs

At 16:50–16:51 UTC on November 12 the Secretary of State
[posted on X](https://x.com/GaSecofState/status/2120922270394982432) SHA-256 hashes of the ballot
manifests and of the machine-counted batch totals:

- ballot manifests: `d731216443e415c931882d07b051b8c927fbe650a93a0efa28a93d428160010e`
- machine-counted batch totals: `419a77b32fd393e951847b589969b7de3d8de0bfe40858830624fc18ced92211`

The office promised to publish the files themselves when the audit completed, and it did: with its
[November 19 release](https://sos.ga.gov/news/historic-number-risk-limiting-audits-confirm-election-outcomes)
it posted the ballot manifests and machine batch totals as zip files, and both match these hashes
byte for byte, so anyone can now check the hand counts against totals fixed before the audit. That
is a commitment few states make, and Georgia kept it. (The posting times come from the posts'
status IDs; the thread, the files and their hashes are in `evidence/GA/`.)

## Results

The audit is complete. Per the release and
[VotingWorks' report](https://mcusercontent.com/bb95d9c7cf4b94c9f44421f7c/files/ea7101ba-52d1-b834-4800-0b0495bf1b58/Georgia_2026_General_Election_Risk_Limiting_Audit_Report_Final_.pdf),
all 20 contests met the 5% risk limit and the reported outcomes were confirmed: 600 batches,
1,050,204 ballots and 1,539,171 vote opportunities, 99.98% of which matched the reported results.
The seed, rolled with 20 ten-sided dice on November 12, was 49999639609719737918, and Arlo's full
audit report lists every sampled batch with its reported and audited counts.

## Two adjustments that would make it stronger

**Post the hashes before the dice are rolled.** These came about 1 hour 50 minutes after the roll
began, when the seed, and so which batches would be checked, was already known. (In November 2025
and May 2026 they came 8 to 54 minutes after the roll.) A hash reveals nothing about the numbers,
so there is no cost to posting it earlier. Posted before the roll, it shows that the manifests and
totals could not have been adjusted once the sample was known. Posted after, it cannot show that,
and the gap invites the very doubts it is meant to dispel.

**Count blind, instead of keeping the totals secret.** The office held back the files themselves so
as not to give the hand counters a "number to hit". A better answer to that concern is to have two
teams count each batch, or each half of a split batch, publicly and independently, with no target
number. Then the machine totals could be published before the audit too, and everyone could follow
along as the counts come in.

The batch retrieval list, prepared by VotingWorks, sends 601 batches in all 159 counties to be hand
counted, and shows that the office drawn at random was the Commissioner of Agriculture. A copy is
in `evidence/GA/`.

Wanted: how the Commissioner of Agriculture was drawn as the randomly chosen contest.
