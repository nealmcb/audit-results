---
layout: default
title: Texas
---


# Texas

[← All states](index.md) · [Calendar](../calendar.md) · [Captures](../captures.md)

## Texas's first statewide risk-limiting audit: questions and answers

The November 3, 2026 general election is the first in which Texas runs a statewide risk-limiting
audit (RLA), as required by laws passed in 2021 (SB 1 and SB 598). These answers draw on the
Secretary of State's [November 16 release](https://www.sos.state.tx.us/about/newsreleases/2026/111626.shtml)
and the livestreamed seed meeting of November 18. Corrections are welcome.

### What is being audited?

The risk-limiting audit checks one contest: U.S. Senate. Separately, counties that count with
electronic equipment also do their usual post-election hand counts, which compare a sample of
hand-counted ballots with the machine totals for U.S. Senate, Chief Justice of the Supreme Court
and one local race each county chooses. Other contests on the ballot, such as Governor, are not
part of this year's risk-limiting audit.

### What does a risk-limiting audit check?

It checks that the reported winner of the audited contest is the one a full hand count of the paper
ballots would find. Randomly selected paper ballots are compared with the reported results, and the
audit keeps going until the evidence is strong enough, or until every ballot has been counted by
hand. A close contest needs more ballots than a wide one.

It does not check who was eligible to vote or the voter rolls. Those are covered by other checks,
including ballot accounting, which reconciles the ballots counted with the voters recorded as
voting.

### How were the ballots chosen?

On November 18 the Secretary of State rolled dice on a livestream to make a 20-digit random seed:
55781838668306731400. The audit software, Arlo, uses the seed to pick the ballots from each county's
ballot manifest, the list of how its paper ballots are stored. The same seed and the same manifests
always give the same selection, and a different seed gives a different one.

### Can anyone check the selection?

Yes, once the inputs are public. Arlo is open-source software from VotingWorks, a 501(c)(3)
nonprofit, and [its code](https://github.com/votingworks/arlo) is published, so anyone can see how it chooses ballots and measures risk. With the seed,
the ballot manifests and the list of ballots chosen, anyone can rerun the selection, or try another
seed and see that it picks different ballots.

### Can the public watch?

The seed meeting was livestreamed. The ballot retrieval and hand counts happen in the counties,
over the days after the seed; ask your county elections office whether and how you can observe.

### When are the results?

The Secretary of State said the audit runs over the next few days and that a report will be posted
on the Secretary of State's website afterwards. This page will link to it.

### What would make the evidence even stronger?

A random sample is evidence about the records it was drawn from and compared with only if those
records were fixed before anyone knew which ballots would be picked. Once the seed is known, a
manifest or a batch total that can still change could be made to fit the sample. So the public
needs a way to confirm that the records were fixed first: publishing them, or their hashes,
before the seed is rolled. This is the idea behind
[Evidence-Based Elections](https://www.stat.berkeley.edu/~stark/Preprints/evidenceVote12.pdf)
(Stark and Wagner, 2012): an election should give convincing evidence that its outcome is right,
not ask to be trusted. Steps used in other states would let anyone confirm it independently:

- before the seed, publish each county's ballot manifest and the reported results the audit
  checks against, batch by batch or ballot by ballot (or at least their SHA-256 hashes), so it is
  clear the ballots were chosen from, and compared with, records fixed in advance;
- when the sample is drawn, publish the list of ballots or batches chosen in each county, so
  observers know what to watch for and anyone can reproduce the selection;
- with the report, publish each audited ballot's or batch's hand count, so anyone can compare it
  with the results published before the seed.

See [timestamping evidence](https://github.com/nealmcb/auditcenter/blob/main/observerfiles/evidence-timestamping.md)
for how observers can fix the evidence in time before an audit.

## 2026 audit dates

### Watch now (Nov 10–24)

- **Wed Nov 18**: Secretary of State generates the RLA's random seed, livestreamed 2:30 pm CT (20:30 UTC) ([YouTube](https://www.youtube.com/live/aPkAeLzbxVg)); the contest audited is U.S. Senate. Seed: 55781838668306731400 (shown on the livestream as 55781 83866 83067 31400), 20 digits from dice rolls called out and repeated, rolled 20:33–20:37 UTC and read back at 20:38 UTC; the audit uses Arlo, and the Secretary of State's staff noted that anyone can run the same open-source software with the same seed to get the same selection ([livestream](https://www.youtube.com/live/aPkAeLzbxVg)). · _official ([SOS release, Nov 16](https://www.sos.state.tx.us/about/newsreleases/2026/111626.shtml))_. Texas's first statewide RLA. YouTube shows the start in each viewer's own time zone, e.g. 1:30 pm in Mountain time
- **Nov 19–20**: First risk-limiting audit under SB 827. · _official (SOS training deck)_. At the seed meeting the Secretary of State's office said counties do the audit over the next one to two days, pulling the selected ballots and reporting back, and that the results will be posted on the SOS website once reviewed

_Not yet confirmed by an official source:_

- Thu Nov 19: Cameron County reviews three races for the statewide audits, 9 am CT (15:00 UTC). · _news ([KRGV](https://www.krgv.com/news/cameron-county-elections-department-to-review-three-races-as-part-of-first-statewide-audit/))_.

### Full calendar, Nov 10 – Jan 2027

- **Nov 18**: RLA seed generated, 2:30 pm CT (20:30 UTC), livestreamed; U.S. Senate contest; seed 55781838668306731400. · _official_. <https://www.sos.state.tx.us/about/newsreleases/2026/111626.shtml>
- **Nov 19–20**: Risk-limiting audit (first under SB 827). · _official_. <https://www.sos.texas.gov/elections/forms/seminar/2026/planning-risk-limiting-audits.pdf>
- **Dec 3**: State canvass deadline; earliest hand count audit deadline. · _computed_. <https://capitol.texas.gov/tlodocs/89R/billtext/html/SB00827F.htm>

## Watched pages

- <https://www.sos.texas.gov/elections/forms/seminar/2026/planning-risk-limiting-audits.pdf> (first SB 827 RLA Nov 19-20; fetched regularly; 1 saved copy)
- <https://www.sos.texas.gov/elections/> (RLA seed event notice; blocked to scripts; 0 saved copies)
- <https://www.sos.state.tx.us/about/newsreleases/2026/111626.shtml> (release: seed generated Nov 18, 2:30 pm CT; U.S. Senate; fetched regularly; 3 saved copies)
- <https://www.sos.state.tx.us/elections/fad/index.shtml> (SOS Audit Program page, where RLA results are expected; fetched regularly; 2 saved copies)

## In the news

Articles and posts from the site's [news log](../news.md), newest first. They are leads, not evidence: the dates above rest on official sources where we have them.

- 2026-11-22 · YouTube: [Cameron County Elections Department to review three races as part of first statewide audit](https://www.youtube.com/watch?v=7zGFkbmSd18)
- 2026-11-21 · Newsweek: [Texas Launches Audit of Senate Race Results after Democratic Sweep - Newsweek](https://www.newsweek.com/texas-launches-audit-of-senate-race-results-after-democratic-sweep-12744250)
- 2026-11-21 · KERA: [Texas Secretary of State launches first-of-its-kind audit of U.S. Senate election, newly required by state law](https://www.kera.org/2026/11/19/texas-secretary-of-state-launches-first-of-its-kind-audit-of-u-s-senate-election-newly-required-by-state-law/)
- 2026-11-21 · The Victoria Advocate: [Texas launches first statewide audit of election results \| The Victoria Advocate](https://victoriaadvocate.com/2026/11/19/texas-launches-first-statewide-audit-of-election-results/)
- 2026-11-21 · Yahoo: [Fact Check: Texas Election Audit Does NOT Just Look At Digital Images -- Secretary Of State Says](https://www.yahoo.com/news/articles/fact-check-texas-election-audit-054813345.html)
- 2026-11-21 · AlterNet: [Texas launches first-ever statewide Senate audit after GOP wipeout - Alternet.org](https://www.alternet.org/texas-senate-audit/)
- 2026-11-21 · Hoodline: [Texas Set to Hand-Count Ballots in Paxton-Talarico Race for First Statewide Audit](https://hoodline.com/2026/11/texas-set-to-hand-count-ballots-in-paxton-talarico-race-for-first-statewide-audit/)
- 2026-11-19 · Houston Public Media: [Texas Secretary of State launches first-of-its-kind audit of U.S. Senate election, newly ...](https://www.houstonpublicmedia.org/articles/news/politics/2026/11/18/567502/texas-secretary-of-state-launches-audit-of-u-s-senate-election/)
- 2026-11-19 · KRGV: [Cameron County Elections Department to review three races as part of first statewide audit](https://www.krgv.com/news/cameron-county-elections-department-to-review-three-races-as-part-of-first-statewide-audit/)
- 2026-11-19 · AOL.com: [Texas launches first statewide risk-limiting election audit - AOL](https://www.aol.com/articles/texas-launches-first-statewide-risk-202538000.html)
- 2026-11-19 · Colorado County Citizen: [Election Canvass - Colorado County Citizen](https://www.coloradocountycitizen.com/article/9337,election-canvass)
- 2026-11-18 · FOX 7 Austin: [Texas picks U.S. Senate race for first statewide ballot audit \| FOX 7 Austin](https://www.fox7austin.com/news/texas-picks-senate-race-first-statewide-ballot-audit)
- 2026-11-18 · Yahoo: [Paxton, Talarico race picked for audit as Texas adds scrutiny - Yahoo](https://www.yahoo.com/news/politics/articles/paxton-talarico-race-picked-audit-181206042.html)
- 2026-11-18 · Texas Border Business: [Texas Secretary of State Begins Mandated Election Audits Following Nov. 3 Vote](https://texasborderbusiness.com/texas-secretary-of-state-begins-mandated-election-audits-following-nov-3-vote/)
- 2026-11-18 · Crossroads Today: [Texas starts statewide election audits \| Local News \| crossroadstoday.com](https://www.crossroadstoday.com/news/local-news/texas-starts-statewide-election-audits/article_e30d2d8a-efcf-4ae3-bf9b-978993914bc4.html)
- 2026-11-18 · Yahoo: [Texas picks U.S. Senate race for first statewide ballot audit - Yahoo](https://www.yahoo.com/news/politics/articles/texas-picks-u-senate-race-185211295.html)
- 2026-11-17 · the Texas Secretary of State: [Texas Secretary of State Initiates Two Audits of the Nov. 3 Election as Prescribed by Law](https://www.sos.state.tx.us/about/newsreleases/2026/111626.shtml)
- 2026-11-10 · Crossroads Today: [Texas post-election audits begin](https://www.crossroadstoday.com/news/texas-post-election-audits-begin/article_56752332-0e54-4f71-a83e-db9741557839.html)

