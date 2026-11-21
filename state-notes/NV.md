## Risk-limiting audits in Nevada

Nevada has required a risk-limiting audit after every election since 2024 (NRS 293.394, NAC 293.480
and 293.485): one state or federal contest chosen by the Secretary of State and one county contest
chosen by each county clerk. The Secretary of State posts a certificate of completion for each audit
on its [2026 election information page](https://www.nvsos.gov/elections/election-information/2026-election-information).
That site refuses automated fetches, so copies of the pages and certificates are in this site's
[evidence folder](https://github.com/nealmcb/audit-results/tree/main/evidence/NV).

Nevada's 2026 audits so far, from the certificates:

| Election | Contests | Method and risk limit | Seed | Counties; ballots audited | Result |
|---|---|---|---|---|---|
| [2026 Primary](../evidence/NV/2026%20Primary%20RLA%20Certificate%20of%20Completion.pdf) (certified June 23) | Secretary of State (REP) statewide, and one contest in each participating county | Ballot comparison, 5% | 96563554651611938493 | 17; 109 | "no variations found during the audit" |
| [2026 Churchill Special](../evidence/NV/2026%20Churchill%20Special%20RLA%20Certificate%20of%20Completion.pdf) (certified August 10) | City of Fallon, Ward 1 (NP) | Ballot comparison, 5% | 08886551305728034600 | 1; 6 | "no variations found during the audit" |

Both audits used Arlo by VotingWorks. The certificate for the November 3 general election is
expected after the county canvass on November 24.

These certificates give the seed and the number of ballots audited. Publishing the ballot
manifests and cast vote records (or their hashes) before each seed is drawn, and the list of ballots
sampled with their audited and reported votes afterwards, would let anyone reproduce the sample and
check the result (see
[Evidence-Based Elections](https://www.stat.berkeley.edu/~stark/Preprints/evidenceVote12.pdf)).
