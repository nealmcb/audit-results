---
layout: default
title: Transparency
---

# What we're learning

A running list, kept up to date as we follow the 2026 audits: what stops independent observers
from seeing the evidence, how we get around it, and what observers and states can do better.

## Obstacles

**Sites that refuse scripts.** Many election sites block automated fetches, so a scheduled
capture gets an error or a bot-challenge page instead of the content:

- Georgia's Secretary of State (audit page, news, and posted PDFs such as the batch retrieval
  list), Rhode Island's Risk-Limiting Audit Center, New Hampshire's Secretary of State PDFs,
  Clayton County, Georgia, and Citizen Portal's meeting summaries refuse outright.
- Minnesota's and Nevada's Secretary of State sites return a challenge page with a normal "200 OK"
  status, which looks like success unless the page's text is checked.
- Archive services can be blocked too: neither archive.ph nor the Wayback Machine could save
  Georgia's audit page.

**Pages built in the browser.** Some pages carry no content until JavaScript runs, so a script sees
an empty shell: Pennsylvania's Department of State newsroom, PACast, and Rhode Island's Open Meetings
Portal. A script can't tell whether a release or meeting notice has been posted.

**Announcements made only on social media or video.** Georgia posted its hashes only on X.
Pennsylvania's dice roll was streamed on Facebook and PACast, Washington's on an unlisted YouTube
video, which search tools can't find.

**Missing times and dates.** Pennsylvania's audit page gave the date of its roll but no time or
livestream link; the time appeared only in news reports on the day. Several county notices carry
no date of their own, and Fulton County's notice paired "Thursday" with November 13, a Friday.

**Pages that change on every visit.** Live results timestamps, counters (South Carolina's count of
registered voters) and rotating form labels make a page look changed every time, which buries real
changes. Our capture tool filters these out.

## Workarounds

- **Save pages from a browser**: Chrome's single-file save (MHTML) records the URL and the save time
  in the file; "Save as PDF" with headers and footers prints them on every page. Browser-driving
  agents (Claude Cowork, Claude in Chrome) can do this for a list of pages.
- **Use the agent that can see the source**: Grok searches X directly; ask it for each post's full
  status URL. Gemini watches YouTube, but only videos it can find, not unlisted ones.
- **Decode X post times** from their status IDs, which encode the posting time to the millisecond,
  rather than trusting a displayed or reported time.
- **Recordings**: `yt-dlp` can fetch a recording's metadata (title, live start time, length) and
  YouTube's automatic captions even when the video itself won't download; Facebook videos download
  directly. Captions give the time each die was called; video frames show on-screen seeds.
- **PDF metadata** gives a document's creation and modification times, though only by its maker's
  clock.
- **Email notices**: many offices email their notices (often through GovDelivery), each with a
  public web copy to cite.
- **Commit and timestamp everything**: we hash every file we hold, list the hashes in a versioned
  SHA256SUMS file, stamp it with OpenTimestamps and sign it with Sigstore (see the
  [README](https://github.com/nealmcb/audit-results#readme)). That proves when we had each file,
  which git and web timestamps can't.

## Advice for observers

- Save the audit page, news page and any posted files shortly before the draw, and note the time.
- Watch or record the roll, and note the clock time of the first and last die and of the seed being
  read back. Check that the seed later posted matches the one rolled.
- Ask, before the roll, whether the ballot manifests, cast vote records and batch tallies (or
  their hashes) have been published or at least fixed in the audit software.
- After the roll, check the list of sampled ballots or batches against the seed, and the files
  against any hashes posted.
- Keep copies of everything, with times, and have them timestamped independently.
- When writing up a recorded ceremony, link each key moment (first and last die, seed read-back,
  contest draws) at its offset in the video, so others can watch it for themselves.

## Advice for states

- **Publish the audit's inputs before the dice are rolled**: the ballot manifests, cast vote records
  and batch tallies, or at least SHA-256 hashes of them. A hash reveals nothing about the numbers,
  costs nothing, and is the only way to show the inputs weren't adjusted once the sample was known.
  Rhode Island's rule already requires the manifest two business days before its seed ceremony, and
  the batch tallies before it.
- **Choose the audited contests before the seed is rolled**, and by a method others can check.
- **Answer "number to hit" worries with blind counting**: have two teams count each batch, or each
  half of a batch, independently, rather than keeping the machine totals secret.
- **Announce the roll's date, time and livestream link on the audit page** well ahead, and post the
  seed there in text as soon as it's rolled.
- **Make random selections reproducible**: a public dice roll and published seed, not a private
  draw with a web random-number generator.
- **Keep audit pages readable by scripts and archives**: plain pages that don't block automated
  fetches, with dates on every notice. Public records shouldn't need a person at a browser to
  capture them.
- **Say what "within expected margins" means** when reporting discrepancies, and publish the
  per-batch or per-ballot comparison, not just a summary.
