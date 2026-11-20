---
layout: default
title: Georgia
---


# Georgia

[← All states](index.md) · [Calendar](../calendar.md) · [Captures](../captures.md)

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

The files themselves are to be published when the audit completes, so that anyone can check them
against these hashes, and the hand counts against the batch totals. That is a commitment few states
make. (The posting times come from the posts' status IDs; the thread is kept in `evidence/GA/`.)

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

Wanted: the seed, how the Commissioner of Agriculture was drawn, and copies of the manifests and
batch totals once they are published.

## 2026 audit dates

### Watch now (Nov 10–24)

- **Thu Nov 12**: SOS RLA kickoff and public dice roll, 10 am ET (15:00 UTC), South Steps of the State Capitol, Atlanta; open to the public and the media. · _official ([@GaSecofState on X, Nov 12](https://x.com/GaSecofState/status/2120922270394982432), posting the manifest and batch-total hashes); time and place from [92.1 WLHR, Nov 12](https://921wlhr.com/secretary-of-state-kicks-off-risk-limiting-audit-with-dice-roll-today/); Richmond County elections staff told its board on Nov 6 that "the dice roll to select batches will take place Thursday, Nov. 12 at 10 a.m.", as summarized by [Citizen Portal](https://citizenportal.ai/articles/11902431/georgia/richmond-county/augusta-city/richmond-county-sets-risk-limiting-audit-dice-roll-nov-12-audits-start-nov-1) (an AI summary of the meeting video, at 36:57)_. First statewide RLA under SB 3EX, with 20 contests: governor, lieutenant governor, attorney general, secretary of state, U.S. Senate, all 14 congressional seats, and one more state office chosen at random ("They'll be drawing that out of the hat," Raffensperger told [WSB-TV, Oct 22](https://www.wsbtv.com/news/local/georgias-secretary-state-touts-vote-audits-ahead-midterms-we-audit-fool-out-it/UCIRZFQHSFGKXBJ3UJS3H5QAHI/)); how and when that draw is made is not announced. @GaSecofState posted SHA-256 hashes of the ballot manifests (d731216443e415c9…) and the machine-counted batch totals (419a77b32fd393e9…) at 16:50:48 and 16:51:24 UTC ([thread](https://x.com/GaSecofState/status/2120922270394982432)), about 1 hour 50 minutes after the roll began; in 2025 and May 2026 they came 8–54 min after it. The files themselves are to be published when the audit completes. The batch retrieval list (601 batches in 159 counties, prepared by VotingWorks; PDF created 12:28 pm ET) shows the office drawn at random was the Commissioner of Agriculture. The seed itself has not been found yet
- **Thu Nov 12**: Gwinnett County RLA and ballot image audit start, 12:00 pm ET (17:00 UTC), 455 Grayson Hwy, Lawrenceville; deadline Wed Nov 18, 5 pm ET (22:00 UTC). · _official ([Gwinnett notice](https://www.gwinnettcounty.com/documents/d/gwinnett-county/notice-november-3-general-special-election-risk-limiting-ballot-image-audit?download=true))_. A noon county start supports a state kickoff that morning. Gwinnett's deadline is a day later than Fulton's
- **Thu Nov 12**: Clayton County RLA starts, 12:00 pm ET (17:00 UTC), South Clayton Recreation Center, 1837 McDonough Rd, Hampton; continues day to day, open to the public. · _official ([Clayton notice](https://www.claytoncountyga.gov/news/risk-limiting-audit-november-3-2026-general-election/))_. The county's event listing says Nov 11; its notice says Nov 12. Its site blocks scripts, so a browser save is wanted
- **Thu Nov 12**: Forsyth County RLA starts, 1:00 pm ET (18:00 UTC), 1201 Sawnee Dr, Cumming; deadline Wed Nov 18, 5 pm ET (22:00 UTC); open to the public. · _official ([Forsyth notice](https://forsythco.b-cdn.net/app/uploads/2026/11/Public-Notice-of-RLA-11-03-26-General-General-Election-Special-Elections-UA-1.pdf))_. Results posted Nov 17: Nov 12–13, 10 state-selected batches, 2,606 ballots (one batch of 1,124 for U.S. House District 7, nine of 1,482 for U.S. Senate), plus a provisional batch of 39 the county board added; the hand counts equal the machine totals in every batch, and the audit board tally sheets are posted ([results notice](https://forsythco.b-cdn.net/app/uploads/2026/11/Public-Notice-of-Audit-Results-11-17-2026-with-links-UA-rev.pdf), [batch totals](https://www.forsythco.com/app/uploads/2026/11/11-13-2026-RLA-Totals-of-11-03-26-General-Election-and-Special-Elections.pdf), [tally sheets](https://www.forsythco.com/app/uploads/2026/11/11-03-26-RLA.-SOS-selected-Batches-Tally-Sheets.pdf))
- **Fri Nov 13**: County hand counts begin (Fulton: 10 am ET (15:00 UTC), Union City); deadline Tue Nov 17, 5 pm. ET (22:00 UTC) Cobb audits on Nov 13, 16 and 17, and also runs an "Enhanced Audit" that reviews ballot images with independent software. · _official (Fulton, Crawford; [Cobb](https://www.cobbcounty.gov/news/cobb-county-certifies-results-november-3-general-electionspecial-election))_. Fulton's notice says "Thursday, November 13"; Nov 13 is a Friday; Cobb finished Nov 17: 21 state-selected batches (11 advance voting, 9 Election Day, 1 absentee) covering nine contests, 145,244 ballots hand counted by 23 two-person teams, and 339,277 ballot images reviewed; both audits met the state's standard ([Cobb release, Nov 17](https://www.cobbcounty.gov/news/cobb-county-post-election-audits-verify-november-3-election-results))
- **Thu Nov 19**: RLAs complete: Crawford County's notice of Nov 19 says the risk-limiting audits have been completed, confirming the reported outcomes of all audited contests, and points to the Secretary of State's release, "Historic number of risk-limiting audits confirm election outcomes". · _official ([Crawford County notice](https://www.crawfordcountyga.org/notice-risk-limiting-audit-results/); [SOS release](https://sos.ga.gov/news/historic-number-risk-limiting-audits-confirm-election-outcomes))_. The release's page refuses scripts; a browser copy is wanted
- **Fri Nov 13**: Richmond County (Augusta) RLA starts, 9:00 am ET (14:00 UTC), Board of Elections Warehouse, 2029 Lumpkin Rd; observers allowed but may not view ballots. · _official ([Augusta, Nov 5](https://www.augustaga.gov/m/newsflash/Home/Detail/4291))_.

### Full calendar, Nov 10 – Jan 2027

- **Nov 12**: SOS RLA kickoff and dice roll, 10 am ET (15:00 UTC), South Steps of the State Capitol. · _official_. <https://x.com/GaSecofState/status/2120922270394982432>
- **Nov 13**: County hand counts begin; deadline Nov 17, 5 pm ET (22:00 UTC). · _official_. <https://www.fultoncountyga.gov/-/media/November-3-Election-notices/Notice-of-Risk-Limiting-Audit--1132026.pdf>
- **Nov 17**: County audit deadline, 5 pm ET (22:00 UTC). · _official (Fulton)_. <https://www.fultoncountyga.gov/-/media/November-3-Election-notices/Notice-of-Risk-Limiting-Audit--1132026.pdf>

_Not yet confirmed by an official source:_

- about Nov 20: State certification. · _unverified_. —

## Watched pages

- <https://sos.ga.gov/page/elections-audit-information> (RLA artifacts, hashes; kickoff expected Nov 12; blocked to scripts; 1 saved copy)
- <https://sos.ga.gov/news> (RLA kickoff media advisory and results release; blocked to scripts; 1 saved copy)
- <https://www.fultoncountyga.gov/-/media/November-3-Election-notices/Notice-of-Risk-Limiting-Audit--1132026.pdf> (county count Nov 13-17; fetched regularly; 1 saved copy)
- <https://www.crawfordcountyga.org/notice-risk-limiting-audit-4/> (county count Nov 13; fetched regularly; 5 saved copies)
- <https://www.gwinnettcounty.com/documents/d/gwinnett-county/notice-november-3-general-special-election-risk-limiting-ballot-image-audit?download=true> (county RLA notice: starts Nov 12, 12 pm; fetched regularly; 1 saved copy)
- <https://forsythco.b-cdn.net/app/uploads/2026/11/Public-Notice-of-RLA-11-03-26-General-General-Election-Special-Elections-UA-1.pdf> (county RLA notice: starts Nov 12, 1 pm; fetched regularly; 1 saved copy)
- <https://www.forsythco.com/government/departments/voter-registrations-elections/current-upcoming-elections/> (RLA results to be posted here; blocked to scripts; 3 saved copies)
- <https://www.augustaga.gov/m/newsflash/Home/Detail/4291> (county RLA notice: starts Nov 13, 9 am; fetched regularly; 3 saved copies)
- <https://www.cobbcounty.gov/news/cobb-county-certifies-results-november-3-general-electionspecial-election> (audits Nov 13, 16, 17; enhanced ballot-image audit; fetched regularly; 1 saved copy)
- <https://www.claytoncountyga.gov/news/risk-limiting-audit-november-3-2026-general-election/> (county RLA notice: starts Nov 12, 12 pm (site may block scripts); blocked to scripts; 0 saved copies)
- <https://forsythco.b-cdn.net/app/uploads/2026/11/Public-Notice-of-Audit-Results-11-17-2026-with-links-UA-rev.pdf> (RLA results notice, posted Nov 17; fetched regularly; 1 saved copy)
- <https://www.forsythco.com/app/uploads/2026/11/11-13-2026-RLA-Totals-of-11-03-26-General-Election-and-Special-Elections.pdf> (breakdown of RLA hand-count results; blocked to scripts; 1 saved copy)
- <https://www.forsythco.com/app/uploads/2026/11/11-03-26-RLA.-SOS-selected-Batches-Tally-Sheets.pdf> (audit board tally sheets, SOS-selected batches; blocked to scripts; 1 saved copy)
- <https://www.forsythco.com/app/uploads/2026/11/11-03-26-RLA-BRE-selected-Batch-Tally-Sheet-1.pdf> (audit board tally sheet, batch chosen by the county board; blocked to scripts; 1 saved copy)
- <https://www.cobbcounty.gov/news/cobb-county-post-election-audits-verify-november-3-election-results> (Cobb County release: RLA and ballot image audit results; fetched regularly; 1 saved copy)
- <https://www.crawfordcountyga.org/notice-risk-limiting-audit-results/> (Crawford County notice: RLAs complete Nov 19; fetched regularly; 1 saved copy)
- <https://sos.ga.gov/news/historic-number-risk-limiting-audits-confirm-election-outcomes> (SOS release: RLAs confirm outcomes (refuses scripts); blocked to scripts; 0 saved copies)

## In the news

Articles and posts from the site's [news log](../news.md), newest first. They are leads, not evidence: the dates above rest on official sources where we have them.

- 2026-11-18 · Cobb County Government: [Cobb County Post-Election Audits Verify November 3 Election Results](https://www.cobbcounty.gov/news/cobb-county-post-election-audits-verify-november-3-election-results)
- 2026-11-14 · YouTube: [Secretary of State's Office to perform 20 risk audits following election -](https://www.youtube.com/watch?v=3Xre_qB3wwo)
- 2026-11-14 · audits - YouTube: [Georgia election 2026: Secretary of State's Office runs record number of](https://www.youtube.com/watch?v=hvvA42n25TE)
- 2026-11-14 · audits - WSB-TV: [Georgia election 2026: Secretary of State's Office runs record number of](https://www.wsbtv.com/news/local/georgia-election-2026-secretary-states-office-runs-record-number-audits/CKIDV7DOEFEOXFLHFCZJKUJZ5U/)
- 2026-11-14 · Atlanta News First: [Georgia election officials to audit midterm results - Atlanta News First](https://www.cbs46.com/2026/11/12/georgia-election-officials-audit-midterm-results/)
- 2026-11-12 · 92.1 WLHR: [Secretary of State Kicks Off Risk-Limiting Audit With Dice Roll Today](https://921wlhr.com/secretary-of-state-kicks-off-risk-limiting-audit-with-dice-roll-today/)
- 2026-11-12 · Atlanta News First (via WCTV): [Georgia election officials to audit midterm results](https://www.wctv.tv/2026/11/12/georgia-election-officials-audit-midterm-results/)
- 2026-11-12 · @GaSecofState on X: [Georgia Secretary of State posts hashes of ballot manifests and machine-counted batch totals](https://x.com/GaSecofState/status/2120922270394982432)
- 2026-11-11 · Election: [Cobb County Certifies Results of November 3 General Election/Special](https://www.cobbcounty.gov/news/cobb-county-certifies-results-november-3-general-electionspecial-election)
- 2026-11-11 · Gwinnett County Board of Voter Registrations and Elections: [Notice of Risk Limiting and Ballot Image Audit, November 3, 2026 General Election & Special Election](https://www.gwinnettcounty.com/documents/d/gwinnett-county/notice-november-3-general-special-election-risk-limiting-ballot-image-audit?download=true)
- 2026-11-10 · WSB-TV: [Georgia's secretary of state touts vote audits ahead of midterms: 'We audit the fool out of it'](https://www.wsbtv.com/news/local/georgias-secretary-state-touts-vote-audits-ahead-midterms-we-audit-fool-out-it/UCIRZFQHSFGKXBJ3UJS3H5QAHI/)
- 2026-11-07 · Cobb County Government: [Unofficial vs. Official Election Results \| Cobb County Georgia](https://www.cobbcounty.gov/news/unofficial-vs-official-election-results)
- 2026-11-07 · 92.1 WLHR: [Franklin Board of Elections to Certify Elections Today](https://921wlhr.com/franklin-board-of-elections-to-certify-elections-today/)
- 2026-11-07 · Democracy Docket: [Georgia election chief probes 'unacceptable' tabulation delay that could flip key state House race](https://www.democracydocket.com/news-alerts/georgia-election-chief-probes-unacceptable-tabulation-delay-that-could-flip-key-state-house-race/)
- 2026-11-06 · Citizen Portal (AI summary of a Richmond County Board of Elections meeting): [Richmond County sets risk-limiting audit: dice roll Nov. 12, audits start Nov. 13](https://citizenportal.ai/articles/11902431/georgia/richmond-county/augusta-city/richmond-county-sets-risk-limiting-audit-dice-roll-nov-12-audits-start-nov-1)
- 2026-11-05 · WSB Radio: [Georgia breaks midterm voter turnout record with more than 4 million ballots cast](https://www.wsbradio.com/news/local/georgia-breaks-midterm-voter-turnout-record-with-more-than-4-million-ballots-cast/CWXO7AY5X5BLNGOL3JJQ4GZNEU/)
- 2026-11-05 · Yahoo: [Secretary of State Brad Raffensperger discusses what happens after Election Day](https://www.yahoo.com/news/videos/secretary-state-brad-raffensperger-discusses-065915572.html)

