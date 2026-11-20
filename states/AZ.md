---
layout: default
title: Arizona
---


# Arizona

[← All states](index.md) · [Calendar](../calendar.md) · [Captures](../captures.md)

## Hand count audits of the November 3, 2026 General Election

Each county's hand count audit (A.R.S. § 16-602) counts by hand the ballots from at least 2% of its
polling places or vote centers and a sample of early-ballot batches, in a few races drawn by lot by
the political parties' county representatives, and compares the counts with the machine results.
A difference within the designated margin set by the Vote Count Verification Committee needs no
further counting. The Secretary of State posts every county's report on its
[2026 election information page](https://azsos.gov/elections/election-information/2026-election-info)
("Hand Count Results for 2026 General Election"). That site refuses automated fetches, so copies of
all of them, with their SHA-256 hashes, are in this site's
[evidence folder](https://github.com/nealmcb/audit-results/tree/main/evidence/AZ). We don't know
when each report was posted: our scheduled checks of the hand count page were refused from
November 10 on, and the copies here were saved from a browser on November 20. The PDFs' own
creation dates run from November 6 (Apache, Coconino) to November 16 (Maricopa, revised
November 17).

All 15 counties' reports say their hand counts confirmed the machine results. Ten report no
differences; five report differences of one to seven votes in a race, all within the designated
margin, so no count was expanded.

| County | Sampled (drawn Nov 4 unless noted) | Races | Result, in the report's words |
|---|---|---|---|
| [Apache](../evidence/AZ/2026_General_HandCount_Apache.pdf) | Vote centers Klagetoh (229 ballots) and Cottonwood (371); 4 early batches of 50 | Corporation Commissioner, Prop 144, U.S. Rep. CD2, State Rep. LD6, Attorney General | "matched the tabulated results with zero discrepancies" |
| [Cochise](../evidence/AZ/2026_General_HandCount_Cochise.pdf) | Vote centers 5 Benson (773) and 7 Sierra Vista (1,037); early batches, 400 ballots | A federal race, Governor, a State Senate district, Prop 144 | "compared to the machine-determined results, with 100% accuracy" |
| [Coconino](../evidence/AZ/coconino-ge/Hand-Count-Audit-Report-Secretary-State-November-3-General-Election.pdf) | Cameron Chapter House (263) and Inscription House (192); 4 early batches, 379 ballots | Attorney General, Superintendent of Public Instruction, Prop 320, U.S. Rep. CD2, State Rep. LD7 | "found zero discrepancies" |
| [Gila](../evidence/AZ/2026_General_HandCount_Gila.pdf) | Globe Elks Lodge and Whispering Pines; early batches G46 and G47 | U.S. Rep. CD2, Secretary of State, Superintendent of Public Instruction, State Rep. LD7, Prop 142 | "matched the machine determined results or were within the margins established by the Vote Count Verification Committee" |
| [Graham](../evidence/AZ/2026_General_HandCount_Graham.pdf) | Bonita/Klondyke (38) and Peridot (171); 2 early batches of 50 | Four races drawn | "no discrepancies were found" |
| [Greenlee](../evidence/AZ/2026_General_HandCount_Greenlee.pdf) | Vote Center 1 Morenci and Precinct 1 Eagle; early batch 19 | U.S. Rep. CD6, State Rep. LD19, Governor, Prop 319 | "matched the machine determined results with zero discrepancies" |
| [La Paz](../evidence/AZ/2026_General_HandCount_LaPaz.pdf) | Vote centers Parker and Salome; early batch A0011 | Secretary of State, Prop 142, State Rep. LD30, U.S. Rep. CD9 | "matched the machine tabulated results perfectly, with no discrepancies" |
| [Maricopa](../evidence/AZ/2026_General_HandCount_Maricopa.pdf) | 6 vote centers (6,801 ballots); 26 early batches of about 200 (drawn by the Libertarian, Democratic and Republican parties) | U.S. Rep., Corporation Commissioner, State Senator, Prop 316 | Differences of 3 to 7 votes in vote-center races (0.045% to 0.063%, against a 1% margin), none in early ballots: "within the variance and designated margin" |
| [Mohave](../evidence/AZ/2026_General_HandCount_Mohave.pdf) | 2 of 24 precincts; 3 early batches of 300 | Superintendent of Public Instruction, Prop 316, State Rep. LD30, U.S. Rep. CD9 | Two one-vote differences (0.09% and 0.13%), within the margin of less than 1% |
| [Navajo](../evidence/AZ/2026_General_HandCount_Navajo.pdf) | Teesto (314) and Timber Mesa Fire (234); early batches 73 and 114 (100 each) | U.S. Rep. CD2, State Senator LD7, State Rep. LD6, State Treasurer, Prop 144 | Vote centers "matched the tabulated results after justification of one ballot that was electronic adjudicated"; early ballots "no discrepancies" |
| [Pima](../evidence/AZ/2026_General_HandCount_Pima.pdf) | 3 of 126 vote centers; 14 early batches of 250 (drawn by the Democratic, Green and Republican parties) | Governor, Prop 318, U.S. Rep., State Rep. | One-vote differences in three races (0.03%): "within the variance as defined by the Arizona Secretary of State" |
| [Pinal](../evidence/AZ/2026_General_HandCount_Pinal.pdf) | 3 precincts; 14 early batches, 1,372 ballots | U.S. Rep., Prop 319, Superintendent of Public Instruction, State Rep. | "no discrepancies between the machine count and the hand count" |
| [Santa Cruz](../evidence/AZ/2026_General_HandCount_Santa_Cruz.pdf) | Vote centers 8 Rio Rico Fire Station #2 and 9 Gabilondo-Zehentner County Service Center; early batches A0133 and A0042 (50 each) | State Mine Inspector, Prop 144, State Senator LD19 and LD21, U.S. Rep. CD7 | One-vote differences from a voter who marked with slashes, which the board read as clear intent: "does not exceed the designated 1% margin" |
| [Yavapai](../evidence/AZ/2026_General_HandCount_Yavapai.pdf) | Vote centers 1 and 4, Prescott; 22 early batches (drawn Nov 6) | U.S. Rep. CD2, Governor, State Rep. LD30, Prop 142 | "matched the machine tabulated results perfectly, with no discrepancies" |
| [Yuma](../evidence/AZ/2026_General_HandCount_Yuma.pdf) | Vote centers Main Library and AWC-Wellton; 9 early batches | U.S. Rep. CD7, State Rep. LD23, Superintendent of Public Instruction, Prop 319 | No difference except one vote in one race at one vote center (0.07%) |

These counts are good evidence that the machines counted the sampled ballots correctly. They would
be stronger still if each county published, before its draw, the list of vote centers and
early-ballot batches eligible to be drawn and their machine counts, so anyone could confirm the
sample came from records fixed in advance (see
[Evidence-Based Elections](https://www.stat.berkeley.edu/~stark/Preprints/evidenceVote12.pdf)).

## 2026 audit dates

### Already happened (selections, seeds and draws)

- **Wed Nov 4**: County hand count audit draws by the parties' county representatives (Yavapai Nov 6); counts Nov 4–10. All 15 counties' reports confirm the machine results: ten found no differences, five found differences of one to seven votes in a race, all within the designated margin, so none was expanded (see the [Arizona page](states/AZ.md)). · _official ([county reports](https://azsos.gov/elections/election-information/2026-election-info); copies in the site's evidence folder)_.

### Full calendar, Nov 10 – Jan 2027

- **Nov 19**: County canvass deadline (hand counts done before it). · _official_. <https://azsos.gov/node/876>
- **Nov 23**: State canvass. · _official_. <https://azsos.gov/node/876>

## Watched pages

- <https://azsos.gov/node/876> (hand count before canvass; blocked to scripts; 0 saved copies)

