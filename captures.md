---
layout: default
title: Captures
---


# Captures of state audit pages

Each watched page is fetched every 30 minutes until it goes quiet, then less often (at least every 12 hours; pages that refuse automated fetches, once a day). Requests are conditional, so an unchanged page may answer HTTP 304. A copy is kept whenever its content changes; the time is when we fetched it (UTC), and the sha256 identifies the exact bytes. Pages marked blocked refuse automated fetches and need a browser capture.

## AZ: az-sos-hand-count

https://azsos.gov/node/876

hand count before canvass

Watched since 2026-11-10T15:17:39Z; every fetch has been refused (HTTP 403), so a browser capture is needed.

## CO: co-arapahoe-calendar-data

https://www.arapahoeco.gov/_assets_/plugins/revizeCalendar/calendar_data_handler.php?webspace=arapahoe&relative_revize_url=//cms2.revize.com&protocol=https:

county calendar event data: RLA Wed Nov 18, canvass Fri Nov 20 (events 351, 352)

Watched since 2026-11-17T01:29:58Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-17T01:29:58Z | `cf1fdd85681b27dd…` | [20261117T012958Z.bin](captures/co-arapahoe-calendar-data/20261117T012958Z.bin) |

## CO: co-audit-center

https://www.sos.state.co.us/pubs/elections/auditCenter.html

RLA files: target contests, manifests, CVR hash values, seed (seed Nov 16)

Watched since 2026-11-13T20:01:55Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-13T20:01:55Z | `50cb8ef5c2f78f11…` | [20261113T200155Z.html](captures/co-audit-center/20261113T200155Z.html) |
| 2026-11-16T16:22:15Z | `966990375f300290…` | [20261116T162215Z.html](captures/co-audit-center/20261116T162215Z.html) |
| 2026-11-16T16:41:18Z | `2fea7052330a6f4a…` | [20261116T164118Z.html](captures/co-audit-center/20261116T164118Z.html) |
| 2026-11-16T20:58:16Z | `9f06311d8822b161…` | [20261116T205816Z.html](captures/co-audit-center/20261116T205816Z.html) |
| 2026-11-17T17:49:05Z | `075a3db202f53d10…` | [20261117T174905Z.html](captures/co-audit-center/20261117T174905Z.html) |
| 2026-11-18T22:24:01Z | `e7c6d05b343f2a5d…` | [20261118T222401Z.html](captures/co-audit-center/20261118T222401Z.html) |
| 2026-11-19T18:40:11Z | `1fb721b42867d61f…` | [20261119T184011Z.html](captures/co-audit-center/20261119T184011Z.html) |

## CO: co-rla-2026-general-batch-comparison

https://www.sos.state.co.us/pubs/elections/RLA/2026/general/files/batchCountComparison.csv

ballot manifest and CVR batch comparison

Watched since 2026-11-16T22:47:27Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-16T22:47:27Z | `37edab875e746c92…` | [20261116T224727Z.csv](captures/co-rla-2026-general-batch-comparison/20261116T224727Z.csv) |

## CO: co-rla-2026-general-canonical-list

https://www.sos.state.co.us/pubs/elections/RLA/2026/general/files/2026GeneralCanonicalList.csv

canonical list of contests and choices

Watched since 2026-11-16T22:47:36Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-16T22:47:36Z | `4bc21cf518d6be5e…` | [20261116T224736Z.csv](captures/co-rla-2026-general-canonical-list/20261116T224736Z.csv) |

## CO: co-rla-2026-general-complete-release

https://content.govdelivery.com/accounts/COSOS/bulletins/431cb69

release: statewide RLA complete Nov 19

Watched since 2026-11-19T22:47:35Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-19T22:47:35Z | `dd901977a079da47…` | [20261119T224735Z.html](captures/co-rla-2026-general-complete-release/20261119T224735Z.html) |

## CO: co-rla-2026-general-contests

https://www.sos.state.co.us/pubs/elections/RLA/2026/general/files/2026GeneralRLAContestList.xlsx

target contests

Watched since 2026-11-13T20:01:59Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-13T20:01:59Z | `880cc6b89dd81458…` | [20261113T200159Z.xlsx](captures/co-rla-2026-general-contests/20261113T200159Z.xlsx) |

## CO: co-rla-2026-general-contests-by-county

https://www.sos.state.co.us/pubs/elections/RLA/2026/general/files/contestsByCounty.csv

contest IDs by county

Watched since 2026-11-16T22:47:29Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-16T22:47:29Z | `4412457d715dba73…` | [20261116T224729Z.csv](captures/co-rla-2026-general-contests-by-county/20261116T224729Z.csv) |

## CO: co-rla-2026-general-county-manifests

https://www.sos.state.co.us/pubs/elections/RLA/2026/general/countyManifest.html

county ballot manifests

Watched since 2026-11-16T16:40:59Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-16T16:40:59Z | `844762b780ff3f69…` | [20261116T164059Z.html](captures/co-rla-2026-general-county-manifests/20261116T164059Z.html) |

## CO: co-rla-2026-general-county-tallies

https://www.sos.state.co.us/pubs/elections/RLA/2026/general/files/tabulateCountyPlurality.csv

candidate vote totals by county

Watched since 2026-11-16T22:47:31Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-16T22:47:31Z | `44f717a5416236a7…` | [20261116T224731Z.csv](captures/co-rla-2026-general-county-tallies/20261116T224731Z.csv) |

## CO: co-rla-2026-general-risk-limit

https://www.sos.state.co.us/pubs/elections/RLA/2026/general/riskLimit.html

risk-limit notice (3%)

Watched since 2026-11-13T20:01:57Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-13T20:01:57Z | `c02b1c75cb4eeeb7…` | [20261113T200157Z.html](captures/co-rla-2026-general-risk-limit/20261113T200157Z.html) |
| 2026-11-16T16:40:17Z | `2759d12f57a78419…` | [20261116T164017Z.html](captures/co-rla-2026-general-risk-limit/20261116T164017Z.html) |

## CO: co-rla-2026-general-round1-activityreport

https://www.sos.state.co.us/pubs/elections/RLA/2026/general/files/round1/activityReport.xlsx

audit activity report, round 1

Watched since 2026-11-18T22:47:56Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-18T22:47:56Z | `cd659b309e5e7ae5…` | [20261118T224756Z.xlsx](captures/co-rla-2026-general-round1-activityreport/20261118T224756Z.xlsx) |

## CO: co-rla-2026-general-round1-contest

https://www.sos.state.co.us/pubs/elections/RLA/2026/general/files/round1/contest.csv

contests list, round 1

Watched since 2026-11-18T22:47:48Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-18T22:47:48Z | `663cc14907c78272…` | [20261118T224748Z.csv](captures/co-rla-2026-general-round1-contest/20261118T224748Z.csv) |

## CO: co-rla-2026-general-round1-contestcomparison

https://www.sos.state.co.us/pubs/elections/RLA/2026/general/files/round1/contestComparison.csv

audit comparison report, round 1

Watched since 2026-11-18T22:47:53Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-18T22:47:53Z | <small>8ad8b93e747cb236<wbr>8465cd47665772a6<wbr>c89057bdad85aeb9<wbr>4bf173d9133c1559</small> | [20261118T224753Z.csv](https://github.com/nealmcb/auditcenter/blob/357c682a45367f1da2fc8faacbeb3d6717f150c8/2026/general/files/round1/contestComparison.csv) (identical copy elsewhere) |

## CO: co-rla-2026-general-round1-contestselection

https://www.sos.state.co.us/pubs/elections/RLA/2026/general/files/round1/contestSelection.csv

contest margins and CVR IDs, round 1

Watched since 2026-11-18T22:47:50Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-18T22:47:50Z | `b2539326ad10e807…` | [20261118T224750Z.csv](captures/co-rla-2026-general-round1-contestselection/20261118T224750Z.csv) |

## CO: co-rla-2026-general-round1-resultsreport

https://www.sos.state.co.us/pubs/elections/RLA/2026/general/files/round1/resultsReport.xlsx

audit results report, round 1

Watched since 2026-11-18T22:47:58Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-18T22:47:58Z | `021a30a7c959ba9c…` | [20261118T224758Z.xlsx](captures/co-rla-2026-general-round1-resultsreport/20261118T224758Z.xlsx) |

## CO: co-rla-2026-general-round1-stategeneral

https://www.sos.state.co.us/pubs/elections/RLA/2026/general/files/round1/stateGeneral.xlsx

state audit report, round 1

Watched since 2026-11-18T22:48:01Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-18T22:48:01Z | `2becb6871083382d…` | [20261118T224801Z.xlsx](captures/co-rla-2026-general-round1-stategeneral/20261118T224801Z.xlsx) |

## CO: co-rla-2026-general-round2-activityreport

https://www.sos.state.co.us/pubs/elections/RLA/2026/general/files/round2/activityReport.xlsx

audit activity report, round 2

Watched since 2026-11-19T18:47:43Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-19T18:47:43Z | `383d130e99b60b25…` | [20261119T184743Z.xlsx](captures/co-rla-2026-general-round2-activityreport/20261119T184743Z.xlsx) |

## CO: co-rla-2026-general-round2-contest

https://www.sos.state.co.us/pubs/elections/RLA/2026/general/files/round2/contest.csv

contests list, round 2

Watched since 2026-11-18T22:48:03Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-18T22:48:03Z | `69681810b8420a87…` | [20261118T224803Z.csv](captures/co-rla-2026-general-round2-contest/20261118T224803Z.csv) |

## CO: co-rla-2026-general-round2-contestcomparison

https://www.sos.state.co.us/pubs/elections/RLA/2026/general/files/round2/contestComparison.csv

audit comparison report, round 2

Watched since 2026-11-19T18:47:39Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-19T18:47:39Z | <small>edb71736deab1065<wbr>fa1975dc2a7df594<wbr>13f68ae3375cc894<wbr>670752717d6b106c</small> | [20261119T184739Z.csv](https://github.com/nealmcb/auditcenter/blob/357c682a45367f1da2fc8faacbeb3d6717f150c8/2026/general/files/round2/contestComparison.csv) (identical copy elsewhere) |

## CO: co-rla-2026-general-round2-contestselection

https://www.sos.state.co.us/pubs/elections/RLA/2026/general/files/round2/contestSelection.csv

contest margins and CVR IDs, round 2

Watched since 2026-11-18T22:48:06Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-18T22:48:06Z | `4eb106315f3f0052…` | [20261118T224806Z.csv](captures/co-rla-2026-general-round2-contestselection/20261118T224806Z.csv) |

## CO: co-rla-2026-general-round2-resultsreport

https://www.sos.state.co.us/pubs/elections/RLA/2026/general/files/round2/resultsReport.xlsx

audit results report, round 2

Watched since 2026-11-19T18:47:45Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-19T18:47:45Z | `0f6c5ef58147f672…` | [20261119T184745Z.xlsx](captures/co-rla-2026-general-round2-resultsreport/20261119T184745Z.xlsx) |

## CO: co-rla-2026-general-round2-stategeneral

https://www.sos.state.co.us/pubs/elections/RLA/2026/general/files/round2/stateGeneral.xlsx

state audit report, round 2

Watched since 2026-11-19T18:47:47Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-19T18:47:47Z | `fb58bd19e3d7a02f…` | [20261119T184747Z.xlsx](captures/co-rla-2026-general-round2-stategeneral/20261119T184747Z.xlsx) |

## CO: co-rla-2026-general-seed-notice

https://www.sos.state.co.us/pubs/elections/RLA/2026/general/seedNotice.html

notice of random seed, with CORLA version

Watched since 2026-11-17T18:48:02Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-17T18:48:02Z | `fc7dffd727f775eb…` | [20261117T184802Z.html](captures/co-rla-2026-general-seed-notice/20261117T184802Z.html) |

## CO: co-rla-2026-general-seed-release

https://content.govdelivery.com/accounts/COSOS/bulletins/431c9c8

release giving the 20-digit seed rolled Nov 16

Watched since 2026-11-16T18:47:51Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-16T18:47:51Z | `3c32ec2c6b319b22…` | [20261116T184751Z.html](captures/co-rla-2026-general-seed-release/20261116T184751Z.html) |

## CO: co-rla-2026-general-tallies

https://www.sos.state.co.us/pubs/elections/RLA/2026/general/files/tabulatePlurality.csv

candidate vote totals summary

Watched since 2026-11-16T22:47:34Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-16T22:47:34Z | `2f2692a178807162…` | [20261116T224734Z.csv](captures/co-rla-2026-general-tallies/20261116T224734Z.csv) |

## CO: co-rla-2026-general-upload-hashes

https://www.sos.state.co.us/pubs/elections/RLA/2026/general/files/uploadStatusCountyUploads.csv

upload status and county data file hash values

Watched since 2026-11-16T16:41:01Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-16T16:41:01Z | `773713f555ed98c8…` | [20261116T164101Z.csv](captures/co-rla-2026-general-upload-hashes/20261116T164101Z.csv) |

## DC: dc-audit-selections

https://www.dcboe.org/getContentAsset/13a662ac-2a85-4d4a-9540-2de88e176abc/5ebbd046-860b-4ee1-81c8-43d0e3bc446e/GE2026_Election-Audit-selections_10022026_FINAL.pdf?language=en

audit Nov 21

Watched since 2026-11-10T15:17:44Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-10T15:17:44Z | `5afe172df10a2dad…` | [20261110T151744Z.pdf](captures/dc-audit-selections/20261110T151744Z.pdf) |

## GA: ga-clayton-rla-notice

https://www.claytoncountyga.gov/news/risk-limiting-audit-november-3-2026-general-election/

county RLA notice: starts Nov 12, 12 pm (site may block scripts)

Watched since 2026-11-12T05:25:03Z; every fetch has been refused (HTTP 307), so a browser capture is needed.

## GA: ga-cobb-certification-release

https://www.cobbcounty.gov/news/cobb-county-certifies-results-november-3-general-electionspecial-election

audits Nov 13, 16, 17; enhanced ballot-image audit

Watched since 2026-11-12T05:25:00Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-12T05:25:00Z | `b87ae4a6c0dd4fa1…` | [20261112T052500Z.html](captures/ga-cobb-certification-release/20261112T052500Z.html) |

## GA: ga-cobb-rla-results

https://www.cobbcounty.gov/news/cobb-county-post-election-audits-verify-november-3-election-results

Cobb County release: RLA and ballot image audit results

Watched since 2026-11-18T14:47:58Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-18T14:47:58Z | `7292061a86dd9c0a…` | [20261118T144758Z.html](captures/ga-cobb-rla-results/20261118T144758Z.html) |

## GA: ga-crawford-rla-notice

https://www.crawfordcountyga.org/notice-risk-limiting-audit-4/

county count Nov 13

Watched since 2026-11-10T15:16:52Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-10T15:16:52Z | `f5be44fd89856295…` | [20261110T151652Z.html](captures/ga-crawford-rla-notice/20261110T151652Z.html) |
| 2026-11-10T15:49:40Z | `40ae8bd725e2ac25…` | [20261110T154940Z.html](captures/ga-crawford-rla-notice/20261110T154940Z.html) |
| 2026-11-17T19:21:39Z | `c5e5125089c9fbab…` | [20261117T192139Z.html](captures/ga-crawford-rla-notice/20261117T192139Z.html) |
| 2026-11-17T19:52:33Z | `59c70325e74decf5…` | [20261117T195233Z.html](captures/ga-crawford-rla-notice/20261117T195233Z.html) |
| 2026-11-20T00:56:54Z | `b354b00b3a134ab8…` | [20261120T005654Z.html](captures/ga-crawford-rla-notice/20261120T005654Z.html) |

## GA: ga-crawford-rla-results

https://www.crawfordcountyga.org/notice-risk-limiting-audit-results/

Crawford County notice: RLAs complete Nov 19

Watched since 2026-11-20T02:47:53Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-20T02:47:53Z | `287382753720bfe3…` | [20261120T024753Z.html](captures/ga-crawford-rla-results/20261120T024753Z.html) |

## GA: ga-forsyth-elections

https://www.forsythco.com/government/departments/voter-registrations-elections/current-upcoming-elections/

RLA results to be posted here

Watched since 2026-11-12T05:24:55Z; fetched successfully until 2026-11-20T06:22:57Z, refused since (HTTP curl: (28) Connection timed out after 90001 milliseconds).

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-12T05:24:55Z | `d7d6acd24c358fcb…` | [20261112T052455Z.html](captures/ga-forsyth-elections/20261112T052455Z.html) |
| 2026-11-14T05:42:35Z | `d3b1f504b4df9275…` | [20261114T054235Z.html](captures/ga-forsyth-elections/20261114T054235Z.html) |
| 2026-11-17T22:26:54Z | `bc137bcbe571ce81…` | [20261117T222654Z.html](captures/ga-forsyth-elections/20261117T222654Z.html) |

## GA: ga-forsyth-rla-notice

https://forsythco.b-cdn.net/app/uploads/2026/11/Public-Notice-of-RLA-11-03-26-General-General-Election-Special-Elections-UA-1.pdf

county RLA notice: starts Nov 12, 1 pm

Watched since 2026-11-12T05:24:52Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-12T05:24:52Z | `74e1b92fae51225a…` | [20261112T052452Z.pdf](captures/ga-forsyth-rla-notice/20261112T052452Z.pdf) |

## GA: ga-forsyth-rla-results-notice

https://forsythco.b-cdn.net/app/uploads/2026/11/Public-Notice-of-Audit-Results-11-17-2026-with-links-UA-rev.pdf

RLA results notice, posted Nov 17

Watched since 2026-11-17T22:48:10Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-17T22:48:10Z | `b3f02c4a85e242d4…` | [20261117T224810Z.pdf](captures/ga-forsyth-rla-results-notice/20261117T224810Z.pdf) |

## GA: ga-forsyth-rla-tally-bre

https://www.forsythco.com/app/uploads/2026/11/11-03-26-RLA-BRE-selected-Batch-Tally-Sheet-1.pdf

audit board tally sheet, batch chosen by the county board

Watched since 2026-11-17T22:48:17Z; fetched successfully until 2026-11-20T06:23:40Z, refused since (HTTP curl: (28) Connection timed out after 90001 milliseconds).

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-17T22:48:17Z | `3813dc1f07089a93…` | [20261117T224817Z.pdf](captures/ga-forsyth-rla-tally-bre/20261117T224817Z.pdf) |

## GA: ga-forsyth-rla-tally-sos

https://www.forsythco.com/app/uploads/2026/11/11-03-26-RLA.-SOS-selected-Batches-Tally-Sheets.pdf

audit board tally sheets, SOS-selected batches

Watched since 2026-11-17T22:48:15Z; fetched successfully until 2026-11-20T06:23:37Z, refused since (HTTP curl: (28) Connection timed out after 90002 milliseconds).

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-17T22:48:15Z | `62d0fcfba901398a…` | [20261117T224815Z.pdf](captures/ga-forsyth-rla-tally-sos/20261117T224815Z.pdf) |

## GA: ga-forsyth-rla-totals

https://www.forsythco.com/app/uploads/2026/11/11-13-2026-RLA-Totals-of-11-03-26-General-Election-and-Special-Elections.pdf

breakdown of RLA hand-count results

Watched since 2026-11-17T22:48:12Z; fetched successfully until 2026-11-20T06:23:35Z, refused since (HTTP curl: (28) Connection timed out after 90001 milliseconds).

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-17T22:48:12Z | `966b230e992e88dc…` | [20261117T224812Z.pdf](captures/ga-forsyth-rla-totals/20261117T224812Z.pdf) |

## GA: ga-fulton-rla-notice

https://www.fultoncountyga.gov/-/media/November-3-Election-notices/Notice-of-Risk-Limiting-Audit--1132026.pdf

county count Nov 13-17

Watched since 2026-11-10T15:16:50Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-10T15:16:50Z | `9fa3d5b57fd370d5…` | [20261110T151650Z.pdf](captures/ga-fulton-rla-notice/20261110T151650Z.pdf) |

## GA: ga-gwinnett-rla-notice

https://www.gwinnettcounty.com/documents/d/gwinnett-county/notice-november-3-general-special-election-risk-limiting-ballot-image-audit?download=true

county RLA notice: starts Nov 12, 12 pm

Watched since 2026-11-12T05:24:50Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-12T05:24:50Z | `f7f4885457e290af…` | [20261112T052450Z.pdf](captures/ga-gwinnett-rla-notice/20261112T052450Z.pdf) |

## GA: ga-richmond-rla-notice

https://www.augustaga.gov/m/newsflash/Home/Detail/4291

county RLA notice: starts Nov 13, 9 am

Watched since 2026-11-12T05:24:58Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-12T05:24:58Z | `48a3dfd357c0e490…` | [20261112T052458Z.html](captures/ga-richmond-rla-notice/20261112T052458Z.html) |
| 2026-11-16T18:26:30Z | `f9ae0e487592abd8…` | [20261116T182630Z.html](captures/ga-richmond-rla-notice/20261116T182630Z.html) |
| 2026-11-18T22:54:48Z | `821d3af3a4507c00…` | [20261118T225448Z.html](captures/ga-richmond-rla-notice/20261118T225448Z.html) |

## GA: ga-sos-audit-information

https://sos.ga.gov/page/elections-audit-information

RLA artifacts, hashes; kickoff expected Nov 12

Watched since 2026-11-10T15:16:45Z; fetched successfully until 2026-11-10T15:34:04Z, refused since (HTTP 403).

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-10T15:34:04Z | `a5c736916a083eb5…` | [20261110T153404Z-browser.html](captures/ga-sos-audit-information/20261110T153404Z-browser.html) |

## GA: ga-sos-news

https://sos.ga.gov/news

RLA kickoff media advisory and results release

Watched since 2026-11-10T15:16:48Z; fetched successfully until 2026-11-10T15:34:19Z, refused since (HTTP 403).

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-10T15:34:19Z | `398c4f56bcceaac4…` | [20261110T153419Z-browser.html](captures/ga-sos-news/20261110T153419Z-browser.html) |

## GA: ga-sos-rla-results-release

https://sos.ga.gov/news/historic-number-risk-limiting-audits-confirm-election-outcomes

SOS release: RLAs confirm outcomes (refuses scripts)

Watched since 2026-11-20T02:47:56Z; every fetch has been refused (HTTP 403), so a browser capture is needed.

## KS: ks-audit-dates-xlsx

https://kssos.org/elections/26elec/2026-General-Election-Post-Election-Audit-Dates.xlsx

county audit dates

Watched since 2026-11-10T15:19:31Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-10T15:19:31Z | `7b81042f1e64a9cf…` | [20261110T151931Z.xlsx](captures/ks-audit-dates-xlsx/20261110T151931Z.xlsx) |

## KS: ks-post-election-audit

https://kssos.org/elections/post-election-audit.html

county audit dates spreadsheet

Watched since 2026-11-10T15:17:24Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-10T15:17:24Z | `9f7921d81957d9a2…` | [20261110T151724Z.html](captures/ks-post-election-audit/20261110T151724Z.html) |

## MD: md-2026-calendar

https://elections.maryland.gov/elections/2026/2026_Election_Calendar.pdf

RLA contest selection Nov 23, due Dec 2

Watched since 2026-11-10T15:17:07Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-10T15:17:07Z | `21225ab8a188feb3…` | [20261110T151707Z.pdf](captures/md-2026-calendar/20261110T151707Z.pdf) |
| 2026-11-19T20:46:07Z | `8319b01f12e0c257…` | [20261119T204607Z.pdf](captures/md-2026-calendar/20261119T204607Z.pdf) |

## MD: md-ballot-audit-plan

https://elections.maryland.gov/voting_system/ballot_audit_plan.html

2026 audit plan

Watched since 2026-11-10T15:19:29Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-10T15:19:29Z | `fcfdb66b84834740…` | [20261110T151929Z.html](captures/md-ballot-audit-plan/20261110T151929Z.html) |
| 2026-11-10T15:50:39Z | `a53fbacfb6d3571d…` | [20261110T155039Z.html](captures/md-ballot-audit-plan/20261110T155039Z.html) |
| 2026-11-17T18:50:49Z | `83400ec8810d111c…` | [20261117T185049Z.html](captures/md-ballot-audit-plan/20261117T185049Z.html) |
| 2026-11-17T19:21:57Z | `9858b0ea8c07f733…` | [20261117T192157Z.html](captures/md-ballot-audit-plan/20261117T192157Z.html) |

## MD: md-rla-page

https://elections.maryland.gov/voting_system/ballot_audit_plan_manual.html

RLA results and ceremony posting

Watched since 2026-11-10T15:19:26Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-10T15:19:26Z | `333c0123002fa005…` | [20261110T151926Z.html](captures/md-rla-page/20261110T151926Z.html) |
| 2026-11-10T15:50:37Z | `8f71ce59a6ef2ec7…` | [20261110T155037Z.html](captures/md-rla-page/20261110T155037Z.html) |

## MN: mn-post-election-reviews

https://www.sos.mn.gov/elections-voting/how-elections-work/post-election-reviews/

selected precincts

Watched since 2026-11-10T15:17:46Z; fetched successfully until 2026-11-19T20:14:22Z, refused since (HTTP 200).

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-19T20:14:22Z | `16ed6501be147baf…` | [20261119T201422Z.html](captures/mn-post-election-reviews/20261119T201422Z.html) |

## MT: mt-elections

https://sosmt.gov/elections/

State Board dice draw Nov 10-12

Watched since 2026-11-10T15:17:19Z; every fetch has been refused (HTTP 403), so a browser capture is needed.

## NC: nc-election-results-releases

https://www.ncsbe.gov/press-release-terms/election-results

Nov 4 sample selection release

Watched since 2026-11-10T15:17:26Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-10T15:17:26Z | `bb0f18dbb597cf1a…` | [20261110T151726Z.html](captures/nc-election-results-releases/20261110T151726Z.html) |
| 2026-11-10T21:15:18Z | `3b6f76d34bd78e8e…` | [20261110T211518Z.html](captures/nc-election-results-releases/20261110T211518Z.html) |
| 2026-11-13T16:28:21Z | `94ef572588fec23c…` | [20261113T162821Z.html](captures/nc-election-results-releases/20261113T162821Z.html) |
| 2026-11-20T22:37:17Z | `34ad3962cd616b73…` | [20261120T223717Z.html](captures/nc-election-results-releases/20261120T223717Z.html) |

## ND: nd-post-election-audits

https://www.sos.nd.gov/elections/election-security/post-election-audits

selected polling locations

Watched since 2026-11-10T15:17:28Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-10T15:17:28Z | `932faafad08f66f3…` | [20261110T151728Z.html](captures/nd-post-election-audits/20261110T151728Z.html) |

## NM: nm-elections

https://www.sos.nm.gov/voting-and-elections/

auditor precinct selection by Nov 15

Watched since 2026-11-10T15:17:49Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-10T15:17:49Z | `6669d7a41791658a…` | [20261110T151749Z.html](captures/nm-elections/20261110T151749Z.html) |

## NV: nv-rla

https://www.nvsos.gov/elections/election-information/2026-election-information

2026 election information page, which links each election's RLA certificate (the old RLA page is gone; refuses scripts)

Watched since 2026-11-10T15:17:17Z; every fetch has been refused (HTTP 200 or a bot-challenge page), so a browser capture is needed.

## OR: or-current-election

https://sos.oregon.gov/voting/pages/current-election.aspx

selection Nov 25

Watched since 2026-11-10T15:17:41Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-10T15:17:41Z | `94c84a2043e41d38…` | [20261110T151741Z.html](captures/or-current-election/20261110T151741Z.html) |
| 2026-11-10T15:19:17Z | `25a7c134a84187b8…` | [20261110T151917Z.html](captures/or-current-election/20261110T151917Z.html) |
| 2026-11-10T15:50:27Z | `e260342109130b16…` | [20261110T155027Z.html](captures/or-current-election/20261110T155027Z.html) |

## PA: pa-dos-newsroom

https://www.pa.gov/agencies/dos/newsroom

day-of RLA dice-roll release (Nov 13), with seed and livestream

Watched since 2026-11-13T00:55:28Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-13T00:55:28Z | `94ff62018721654c…` | [20261113T005528Z.html](captures/pa-dos-newsroom/20261113T005528Z.html) |

## PA: pa-post-election-audits

https://www.pa.gov/en/agencies/vote/elections/post-election-audits.html

RLA dice roll Nov 13 (Governor)

Watched since 2026-11-10T15:16:55Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-10T15:16:55Z | `8b5c2d15bc6ad3d4…` | [20261110T151655Z.html](captures/pa-post-election-audits/20261110T151655Z.html) |
| 2026-11-10T15:49:43Z | `925987592c687b0b…` | [20261110T154943Z.html](captures/pa-post-election-audits/20261110T154943Z.html) |
| 2026-11-13T18:57:07Z | `45e60eab24cbfe4c…` | [20261113T185707Z.html](captures/pa-post-election-audits/20261113T185707Z.html) |
| 2026-11-20T15:13:53Z | `c054cd31ab8e8295…` | [20261120T151353Z.html](captures/pa-post-election-audits/20261120T151353Z.html) |

## PA: pa-rla-2026-general-report

https://www.pa.gov/content/dam/copapwp-pagov/en/vote/elections/risk-limiting-audit-reports/2026-general-election/audit-report-november-3-2026-general-election-2026-11-19t1653z.csv

Arlo audit report, 2026 general RLA (generated 2026-11-19 16:53 UTC)

Watched since 2026-11-20T18:47:23Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-20T18:47:23Z | `98cb8c7e6b835a41…` | [20261120T184723Z.csv](captures/pa-rla-2026-general-report/20261120T184723Z.csv) |

## RI: ri-rla-center

https://elections.ri.gov/elections/risk-limiting-audit-center

targets by Nov 13; seed ceremony

Watched since 2026-11-10T15:17:12Z; every fetch has been refused (HTTP 403), so a browser capture is needed.

## SC: sc-election-audits

https://scvotes.gov/elections-statistics/election-audits/

ballot-image audit

Watched since 2026-11-10T15:17:36Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-10T15:17:36Z | `05a2fcf1f52c4173…` | [20261110T151736Z.html](captures/sc-election-audits/20261110T151736Z.html) |
| 2026-11-10T16:03:04Z | `39d59c31de604070…` | [20261110T160304Z.html](captures/sc-election-audits/20261110T160304Z.html) |
| 2026-11-10T16:34:16Z | `05a2fcf1f52c4173…` | [20261110T163416Z.html](captures/sc-election-audits/20261110T163416Z.html) |
| 2026-11-10T17:05:28Z | `39d59c31de604070…` | [20261110T170528Z.html](captures/sc-election-audits/20261110T170528Z.html) |
| 2026-11-10T17:36:38Z | `05a2fcf1f52c4173…` | [20261110T173638Z.html](captures/sc-election-audits/20261110T173638Z.html) |
| 2026-11-10T18:07:48Z | `c2fdd2d9454d186f…` | [20261110T180748Z.html](captures/sc-election-audits/20261110T180748Z.html) |
| 2026-11-10T19:10:29Z | `be4e209577e690e3…` | [20261110T191029Z.html](captures/sc-election-audits/20261110T191029Z.html) |
| 2026-11-10T19:41:45Z | `05a2fcf1f52c4173…` | [20261110T194145Z.html](captures/sc-election-audits/20261110T194145Z.html) |
| 2026-11-10T20:13:01Z | `be4e209577e690e3…` | [20261110T201301Z.html](captures/sc-election-audits/20261110T201301Z.html) |
| 2026-11-10T20:44:11Z | `05a2fcf1f52c4173…` | [20261110T204411Z.html](captures/sc-election-audits/20261110T204411Z.html) |
| 2026-11-10T21:15:26Z | `c2fdd2d9454d186f…` | [20261110T211526Z.html](captures/sc-election-audits/20261110T211526Z.html) |
| 2026-11-10T21:46:37Z | `be4e209577e690e3…` | [20261110T214637Z.html](captures/sc-election-audits/20261110T214637Z.html) |
| 2026-11-10T22:17:52Z | `05a2fcf1f52c4173…` | [20261110T221752Z.html](captures/sc-election-audits/20261110T221752Z.html) |
| 2026-11-10T23:20:12Z | `c2fdd2d9454d186f…` | [20261110T232012Z.html](captures/sc-election-audits/20261110T232012Z.html) |
| 2026-11-10T23:51:22Z | `39d59c31de604070…` | [20261110T235122Z.html](captures/sc-election-audits/20261110T235122Z.html) |
| 2026-11-11T00:22:32Z | `c9a963e1ce346f46…` | [20261111T002232Z.html](captures/sc-election-audits/20261111T002232Z.html) |
| 2026-11-11T01:24:58Z | `158f379cdbdaa127…` | [20261111T012458Z.html](captures/sc-election-audits/20261111T012458Z.html) |
| 2026-11-11T01:56:11Z | `36116d38f1ea7a04…` | [20261111T015611Z.html](captures/sc-election-audits/20261111T015611Z.html) |
| 2026-11-11T02:27:22Z | `c2fe7db1574c5197…` | [20261111T022722Z.html](captures/sc-election-audits/20261111T022722Z.html) |
| 2026-11-11T02:58:36Z | `c9a963e1ce346f46…` | [20261111T025836Z.html](captures/sc-election-audits/20261111T025836Z.html) |
| 2026-11-11T03:29:48Z | `158f379cdbdaa127…` | [20261111T032948Z.html](captures/sc-election-audits/20261111T032948Z.html) |
| 2026-11-11T04:32:09Z | `c9a963e1ce346f46…` | [20261111T043209Z.html](captures/sc-election-audits/20261111T043209Z.html) |
| 2026-11-11T05:03:24Z | `c2fe7db1574c5197…` | [20261111T050324Z.html](captures/sc-election-audits/20261111T050324Z.html) |
| 2026-11-11T05:34:34Z | `c9a963e1ce346f46…` | [20261111T053434Z.html](captures/sc-election-audits/20261111T053434Z.html) |
| 2026-11-11T06:36:55Z | `36116d38f1ea7a04…` | [20261111T063655Z.html](captures/sc-election-audits/20261111T063655Z.html) |
| 2026-11-11T07:39:15Z | `158f379cdbdaa127…` | [20261111T073915Z.html](captures/sc-election-audits/20261111T073915Z.html) |
| 2026-11-11T08:10:25Z | `e093b8e61b75e443…` | [20261111T081025Z.html](captures/sc-election-audits/20261111T081025Z.html) |
| 2026-11-11T09:12:44Z | `9a49091256a2899b…` | [20261111T091244Z.html](captures/sc-election-audits/20261111T091244Z.html) |
| 2026-11-11T09:43:53Z | `e093b8e61b75e443…` | [20261111T094353Z.html](captures/sc-election-audits/20261111T094353Z.html) |
| 2026-11-11T10:46:13Z | `fb310525e9bd49da…` | [20261111T104613Z.html](captures/sc-election-audits/20261111T104613Z.html) |
| 2026-11-11T11:17:24Z | `9a49091256a2899b…` | [20261111T111724Z.html](captures/sc-election-audits/20261111T111724Z.html) |
| 2026-11-11T12:19:43Z | `9608683ece35c6f8…` | [20261111T121943Z.html](captures/sc-election-audits/20261111T121943Z.html) |
| 2026-11-11T13:22:02Z | `5c56995a1ad32e8f…` | [20261111T132202Z.html](captures/sc-election-audits/20261111T132202Z.html) |
| 2026-11-11T13:53:12Z | `9608683ece35c6f8…` | [20261111T135312Z.html](captures/sc-election-audits/20261111T135312Z.html) |
| 2026-11-11T14:55:32Z | `ed7e952cc1159fa1…` | [20261111T145532Z.html](captures/sc-election-audits/20261111T145532Z.html) |
| 2026-11-11T15:26:42Z | `5c56995a1ad32e8f…` | [20261111T152642Z.html](captures/sc-election-audits/20261111T152642Z.html) |
| 2026-11-11T15:57:51Z | `ed7e952cc1159fa1…` | [20261111T155751Z.html](captures/sc-election-audits/20261111T155751Z.html) |
| 2026-11-11T17:00:12Z | `9608683ece35c6f8…` | [20261111T170012Z.html](captures/sc-election-audits/20261111T170012Z.html) |
| 2026-11-11T17:31:23Z | `90db8e6fcb6ce248…` | [20261111T173123Z.html](captures/sc-election-audits/20261111T173123Z.html) |
| 2026-11-11T18:02:34Z | `9608683ece35c6f8…` | [20261111T180234Z.html](captures/sc-election-audits/20261111T180234Z.html) |
| 2026-11-11T18:33:45Z | `5c56995a1ad32e8f…` | [20261111T183345Z.html](captures/sc-election-audits/20261111T183345Z.html) |
| 2026-11-11T19:04:56Z | `90db8e6fcb6ce248…` | [20261111T190456Z.html](captures/sc-election-audits/20261111T190456Z.html) |
| 2026-11-11T19:36:07Z | `ed7e952cc1159fa1…` | [20261111T193607Z.html](captures/sc-election-audits/20261111T193607Z.html) |
| 2026-11-11T20:38:34Z | `90db8e6fcb6ce248…` | [20261111T203834Z.html](captures/sc-election-audits/20261111T203834Z.html) |
| 2026-11-11T21:09:45Z | `9608683ece35c6f8…` | [20261111T210945Z.html](captures/sc-election-audits/20261111T210945Z.html) |
| 2026-11-11T21:40:56Z | `5c56995a1ad32e8f…` | [20261111T214056Z.html](captures/sc-election-audits/20261111T214056Z.html) |
| 2026-11-11T23:14:34Z | `9608683ece35c6f8…` | [20261111T231434Z.html](captures/sc-election-audits/20261111T231434Z.html) |
| 2026-11-11T23:45:49Z | `90db8e6fcb6ce248…` | [20261111T234549Z.html](captures/sc-election-audits/20261111T234549Z.html) |
| 2026-11-12T00:17:02Z | `94c643f3f98a57dd…` | [20261112T001702Z.html](captures/sc-election-audits/20261112T001702Z.html) |
| 2026-11-12T00:48:14Z | `8a619b6a3b3ff4e8…` | [20261112T004814Z.html](captures/sc-election-audits/20261112T004814Z.html) |
| 2026-11-12T01:19:25Z | `05d53e2cdbdc9afc…` | [20261112T011925Z.html](captures/sc-election-audits/20261112T011925Z.html) |
| 2026-11-12T01:50:39Z | `b99e03783ed4c50a…` | [20261112T015039Z.html](captures/sc-election-audits/20261112T015039Z.html) |
| 2026-11-12T02:21:52Z | `05d53e2cdbdc9afc…` | [20261112T022152Z.html](captures/sc-election-audits/20261112T022152Z.html) |
| 2026-11-12T03:24:21Z | `b99e03783ed4c50a…` | [20261112T032421Z.html](captures/sc-election-audits/20261112T032421Z.html) |
| 2026-11-12T03:55:34Z | `05d53e2cdbdc9afc…` | [20261112T035534Z.html](captures/sc-election-audits/20261112T035534Z.html) |
| 2026-11-12T04:26:47Z | `94c643f3f98a57dd…` | [20261112T042647Z.html](captures/sc-election-audits/20261112T042647Z.html) |
| 2026-11-12T04:58:06Z | `b99e03783ed4c50a…` | [20261112T045806Z.html](captures/sc-election-audits/20261112T045806Z.html) |
| 2026-11-12T05:29:22Z | `8a619b6a3b3ff4e8…` | [20261112T052922Z.html](captures/sc-election-audits/20261112T052922Z.html) |
| 2026-11-12T06:00:52Z | `94c643f3f98a57dd…` | [20261112T060052Z.html](captures/sc-election-audits/20261112T060052Z.html) |
| 2026-11-12T06:32:41Z | `8a619b6a3b3ff4e8…` | [20261112T063241Z.html](captures/sc-election-audits/20261112T063241Z.html) |
| 2026-11-12T07:04:26Z | `b99e03783ed4c50a…` | [20261112T070426Z.html](captures/sc-election-audits/20261112T070426Z.html) |
| 2026-11-12T07:36:05Z | `94c643f3f98a57dd…` | [20261112T073605Z.html](captures/sc-election-audits/20261112T073605Z.html) |
| 2026-11-12T08:07:34Z | `0341fbbfe9ab53ae…` | [20261112T080734Z.html](captures/sc-election-audits/20261112T080734Z.html) |
| 2026-11-12T08:39:02Z | `0f2f440e9862fb7f…` | [20261112T083902Z.html](captures/sc-election-audits/20261112T083902Z.html) |
| 2026-11-12T09:10:33Z | `0341fbbfe9ab53ae…` | [20261112T091033Z.html](captures/sc-election-audits/20261112T091033Z.html) |
| 2026-11-12T09:42:03Z | `0f2f440e9862fb7f…` | [20261112T094203Z.html](captures/sc-election-audits/20261112T094203Z.html) |
| 2026-11-12T10:13:32Z | `16be0d414152860d…` | [20261112T101332Z.html](captures/sc-election-audits/20261112T101332Z.html) |
| 2026-11-12T10:44:58Z | `0f2f440e9862fb7f…` | [20261112T104458Z.html](captures/sc-election-audits/20261112T104458Z.html) |
| 2026-11-12T11:16:24Z | `16be0d414152860d…` | [20261112T111624Z.html](captures/sc-election-audits/20261112T111624Z.html) |
| 2026-11-12T11:47:53Z | `0f2f440e9862fb7f…` | [20261112T114753Z.html](captures/sc-election-audits/20261112T114753Z.html) |
| 2026-11-12T12:19:21Z | `f28770fca54a0815…` | [20261112T121921Z.html](captures/sc-election-audits/20261112T121921Z.html) |
| 2026-11-12T12:51:04Z | `34cf2cd0b83c5bd0…` | [20261112T125104Z.html](captures/sc-election-audits/20261112T125104Z.html) |
| 2026-11-12T13:54:01Z | `43c2e9404d651ab3…` | [20261112T135401Z.html](captures/sc-election-audits/20261112T135401Z.html) |
| 2026-11-12T14:25:29Z | `f28770fca54a0815…` | [20261112T142529Z.html](captures/sc-election-audits/20261112T142529Z.html) |
| 2026-11-12T14:56:57Z | `43c2e9404d651ab3…` | [20261112T145657Z.html](captures/sc-election-audits/20261112T145657Z.html) |
| 2026-11-12T15:28:26Z | `ec0d528cf419139a…` | [20261112T152826Z.html](captures/sc-election-audits/20261112T152826Z.html) |
| 2026-11-12T15:59:54Z | `f28770fca54a0815…` | [20261112T155954Z.html](captures/sc-election-audits/20261112T155954Z.html) |
| 2026-11-12T16:31:23Z | `34cf2cd0b83c5bd0…` | [20261112T163123Z.html](captures/sc-election-audits/20261112T163123Z.html) |
| 2026-11-12T17:34:27Z | `f28770fca54a0815…` | [20261112T173427Z.html](captures/sc-election-audits/20261112T173427Z.html) |
| 2026-11-12T18:05:56Z | `34cf2cd0b83c5bd0…` | [20261112T180556Z.html](captures/sc-election-audits/20261112T180556Z.html) |
| 2026-11-12T18:37:25Z | `ec0d528cf419139a…` | [20261112T183725Z.html](captures/sc-election-audits/20261112T183725Z.html) |
| 2026-11-12T19:09:00Z | `43c2e9404d651ab3…` | [20261112T190900Z.html](captures/sc-election-audits/20261112T190900Z.html) |
| 2026-11-12T20:11:58Z | `f28770fca54a0815…` | [20261112T201158Z.html](captures/sc-election-audits/20261112T201158Z.html) |
| 2026-11-12T20:43:33Z | `34cf2cd0b83c5bd0…` | [20261112T204333Z.html](captures/sc-election-audits/20261112T204333Z.html) |
| 2026-11-12T21:46:47Z | `f28770fca54a0815…` | [20261112T214647Z.html](captures/sc-election-audits/20261112T214647Z.html) |
| 2026-11-12T22:48:44Z | `f28770fca54a0815…` | [20261112T224844Z.html](captures/sc-election-audits/20261112T224844Z.html) |

## SC: sc-hand-count-audit-2026

https://scvotes.gov/hand-count-audit-for-the-2026-statewide-general-election/

selected precincts and contests

Watched since 2026-11-10T15:17:31Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-10T15:17:31Z | `ef1cb463c7596c54…` | [20261110T151731Z.html](captures/sc-hand-count-audit-2026/20261110T151731Z.html) |
| 2026-11-11T08:10:22Z | `a0d21dcda1b49794…` | [20261111T081022Z.html](captures/sc-hand-count-audit-2026/20261111T081022Z.html) |
| 2026-11-12T08:07:31Z | `37223284f7181fcc…` | [20261112T080731Z.html](captures/sc-hand-count-audit-2026/20261112T080731Z.html) |
| 2026-11-12T22:48:41Z | `37223284f7181fcc…` | [20261112T224841Z.html](captures/sc-hand-count-audit-2026/20261112T224841Z.html) |

## TX: tx-elections-home

https://www.sos.texas.gov/elections/

RLA seed event notice

Watched since 2026-11-10T15:17:05Z; every fetch has been refused (HTTP 403), so a browser capture is needed.

## TX: tx-rla-planning-deck

https://www.sos.texas.gov/elections/forms/seminar/2026/planning-risk-limiting-audits.pdf

first SB 827 RLA Nov 19-20

Watched since 2026-11-10T15:17:03Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-10T15:17:03Z | `973b2503638fa5ae…` | [20261110T151703Z.pdf](captures/tx-rla-planning-deck/20261110T151703Z.pdf) |

## TX: tx-sos-audit-program

https://www.sos.state.tx.us/elections/fad/index.shtml

SOS Audit Program page, where RLA results are expected

Watched since 2026-11-18T20:38:58Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-18T20:38:58Z | `9f32f2b4ff871f4d…` | [20261118T203858Z.html](captures/tx-sos-audit-program/20261118T203858Z.html) |

## TX: tx-sos-rla-release-2026-11-16

https://www.sos.state.tx.us/about/newsreleases/2026/111626.shtml

release: seed generated Nov 18, 2:30 pm CT; U.S. Senate

Watched since 2026-11-17T18:48:04Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-17T18:48:04Z | `b59f56781b9a49c2…` | [20261117T184804Z.html](captures/tx-sos-rla-release-2026-11-16/20261117T184804Z.html) |
| 2026-11-18T20:21:13Z | `c90a541c4b978eef…` | [20261118T202113Z.html](captures/tx-sos-rla-release-2026-11-16/20261118T202113Z.html) |

## VA: va-rla

https://www.elections.virginia.gov/resultsreports/election-security/rla

State Board RLA selection; RLA before Dec 7

Watched since 2026-11-10T15:17:14Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-10T15:17:14Z | `38bd7f3df669f778…` | [20261110T151714Z.html](captures/va-rla/20261110T151714Z.html) |
| 2026-11-13T05:25:55Z | `38bd7f3df669f778…` | [20261113T052555Z.html](captures/va-rla/20261113T052555Z.html) |
| 2026-11-17T06:37:29Z | `34a154cfeea0bc44…` | [20261117T063729Z.html](captures/va-rla/20261117T063729Z.html) |

## WA: wa-king-observing

https://kingcounty.gov/en/dept/elections/about-us/security-and-accountability/observing-elections-activities

King County's observing schedule: RLA Nov 19, 9:00 am

Watched since 2026-11-18T17:10:19Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-18T17:10:19Z | `eb1c8dc4bbe8a9f3…` | [20261118T171019Z.html](captures/wa-king-observing/20261118T171019Z.html) |
| 2026-11-19T01:31:03Z | `0452df0c4a546a88…` | [20261119T013103Z.html](captures/wa-king-observing/20261119T013103Z.html) |
| 2026-11-19T23:54:56Z | `c80e72e62dc128cf…` | [20261119T235456Z.html](captures/wa-king-observing/20261119T235456Z.html) |
| 2026-11-20T05:52:14Z | `6dd9b9ec971a8566…` | [20261120T055214Z.html](captures/wa-king-observing/20261120T055214Z.html) |

## WA: wa-post-election-audits

https://www.sos.wa.gov/elections/data-research/election-technology/post-election-audits

WA audit index

Watched since 2026-11-10T15:17:01Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-10T15:17:01Z | `2419b6664cc32906…` | [20261110T151701Z.html](captures/wa-post-election-audits/20261110T151701Z.html) |
| 2026-11-10T15:18:40Z | `7743ed9b7841e22e…` | [20261110T151840Z.html](captures/wa-post-election-audits/20261110T151840Z.html) |
| 2026-11-10T15:49:48Z | `a30566af34c688ce…` | [20261110T154948Z.html](captures/wa-post-election-audits/20261110T154948Z.html) |
| 2026-11-10T16:33:42Z | `c4486535e1709a97…` | [20261110T163342Z.html](captures/wa-post-election-audits/20261110T163342Z.html) |
| 2026-11-12T16:30:47Z | `51a03472df9095f6…` | [20261112T163047Z.html](captures/wa-post-election-audits/20261112T163047Z.html) |
| 2026-11-13T22:08:53Z | `fef3267d9ae50642…` | [20261113T220853Z.html](captures/wa-post-election-audits/20261113T220853Z.html) |

## WI: wi-audit-selection

https://elections.wi.gov/node/11791

WEC random selection

Watched since 2026-11-10T15:17:21Z; every fetch has been refused (HTTP 403), so a browser capture is needed.

## WI: wi-madison-audit-notice

https://www.cityofmadison.com/city-hall/committees/meeting-schedule/documents/agendas/Public%20Notice_1.pdf

City of Madison voting equipment audit notice, Nov 20

Watched since 2026-11-20T23:53:49Z.

| Changed at (UTC) | sha256 | Copy |
|---|---|---|
| 2026-11-20T23:53:49Z | `8d8b30675980241e…` | [20261120T235349Z.pdf](captures/wi-madison-audit-notice/20261120T235349Z.pdf) |

