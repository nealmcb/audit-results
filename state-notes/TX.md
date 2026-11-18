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
