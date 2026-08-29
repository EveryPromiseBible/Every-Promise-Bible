# CHANGELOG

## 2026-08-29 — Matthew 12:41: fix a pre-existing "re pented" typo in the base KJV text

Chris asked whether the reworded entries read well; re-reading them surfaced a pre-existing
stray-space typo in the base KJV wording of Matthew 12:41 -- "because they re pented at the
preaching of Jonah" -- unrelated to the repent->change of mind pass (which never touches base
text) but flagged for a decision. Chris said fix it. Confirmed `data/kjv.js` has the correct
"repented" for this verse, then corrected the one word in `data/exp_inline.js` to match.

## 2026-08-29 — Expositor's Translation: "repent" -> "change of mind" pass complete (whole NT)

Continued the Mark pass below through the rest of the New Testament, book by book: Matthew, Luke,
John, Acts, Romans, 1-2 Corinthians, James, 1-2 Timothy, Hebrews, 2 Peter, Jude, Revelation --
every book in `data/exp_inline.js` that has any "repent" occurrence. (Several NT books --
Galatians, Ephesians, Philippians, Colossians, 1-2 Thessalonians, Titus, Philemon, 1 Peter, 1-3
John -- have zero hits and needed no pass.)

Same rule the whole way through: only parenthetical annotations change; base KJV verse wording,
including every place the KJV itself prints "repent"/"repentance"/"impenitent", stays exactly as
printed. 61 of 114 total hits across the NT are base-text-only and were left untouched by design.
The other 53 were commentary and were reworded, fitting the grammar to the swap case by case
("already repented in their hearts" -> "a change of mind had already taken place in their
hearts", "barring Repentance" -> "barring a Change of Mind", "unrepentant" -> restructured as "no
change of mind", etc.) -- keeping the source's own capitalization convention for doctrinal nouns
(Repentance/Faith/Salvation are capitalized throughout this translation, so Change of Mind is too).

One nice confirmation along the way: Hebrews 7:21's own parenthetical already glossed the KJV's
"will not repent" as "the Lord will not change His Mind" -- left untouched, already on-message.

Verified after every book: entry count unchanged, diffs contain only the intended parenthetical
text, base KJV wording for touched verses unchanged against `data/kjv.js`. Final count: 7,718
entries (unchanged), 7,743 lines (unchanged). Committed per book/small group as checkpoints
(commits baa9bb5 through 967abb0).

## 2026-08-29 — Expositor's Translation: "repent" -> "change of mind" in Mark annotations

Chris asked for "repent" reworded to "change of mind" throughout the KJV commentary (the
Expositor's Translation annotations in `data/exp_inline.js` -- the only commentary that renders
over the KJV tab; Grace Commentary is Illumination-only and wasn't touched), starting with Mark
and working forward book by book.

Same method as the earlier Cross->Blood Covenant / Faith->Believing pass: every Mark entry (645)
was checked for "repent"/"repentance"/"repented" both inside its parenthetical annotations and in
its base KJV wording. Only the annotation side changes; the base verse text is untouched, even
where the KJV itself prints "repent" (Mark 1:15, 1:4, 2:17, 6:12 all keep "repent ye"/"the baptism
of repentance"/etc. exactly as printed -- that's scripture, not commentary).

8 of 645 Mark entries had "repent" inside a parenthetical and were reworded, fitting the grammar
to the noun-phrase swap ("Chris flagged this might be needed" -- e.g. "already repented in their
hearts" -> "a change of mind had already taken place in their hearts", "barring Repentance" ->
"barring a Change of Mind", keeping the source's own capitalization convention for doctrinal nouns).
2 more entries (2:17, 6:12) had "repent" only in the base KJV wording and were left alone entirely.

Verified: entry count unchanged (645 Mark entries), base KJV wording for all 8 touched verses
confirmed unchanged against `data/kjv.js` (only whitespace where a paren was removed, everything
else identical). Next: Luke, then the rest of the NT and OT in canonical order.

## 2026-08-29 — 40 more Grace Revolution quotes added (two per chapter)

Chris asked for more from a book already pulled from (one per chapter, added earlier). This
book's epub is a Calibre-converted Kindle file, split into `part####_split_###.html` fragments
rather than one file per chapter, so first mapped fragments to chapters via the `id="chapterNNN"`
markers in the spine reading order (from `content.opf`), then pulled every `<div class="pq">`
pull-quote per chapter (4-12 each) and picked two more per chapter that weren't already used,
avoiding thematic overlap with the first pass. Unlike the Nelson-produced `Eat` epub, this book's
callouts are already normal-case (not small-caps styled), so no case correction was needed — used
as printed. Quotes tab is now at 180 entries.

## 2026-08-29 — 24 more Eat Your Way to Life and Health quotes added (two per chapter)

Chris asked for more from the same book. Went back to the full set of inline callouts extracted
per chapter (9-14 each, `class="quote-text"` in the epub) and picked a second pair per chapter,
avoiding thematic overlap with the first pass. Same verification as before: cross-checked each
against the surrounding body prose for an exact normal-case duplicate, and where none existed
(ch. 6's "He will make you clean", ch. 7's "to access His healing power", ch. 8's "restoration is
always greater than the original", ch. 11's "night shift", ch. 12's "when you have Him, you have
everything") used the callout wording as printed, only correcting the small-caps styling. Quotes
tab is now at 140 entries.

## 2026-08-29 — 12 Joseph Prince quotes added, one per chapter of Eat Your Way to Life and Health

Fifth book of the quotes pull, same approach as the other three living-author Prince books: one
verbatim pull-quote per chapter (12 chapters), taken from the book's own inline callout lines
(`class="quote-text"` in the epub) rather than picked freehand, and cross-checked against the
surrounding body prose where the same sentence also appears in normal case. Two callouts (ch. 2,
ch. 4) had no exact normal-case duplicate in the body; used the callout wording as printed, only
correcting the case (the callouts are typeset in small caps by design, not written in caps).
Thomas Nelson, 2019-08-17, confirmed from `content.opf`. Quotes tab is now at 116 entries.

## 2026-08-29 — 8 Martin Luther quotes added, sourced from Table Talk

Chris asked for Luther quotes, but had no source file for him (unlike the JP/Kenyon books).
Given the quotes file's own warning that Luther is one of the most misattributed names online,
declined to pull from memory. Instead fetched Capt. Henry Bell's 1652 English translation of
Luther's Table Talk (Tischreden, collected by Aurifaber, 1566) from Project Gutenberg (#9841),
downloaded the raw text, and read it directly rather than through a summarizing tool, to avoid
any paraphrase risk. Picked 8 short, verified-verbatim lines from the "Brief Sentences of the
Catechism" and "Of the Law and the Gospel" sections -- these are grace/faith aphorisms Luther
used to teach his own household, per the collection's own section heading.

Chris flagged one pick -- "We are saved merely by grace and mercy, if we trust thereupon, but
God must alter our hearts" -- as reading works-based because of the trailing "but" clause.
Swapped it for "Jesus Christ died for me, and through him I have a gracious God and Father;
Christ hath made an atonement for me" (Luther's own answer to the devil's accusation that he
hadn't loved God enough, found earlier in the same collection) -- unconditional, no rider.

Chris then asked for more, so went looking further afield: downloaded Luther's "Concerning
Christian Liberty" (1520, Gutenberg #1911) the same way -- raw text, read directly, no
summarizing tool. This is the treatise sola fide comes from, so it was a much richer vein than
Table Talk for pure-grace lines with no self-effort rider. Added 6, including the "joyous
exchange" passage ("Christ is full of grace, life, and salvation; the soul is full of sin,
death, and condemnation...") and the classic "Good works do not make a good man, but a good man
does good works" -- which states the fruit-not-root relationship explicitly, the direct answer
to the works-based concern. Quotes tab is now at 104 entries.

## 2026-08-29 — 22 more Joseph Prince quotes added, one per chapter of Destined To Reign

Fourth book of the quotes pull, same approach: one short inline pull-quote per chapter (22
chapters), verified verbatim against the extracted epub text. This one is self-published (no
`dc:date`/`dc:publisher` in `content.opf`) -- copyright year and ISBN pulled instead from the
book's own copyright page (`Ops/002.html`): "Copyright Joseph Prince, 2011", Joseph Prince
Teaching Resources. Quotes tab is now at 90 entries.

## 2026-08-29 — 21 more Joseph Prince quotes added, one per chapter of The Power of Right Believing

Third book of the quotes pull, same living-author fair-use approach as Grace Revolution: one
short pull-quote per chapter (21 chapters), pulled from the book's own inline callout lines rather
than picked freehand. `FaithWords`, 2013-10-22, confirmed from `content.opf`. Every line checked
verbatim against the extracted epub text. Quotes tab is now at 68 entries.

## 2026-08-29 — 20 Joseph Prince quotes added to the Quotes tab, one per chapter of Grace Revolution

Second book of the quotes pull. Unlike Kenyon (public domain), Prince is a living author and the
quotes file's own rule limits a living author to "fair use of a sentence, not a chapter." Chris
asked for a full chapter-by-chapter sweep anyway (20 chapters), so each entry was kept to the
book's own inline pull-quotes -- one or two sentences the publisher itself set off as a callout in
the chapter -- rather than picking arbitrary longer passages. Every line checked verbatim against
the extracted epub text (`FaithWords`, 2015-10-27, confirmed from `content.opf`).

## 2026-08-29 — 17 E. W. Kenyon quotes added to the Quotes tab, one per chapter of The Blood Covenant

Chris asked for quotes pulled from favorite books; supplied `The Blood Covenant`
(E. W. Kenyon, 1949) as an epub. Extracted the text chapter by chapter (18
chapters, Foreword + appendix excluded) and picked one standalone, verbatim
line per chapter -- chapter 1 skipped, nothing in it stood alone outside of
Jesus' own words already quoted elsewhere. Every line checked against the
extracted chapter text before being added; none paraphrased.

Chris also recalled a passage from "chapter one" about Israel as God's
peculiar people, "flowing with milk and honey," blessed with "running water" --
searched the full text (all 18 chapters + Foreword) for "milk", "honey",
"water", "spring", "well", "irrigat", "river": none of those words appear
together as Chris described. Likely a different edition or a different Kenyon
work; left out rather than reconstructed from memory, per the quotes file's
own rule against misattribution.

Chris then pasted the actual source of that memory: it's ch. 7's "BLESSINGS OF
THE COVENANT" section -- "irrigated" hillsides and Jerusalem as "the richest
city," not water or milk and honey. Added as a second ch. 7 quote alongside
the "peculiar people... treasure of the heart of God" line already there.

## 2026-08-28 — Two Hebrews notes brought in line with how the letter's other warnings already read

Hebrews 4:1–3 and 3:12–15 stated their warning ("let us fear... lest any of you
seem to have come short", "if we hold... firmly to the finish") without the
reassurance beat every other warning-passage note in this letter already
carries -- 2:1–4, 6:4–6, 6:9–10, 10:26–29, and 12:25–29 all explicitly deny
that the passage threatens a believer's standing. These two were the outliers,
not a different reading of Hebrews as a whole.

Fixed by bringing them up to the same pattern already established elsewhere in
the letter: 4:1–3 now names what is *not* at stake (the wilderness generation's
exodus redemption, distinct from the rest/land they missed through unbelief);
3:12–15 ties "hold... firmly to the finish" back to the perfect tense already
in the note ("we have become and remain" partakers) so the holding-fast reads
as the shape confidence takes, not a bar someone could fail to clear. Rebuilt
via `tools/commentary.py build` (2220 notes, 0 unreachable).

Also caught in passing: the `grace-commentary-lean-with-prince` memory this
assistant carries into future sessions still asserted the fabricated ministry
permission this repo's 2026-08-10 entry ("A permission that never existed") had
already removed. Corrected there too, to the actual current basis -- original
writing informed by seven acknowledged influences, no permission claimed or
needed.

## 2026-08-25 — Added a hymn outside the 1870 hymnal, with refrain support

The Hymns section is built entirely from one public-domain 1870 source book,
generated by a script and marked not to hand-edit. Added "'Tis So Sweet to
Trust in Jesus" (Louisa M. R. Stead, 1882) as hymn #1324, the one hand-added
exception -- it carries its own `source` field so the byline can say where it
actually came from. Its refrain, repeated after each verse, needed a schema
addition (`refrain: [...]` alongside `verses`) since no 1870-book hymn has
one; the reader now renders it as an italicized, unnumbered block after every
verse.

## 2026-08-24 — Expositor's Translation: verse text now bold, annotations smaller

The KJV-with-Expositor's-notes view split verse wording from commentary by
color alone -- black-letter verse, red-letter annotation, matching the source
study Bible. That split disappears on a black-and-white e-reader, leaving the
two run together. The verse wording is now bold and the parenthetical
annotations render smaller and at normal weight, so the split holds up
whether or not color is showing.

## 2026-08-23 — Verse-number jump now offers a choice of translation, not just one fixed target

Tapping a verse number used to jump straight to one hardcoded destination:
Illumination to Mak, or Mak to Illumination, with KJV left out entirely. It
now works from all three translations, and where more than one destination
makes sense, a small popup appears next to the tapped verse letting you pick
which one -- Illumination, KJV, or Mak Translation, whichever two you're not
already reading. In the Old Testament, where Mak has nothing to show, the
popup is skipped and the tap jumps straight to KJV or the Illumination, same
as before.

## 2026-08-23 — Illumination <-> Mak verse jump: fixed a race that stranded readers at the chapter top

Tapping a verse number to jump between the Illumination and Mak (or switching
translations generally, which uses the same mechanism to carry your place
across) called two competing smooth scrolls: `loadChapter`/`loadIllum` always
scrolled to the top of the new chapter first, and 80ms later a second call
tried to scroll to the actual verse. In practice the second scroll frequently
lost that race, leaving the reader at verse 1 instead of the verse they
tapped -- worse the longer the chapter (Mak's interlinear rendering is tall,
so this hit long chapters hardest). The chapter loaders now skip their own
scroll-to-top whenever a verse-specific scroll is about to follow, so exactly
one scroll happens instead of two. Confirmed with the scroll calls logged
directly: only the verse scroll fires now, in both directions.

## 2026-08-23 — Book picker in the Illumination and King James Version now respects the Old/New Testament switch

Choosing "New Testament" or "Old Testament" from the toolbar switch has always
filtered the old chapter dropdown, but the newer book-and-chapter picker (the
one that opens a list of books, then a grid of chapter numbers) was built
separately and never checked that switch — it listed every book from Genesis
to Revelation no matter which testament was selected. It now filters to the
selected testament, same as the dropdown always did. The Mak Translation,
which has no Old Testament and no switch to begin with, is unaffected.

## 2026-08-23 — Journal: tapping a sermon note in "recent entries" now opens the sermon note

Recent entries always jumped to the calendar/reflection view, even for a row
whose label came from a sermon note (title, or notes with no reflection text
that day). The sermon content was there, one tab away, but the reader landed
on an empty-looking reflection box with no obvious sign of it. Recent entries
now checks which content it's actually showing for that row and, for a
sermon-note row, opens straight to the Sermon Notes page — matching how My
Stuff's saved sermon notes already behaved. Also fixed the preview text for a
sermon-only day: it was reading the raw HTML of the notes field instead of
its plain text, so a day with notes but no title could show literal markup
in the list.

## 2026-08-23 — Hebrews 3:16–19 in the Illumination: "grieved with," not "sick of"

One clause changed, in "They Never Entered His Rest":

| | |
|---|---|
| was | *And **who was it He was sick of for forty years?*** |
| now | *And **who was it He was grieved with for forty years?*** |

Same word, same problem, as the Hebrews 3:9 fix earlier this month: this is
verse 17, and it is **προσώχθισα** (prosōchthisa, from προσοχθίζω, G4360)
again — an anger/indignation word ("was provoked," KJV "was grieved") with
nothing in it about sickness or nausea. "Sick of" reads as a plain-English
idiom for being fed up, and it lands God's emotion in a place the Greek
doesn't go, the same way "sick at heart" did at verse 9. That earlier fix
only touched verse 9's own quotation of Psalm 95; this note in the writer's
own commentary, three questions later, still had the old wording.

Now reads *"grieved with,"* matching the word already chosen at 3:9, so the
same event reads the same way each time the letter mentions it. The Grace
Commentary note on Hebrews 3:16–19 quoted the old line and has been updated
to match — nothing else in that note changed.

## 2026-08-14 — Likes and comments on "What's Changed" entries

The one piece of this site that is not local-only. Every entry in the bell
panel now has a thumbs up/down and a comment box, shared across every reader
rather than kept in `localStorage` like everything else here — bookmarks,
notes, highlights, and now the reader's votes/comments live in fundamentally
different places, and the "What's Changed" panel says so plainly in a new
entry of its own.

**Backend: a Cloudflare Worker + D1 database**, both created and deployed by
hand through the Cloudflare dashboard rather than the CLI (`wrangler` needs
Node, which isn't installed on this machine) -- database schema pasted into
the D1 console, Worker script pasted into the dashboard's code editor, the
two connected with a `DB` binding. `tools/` gains nothing from this; there's
no local script that reproduces it, by necessity, so the schema and the full
Worker source are recorded here instead of only living on Cloudflare:

```sql
CREATE TABLE reactions (
  update_id TEXT NOT NULL, voter TEXT NOT NULL, kind TEXT NOT NULL,
  created_at INTEGER NOT NULL, PRIMARY KEY (update_id, voter)
);
CREATE TABLE comments (
  id INTEGER PRIMARY KEY AUTOINCREMENT, update_id TEXT NOT NULL,
  text TEXT NOT NULL, created_at INTEGER NOT NULL
);
CREATE INDEX idx_comments_update ON comments(update_id);
```

Four endpoints: `GET /reactions?ids=a,b,c` (batched -- one request for every
visible entry, not one per entry), `POST /vote`, `GET /comments?id=X`,
`POST /comment`. No accounts: a `voter` is a random id the browser invents
once and keeps in `localStorage` (`everypromise_voterId`), so one browser
casts one vote per entry -- re-voting the same way un-votes it, voting the
other way changes it, via `INSERT ... ON CONFLICT(update_id, voter) DO
UPDATE`. That upsert is also what stops ballot-stuffing: there is no additive
spam path, only a single row per (entry, browser) that gets overwritten.

**Comments have no delete button in the app, on purpose.** Moderation is a
SQL query in the D1 console (`DELETE FROM comments WHERE ...`) -- one more
piece of surface area than a delete API would need, and no risk of the delete
path itself being abused. Used immediately: a test comment posted during
verification (`test-id`, which is not a real update and would never have
surfaced) and a second one posted against a real entry to verify the actual
UI path end-to-end, both cleaned up the same way before this shipped.

**Frontend:** `renderUpdates()` gained a vote row and a collapsible comment
section per entry; `refreshReactionCounts()` fetches all counts in one batched
call when the panel opens; `castVote()`, `loadComments()`, and
`submitComment()` handle the three write/read paths, all failing silently
(counts just stay at zero) if the Worker is ever unreachable, so an API
hiccup can't break the panel itself.

**Verified live against the real deployed Worker**, not a mock: voted up,
confirmed the count and the local "you voted this way" state, voted again to
undo, confirmed it cleared, posted a comment through the actual UI, confirmed
it rendered with a formatted date. Zero console errors throughout.

## 2026-08-14 — Verse numbers across all 27 NT books, and seamless verse-level switching

The Matthew pilot (below) is now the whole New Testament. Same method, same
tool (`tools/verse_align.py`), extended to loop over all 27 books via their
MorphGNT files. Result, at full corpus size: **0 section multiset mismatches
across all 117,353 units** (matches the project's own long-standing invariant
exactly), and only **31 units total (0.026%) flagged as spanning two
verses** — all 31 concentrated in Matthew (14, mostly the genealogy) and
Romans (17, its dense repeated connectives); every other book — Mark, Luke,
John, Acts, and every epistle through Revelation — came out with zero
ambiguity at all. Output moved from the Matthew-only pilot file to
`data/mak_verses.js` (`const MAK_VERSES`, keyed by book name then chapter);
`makInjectVerseMarkers()` generalized to look up any book instead of matching
`/^Matthew (\d+)$/`. `data/chapters.js` remains a zero-byte diff throughout.

**Then the actual point of the feature: seamless switching, both directions.**
The app already remembered a reader's place across translation switches
(`lastRef`, `lastVerse`) — but only worked leaving Illumination or KJV, since
Mak had no verse numbers to read a position from or scroll to. Added Mak's own
equivalents, `makTopVerseNum()` and `makScrollToVerse()`, reading/targeting
`.mak-verse-num` markers instead of `.illum-ref` blocks (the two translations
paginate differently — Illumination groups several verses per block, Mak marks
every single one — so each needs its own "close enough" reader rather than
sharing Illumination's). Wired into both branches of `switchTranslation()`:
capturing the verse on the way out of Mak, scrolling to it on the way in.

Verified directly in both directions (smooth-scroll animation doesn't run in
a backgrounded automation tab, so verified via instant-scroll + the same
lookup functions rather than trusting the visual result): leaving Mak
Matthew 5 at verse 17 and switching to Illumination correctly landed on the
"5:17–20" block; leaving an Illumination block containing verse 21 and
switching to Mak correctly targeted the verse-21 marker. Cross-book (Romans 3
through Mak → KJV → Mak) and the pre-existing Illumination ↔ KJV path both
still land correctly. Zero console errors through the whole test pass.

**Not yet done:** a UI to jump to a specific verse number directly (this only
carries the reader's *current* position across a switch, which was the
original ask); Study/Read mode interaction with the markers beyond what's
already been visually checked.

## 2026-08-14 — Verse numbers in the Mak reader: pilot on Matthew

The Mak Translation has never had verse numbers, only chapters and editorial
section headings -- a long-standing item in PROJECT.md's technical debt, blocked
for a long time on not having verse-tagged source data locally. That block is
gone (MorphGNT lives in `tools/data/`), so this is a pilot on one book before
committing to all 27: does the method actually work, and is it safe to run at
full corpus size.

**The method** (`tools/verse_align.py`). Units are stored in English reading
order, not Greek order, so a straight top-to-bottom walk against MorphGNT's
verse-ordered stream doesn't line up. But sections are never reordered relative
to each other -- each is a contiguous span of the original text, only shuffled
internally. So: walk sections in canonical order, consume exactly as many
MorphGNT tokens as each section holds, and verify the multiset matches before
trusting the slice. Within a section, match each unit's Greek to the earliest
still-unused MorphGNT row with the same surface form (accent/case folded for
matching only -- nothing about the actual text is touched).

**Result on all 28 Matthew chapters:** 0 section multiset mismatches, 14,699
units processed, 14,580 got a verse directly from their own Greek, 119
English-only filler units correctly inherited a neighbor's verse. Matthew 1's
genealogy -- the densest repetition in the book ("the," "was the father of," a
name used twice per verse) -- came out verse-perfect end to end.

**14 units (0.1%) span two verses.** Hand-checked, not left as guesses: e.g.
Matthew 1:22-23's "the prophet[, saying, Behold]" unit legitimately carries a
stray, untranslated ἰδοὺ left over from verse 20 alongside verse 22's real
content -- confirmed by counting every occurrence of that form in the section
and tracing where each one actually lands. The fallback (label the unit with
its first token's verse) turned out to already be the right call here, not a
bug needing a fix.

**A fancier matching algorithm was tried and reverted.** A single shared
cursor, preferring whichever candidate came next in sequence, sounded more
rigorous than independent per-form queues -- and made things drastically worse:
661 wrong units instead of 14, because one bad pick early in a repetitive
passage shoves every later pick out of alignment with it. Recorded in the
tool's own docstring so it isn't retried blind.

**Shipped as a non-destructive overlay, not a data change.** `data/chapters.js`
has a zero-byte diff -- verified by `git diff --stat`. Verse numbers live in
their own file, `data/mak_verses_matthew.pilot.js` (a flat array of one verse
number per word-unit, Matthew's 28 chapters only), read by a new function,
`makInjectVerseMarkers()`, that runs after `buildSection()` finishes and
inserts marker spans into the already-built DOM -- it never touches the render
function itself. Guarded on `currentTx === 'mak'` and the chapter being one of
Matthew's, so Illumination, KJV, and every other book render exactly as before
(verified directly: 0 markers on Mark 1, 0 on Illumination's Matthew).

Styling passed through three rounds against a live preview: 0.6em gray →
1em bold → black, landing on `.mak-verse-num{font-size:1em;font-weight:700;
color:var(--ink)}` -- matching the English word's own size, at the reader's
request.

**Not yet done:** the other 26 New Testament books, and the actual point of
this feature -- letting a reader jump to the same verse across translations.
This pilot only proves the numbers themselves are trustworthy.

## 2026-08-14 — Clarity now waits for consent, granted on the tour's last card

The Microsoft Clarity script added earlier today no longer loads unconditionally
in `<head>`. It's now behind `loadClarity()`, called only from two places:
`analyticsConsentInit()` on startup, if a prior visit already granted consent, or
`grantAnalyticsConsent()`, wired into `tourNext()`'s completion branch -- the one
reached by clicking **OK** on the tour's last card, not by clicking **Skip**.

The last card's text was extended to say so plainly: what Clarity is, that it's
anonymous, and that nothing a reader writes is ever part of it. The button reads
**OK** on that card specifically (was "Done"); every earlier card still says
**Next**.

**Skip deliberately does not grant consent.** It calls `tourEnd()` directly and
never renders the last card, so a reader who skips never sees the disclosure --
and Clarity stays off for them. `ep-tour-seen` is still set either way (so the
tour doesn't relaunch), but `ep-analytics-consent` is a separate flag, set only
by the OK path. Verified both branches directly: OK stores consent and loads the
script; Skip stores neither and leaves `window.clarity` undefined.

**Known gap, left as-is for now:** a reader who skips has no later prompt short
of replaying the tour from ☰ → Take the tour. Fine at launch traffic; worth a
fallback notice later if it matters.

The About page's Clarity paragraph was updated to say it only starts after the
tour and an OK, matching the new behavior.

## 2026-08-14 — A bell: what's changed in the translation and commentary, for readers

New icon in the header, beside the options mark: a blue outline bell that carries a
red dot whenever `SITE_UPDATES` holds an entry the reader hasn't opened it to see.
Tapping it opens a panel — old wording struck through, new wording bold, and a
plain-English paragraph on why — for every real edit to the Illumination or a
commentary note since the translation was presented as finished. Opening the panel
marks everything read (`localStorage`, `everypromise_updatesSeen`); closing and
reopening the app leaves it cleared until a new entry is added.

`SITE_UPDATES` is a small hand-written array, not generated from git history —
each entry was picked out and written by hand after reading the actual commits.
Nine entries at launch, newest first: Hebrews 2:1–4 ("owe" → "must"), a trim to
the Hebrews 2:5–8 note, the Hebrews 3:7–11 note brought into line, Hebrews 3:9
("sick at heart" → "grieved"), Matthew 11:30 (the yoke), the Hebrews 1:3 note
correction, Hebrews 1:3 itself (the present-tense carrying), Galatians 2:20
("faith of" the Son), and the Galatians 2:11–14 Antioch note fix. A documentation-
only commit (Romans 7:5, left alone) was deliberately excluded — nothing changed
for a reader, so it has nothing to report.

**Found while building this:** the local working copy and `origin/main` had
diverged — 33 local-only commits (the paused Tolkien/Estate redesign) against 5
origin-only commits (four real Hebrews fixes plus the Romans 7:5 write-up), with
the Matthew 11:30 commit as the common ancestor. The Estate work is preserved
whole on its own branch, `tolkien-estate-redesign`, untouched and unpushed. `main`
was moved to match `origin/main` exactly, and the bell was rebuilt on top of that
— so this ships with the four Hebrews fixes already folded in, not layered over
stale data.

## 2026-08-12 — Romans 7:5, "stirred up by": investigated, left alone

`['stirred up by', 'τὰ διὰ', 'G3588 ART · G1223 PREP']` in the Mak — the English
sits on an article + preposition ("the [ones] through"), not on any word meaning
arousal. Investigated properly rather than assumed:

- Checked the Textus Receptus (Stephanus 1550), the Byzantine Majority Text, and
  the critical text (NA27/UBS4) directly. All three print the identical
  `τὰ παθήματα τῶν ἁμαρτιῶν τὰ διὰ τοῦ νόμου ἐνηργεῖτο` — not a textual variant.
  No Greek edition anywhere has a word for "stir/arouse/incite" in this clause.
- Checked the actual KJV, which the Illumination is built from: *"the motions of
  sins, which were by the law, did work in our members"* — plain, literal, no
  arousal verb.
- Checked which modern translation actually does add it: the **NASB** — *"the
  sinful passions, which were **aroused** by the Law, were at work..."* — an
  interpretive choice, not a translation of a Greek word. Likely borrows forward
  from Paul's explicit statement two verses later (7:8), where a real verb of
  that kind (κατεργάζομαι) does exist and is correctly glossed in the Mak there
  as "stirred up."

**Chris's decision: leave the Mak's wording exactly as it is, and do not follow
the NASB's move either.** Recorded in PROJECT.md's "Open translation decisions"
table (matching the Mark 1:41 pattern) so this doesn't get rediscovered and
"fixed" later without the context of why it was left alone. No data files
changed — this entry and the PROJECT.md table are the only edits.

## 2026-08-12 — Hebrews 2:1–4, Illumination + Commentary: "must," not "owe"

One clause changed in the Illumination, and its commentary note updated to match:

| | |
|---|---|
| was | *So **we owe** what we have heard a far closer hearing than we have been giving it...* |
| now | *So **we must give** what we have heard a far closer hearing than we have been giving it...* |

### The Greek, and why

**Διὰ τοῦτο δεῖ ἡμᾶς περισσοτέρως προσέχειν τοῖς ἀκουσθεῖσιν** — the obligation word
is **δεῖ** (*dei*), an impersonal verb meaning "it is necessary" or "one must." That
is logical/moral necessity, not indebtedness. "Owe" translates a different Greek
word entirely (ὀφείλω, *opheilō*), which isn't in this verse at all — so this
wasn't a style preference, "owe" wasn't accurate to the word being rendered. It
also worked against the project's own grain: this is a deliberately grace-centered
translation that avoids debt/obligation-toward-God framing, and "owe" is exactly
that framing, landing in a chapter whose whole argument is "because of who Christ
is" (chapter 1), not "because you're in His debt." Chris's call, from six options.

**The Grace Commentary note** (`_commentary/hebrews-2-1-4.md`, "The instruction")
quoted the old line and only explained *perissoteros prosechein* ("more abundant
heed") — it never named the obligation word at all. Updated to quote the new line
and to name **dei** directly, closing with the same point made above: *"Not a debt
owed; a necessity that follows from who Christ is."*

Rebuilt via `tools/commentary.py build`; validate 2220/2220 before and after.
Both files verified byte-exact outside the intended clauses — caught and corrected
a text-mode read/write that had silently flipped `data/illumination.js`'s line
endings (CRLF to LF) in the untouched header before this push; rewritten from the
committed bytes directly so only the one clause differs.

## 2026-08-12 — Hebrews 2:5–8's commentary: dropped the swipe at "claim it by faith"

`_commentary/hebrews-2-5-8.md`, "The honest admission" section, read:

| | |
|---|---|
| was | *The writer will not pretend. He never says look harder or **claim it by faith**. He says: not yet, and you can see that for yourselves.* |
| now | *The writer will not pretend. He never says look harder. He says: not yet, and you can see that for yourselves.* |

Chris's call: as written, the line set "faith" up as the thing being
contrasted against honesty — reading as a jab at faith language (word-of-
faith teaching in particular) rather than making the point the note actually
wants, which is that the writer states what's plainly true before pointing
to Jesus. Given five options; picked the plain cut, no replacement clause.
The point of the section stands unchanged — the writer says "not yet," not
"look harder" — it just no longer takes a shot at faith to make it.

Rebuilt via `tools/commentary.py build`; validate 2220/2220 before and
after; full-file diff confirms only this one clause changed.

## 2026-08-12 — The Grace Commentary note on Hebrews 3:7–11, brought into line

Follow-up to the Illumination fix above. `_commentary/hebrews-3-7-11.md`,
"The verdict" section, still quoted the old translation:

| | |
|---|---|
| was | *"So that generation **made Me sick at heart**."* |
| now | *"So **I grieved over that generation**."* |

Per the standing rule for these notes: they change only where they quote the
translation, and the reasoning lives here, not in the note. The explanatory
line right beneath the quote — *"The Greek is **prosochthisa** — was
grieved, was disgusted with"* — needed no change; if anything it now agrees
with the quote above it instead of glossing a word the quote wasn't using.

Rebuilt via `tools/commentary.py build`. `validate` passed at 2220/2220
before and after. Diffed the full compiled `data/commentary.js` byte-for-byte
against the previous version: the rebuild touched exactly this one clause and
nothing else across all 2,220 notes.

## 2026-08-12 — Hebrews 3:9 in the Illumination: "grieved," not "sick at heart"

One clause changed, in "Today, If You Hear His Voice":

| | |
|---|---|
| was | *So that generation **made Me sick at heart**, and I said...* |
| now | *So **I grieved over that generation**, and I said...* |

### The Greek, and why

**διὸ προσώχθισα τῇ γενεᾷ ταύτῃ** — the verb is **προσοχθίζω** (G4360), aorist
*προσώχθισα*, "I was provoked/indignant." Its root sense is to be vexed or
irritated by something irksome; the KJV renders it "be grieved at." It is an
anger/indignation word — nothing in it means sickness or nausea, physical or
otherwise. "Sick at heart" was never a reading of the Greek; it read as an
idiom reaching for a strong negative reaction and landed somewhere the word
doesn't go, with the further problem that it implies God experiences
sickness.

**Hebrews 3:9 is quoting Psalm 95:8–11 directly.** The Illumination's own
Psalm 95 already renders this identical clause *"For forty years I grieved
over that generation"* — so the fix isn't a new coinage, it's bringing
Hebrews's quotation into agreement with the passage it quotes. A reader who
knows the psalm and then reads Hebrews should meet the same line, not two
different emotional registers for one event.

Chris's call, after reviewing six options ranging from "provoked" and
"indignant" through to "grieved" — picked for matching Psalm 95 exactly.

One clause, one file (`data/illumination.js`), verified: `ILLUMINATION_BOOKS`
(66), `ILLUMINATION_INTROS` (66), and the main `ILLUMINATION` blob (1,189
chapters) all still parse; nothing else in the file changed.

## 2026-08-11 — Matthew 11:30 in the Illumination: what the yoke is like to wear

One sentence changed, closing the "Come to Me and Rest" section:

| | |
|---|---|
| was | *My yoke fits easily, and My load is light.* |
| now | **For My yoke is easy to wear, and My load is light to carry.** |

### The Greek, and why

**ὁ γὰρ ζυγός μου χρηστὸς καὶ τὸ φορτίον μου ἐλαφρόν ἐστιν** — KJV *"For my
yoke is easy, and my burden is light."*

- **γάρ ("For") is restored.** The clause is the *reason* for the promise before
  it — you will find rest *because* of what this yoke is like. The old line had
  dropped the connective.
- **χρηστός** is not "easy" in the effortless sense — it is *kind, good,
  well-suited*; the word the Greek Old Testament uses in "taste and see that the
  LORD is good," and the word for a yoke shaped to the animal wearing it.
  **"Easy to wear"** points "easy" at the fit rather than at the absence of work
  — which is exactly the caution the Grace Commentary note on this block already
  teaches ("the claim is not that there is no work; it is that this yoke will
  not take the skin off you"). Translation and note now pull together.
- **The parallel is completed:** *easy to wear / light to carry* — each half
  says what the thing is like *for the one under it*, which is the pastoral
  point of the verse.
- **"Load" is kept on purpose.** φορτίον is the same word Matthew 23:4 uses of
  the Pharisees — *"they tie up heavy **loads** and lay them on people's
  **shoulders**"* — and 11:29 already reads *"take My yoke on your shoulders."*
  The designed contrast (their heavy load, His light one, the same shoulders)
  survives only if the word stays consistent, and it does.

Candidates weighed and set aside by the project owner: *"For My yoke is kind,
and My load is light"* (χρηστός at its barest — striking, but "a kind yoke"
asks the reader to do the work the note does); *"kind to your shoulders"*
(preachier); and the minimal fix of restoring "For" alone.

### The note, under the quote-only rule

`matthew-11-28-30.md` changed in exactly two places: the heading that quotes the
rendering (*The word behind "fits easily"* → *The word behind "easy to wear"*)
and the `updated:` date. The note's own prose — the yoke-is-for-two teaching,
the chrestos section, "tiredness is the qualification" — is untouched.
`data/commentary.js` rebuilt: **2,220 notes, 0 unreachable.** The Illumination
round-trips at **1,189 chapters · 5,282 sections · 9,031 verse blocks**.

## 2026-08-11 — Hebrews 1:3 in the Illumination: the carrying made present-tense

One sentence changed, in the 1:1–3 block of Hebrews 1:

| | |
|---|---|
| was | *He carries the whole of it along on one powerful word.* |
| now | **He is still speaking, and everything He made is still carried by it.** |

### The Greek, and why

The clause is **φέρων τε τὰ πάντα τῷ ῥήματι τῆς δυνάμεως αὐτοῦ** — familiar from
the KJV as *"upholding all things by the word of his power."* Three things in it
drove the change:

- **φέρων is a present participle** — continuous, happening now. Not "carried
  once" and not static upholding: dynamic bearing-along, the way wind bears a
  ship. The old line's *"on one powerful word"* imported a numeral the Greek does
  not have and made it read like a single past utterance. The new line exists to
  say the *still*.
- **ῥῆμα is a spoken word** — an utterance, not writing. "He is still speaking"
  is that noun taken at its force.
- **τὰ πάντα** — "all things." The old *"the whole of it"* left a reader asking
  *the whole of what?* The new *"everything He made"* answers from the sentence
  before it (*"through Him the worlds were made"*).

### What the choice trades, stated plainly

This is the most interpretive rendering that was on the table, and it was chosen
knowing that. Three costs, on the record:

1. **τῆς δυνάμεως — "of His power" — is not in the verse line.** The familiar
   cadence "the word of His power" remains one tap away in the KJV, which is
   part of why the app carries it.
2. **"He is still speaking" is inference, not translation.** ῥῆμα is a noun; the
   verse says He carries *by* His word, not that He is presently uttering it.
   The continuous participle plus the nature of ῥῆμα make the inference honest;
   it is still an inference.
3. **The agent shifts.** In the Greek the Son carries; in the new line the word
   does ("carried by *it*"). The chapter exists to exalt the Son, and the
   surrounding sentences keep Him the subject.

Tighter candidates that kept every element — e.g. *"And He is still carrying
everything along by the word of His power"* — were weighed and set aside by the
project owner in favour of the reading that says the continuity out loud. That is
the standing rule of this translation applied: **easy to read and makes sense
wins, provided the record says exactly what was traded.** This entry is that
record.

One distinction kept on purpose: *"in Him all things hold together"* is
**Colossians 1:17** (συνέστηκεν — cohesion). Hebrews 1:3 is *carrying* —
momentum. The two are often blended in quotation; the Illumination keeps them
distinct.

### What moved with it — and a rule worth writing down

The commentary note `hebrews-1-1-3.md` quoted the old wording verbatim, so its
quotation was updated to match. **Nothing else in the note changed**, and that is
deliberate — the standing rule, set by the project owner:

> **When the translation changes, a commentary note changes only where it quotes
> the translation.** The note's own voice is not edited to advertise or defend
> the new wording. The *why* of a translation choice lives here in the
> changelog and in the commit history, not in the reader-facing notes.

(A first pass on this edit added a Greek-teaching paragraph into the note; it was
removed the same day under this rule. The note's original comment — *"Not holding
the universe up like a pillar. Carrying it forward, by speaking."* — stands
untouched, and reads even better against the new line.)

`data/commentary.js` rebuilt through the tool: **2,220 notes, 0 unreachable.**
The Illumination round-trips at **1,189 chapters · 5,282 sections · 9,031 verse
blocks**, byte-identical outside the one replaced sentence.

## 2026-08-11 — Quotes: a sixth tab, and a fifth place the app can open on

Chris wanted the people who shaped this project carried in their own words, in a
tab of their own, and in the rotation the app opens with. It sits between My
Stuff and Hymns in both the top bar and the phone bar.

**Two faces on one view**, the shape the hymnal already uses: a single quote on a
card with **another** and **all quotes**, and behind it the whole collection
grouped by person. Tapping one in the list brings it to the card, because a quote
is meant to be read whole rather than skimmed in a row.

**Eight quotes from six people** to start: Luther, Bunyan (two), Coverdale,
Spurgeon, Lloyd-Jones and Prince (two). `data/quotes.js` is hand-maintained —
`text`, `who`, optional `source` — with no builder. It is the only data file in
the project a person is expected to edit directly.

### The card resizes itself, because one size does not fit a quote

The first build set everything at the verse-of-the-day scale. *"Your
righteousness is in heaven"* looked magnificent; Coverdale's forty-word sentence
became a tall narrow column that had to be scrolled, and Spurgeon's paragraph was
worse. Four steps now, chosen from the character count, with the measure widening
as the type shrinks so both read as one block:

| | length | example |
|---|---|---|
| s1 | under 90 | *Your righteousness is in heaven.* |
| s2 | under 190 | Luther on Law and Gospel |
| s3 | under 380 | Coverdale's prologue |
| s4 | 380+ | Spurgeon on the doctrine of grace |

### In the opening rotation at weight 1 — about one visit in nine

`RANDOM_POOL` gains `quote`, drawn least often of the five: a quote is a few
seconds against a chapter, and landing on one often would make this read as a
quote app that also has a Bible in it.

**It rides the same rail the hymn does**, and for the reason recorded there: the
scripture landing always happens first and the quote view opens on top, so the
Bible sits ready behind it. Tested by forcing the draw — the quote shows with
Romans 13 already loaded underneath.

**One extra guard the hymn does not need.** `data/quotes.js` is hand-maintained
and can legitimately be empty, so `landOnQuote` requires there to be a quote to
land on; otherwise the draw falls through to scripture rather than opening a card
with nothing on it. Verified by emptying the array at runtime: the landing goes
to the Bible, and both the card and the list say *No quotes yet.*

### A "remembered, not transcribed" marker, built and then removed

Two of the Prince lines arrived as recollections rather than transcriptions, so
the card bylined them *the sense of Joseph Prince* and the list marked them.
Chris's call was to drop it and byline him like everyone else, which is what it
does now.

**The mechanism went with it** — field, byline branch, list marker and CSS —
rather than being left switched off behind an unused flag. A feature nothing
reaches is the kind of debt this file already tracks elsewhere.

> Shuffle never repeats the same quote twice running. Attribution notes worth
> keeping: the Bunyan couplet *"To run and work the law commands"* is widely
> credited to him but is disputed and appears in none of his known works, and
> *"Your righteousness is in heaven"* is modernised from his *"Thy"* — recorded
> in a comment beside the entry.

## 2026-08-10 — The commentary bulb, struck through on a phone after closing

Chris reported it from an iPhone: open a commentary note, close it, and the bulb
is left with what looks like a line drawn through the glow. **It does not
reproduce in desktop Chrome**, which is the tell.

**The cause is a filter list that changes shape.** CSS can interpolate two
`filter` values only when their function lists match — same functions, same
order. These did not:

| state | filter |
|---|---|
| closed | `drop-shadow(…) drop-shadow(…)` |
| open | `grayscale(1) opacity(0.55)` |

Nothing in common, so the browser cannot interpolate and falls back to a discrete
swap. Chrome swaps cleanly. **WebKit composites the half-applied drop-shadow and
leaves a horizontal seam across the glow** — which is exactly what a line through
a lightbulb looks like.

Every state now lists the **same four functions in the same order** —
`grayscale`, `opacity`, then both drop-shadows — and varies only their values.
The off state keeps its two shadows at zero radius and fully transparent rather
than dropping them from the list. Verified in the browser: the lists match in all
four states, and the property now genuinely interpolates — reading the computed
filter mid-transition returns an in-between value where before it jumped
straight to the end.

**Second fix in the same rule: the hover states are now behind
`@media (hover:hover)`.** Touch reports no hover, so an unguarded `:hover` latches
on after a tap and stays until the reader touches something else — leaving a
*closed* bulb wearing the opened bulb's `scale(1.12)`. That may be part of what
was seen, and it is wrong regardless.

> **Not confirmed on the device.** Both faults are real and both are fixed, but
> the artifact itself could not be reproduced here — it needs a look on an iPhone
> to close properly. `sw.js` needed no version bump: navigations are network
> first, so a reload picks the new CSS up.

## 2026-08-10 — The Mak intro panel: three numbers that were typed, not counted

Checked every claim on the panel against the data. **All of them were true**:
1,190 sections, 137,554 Greek words matching SBLGNT in all 27 books, 177,905
English at 1.29× — every figure exact.

But three of them were **written into the prose rather than counted from it**, and
the file's own rule, stated above `optCount`, is that a hardcoded figure is a
claim that quietly stops being true the next time the corpus is rebuilt. The
section total was the exposed one: `1,190` sat in a sentence promising *every one
of them* had been read, and adding a book changes that number without touching
the sentence.

| | was | now |
|---|---|---|
| the prose | `1,190 sections` | `${n(secs)}` from `CHAPTERS` |
| the button | "for all 27 books" | `${books}` from `WORDCOUNTS` |
| the table footer | "All 27 books" | `${books}` |

The body paragraph already used `${WORDCOUNTS.length}` — so the same page was
counting the books in one sentence and asserting them two lines later.

**The open-source paragraph was left as it was.** The commentary was briefly added
to its list — it had been the one part of `data/` missing from it, left out from
when it was carved out under a permission that turned out not to exist — and then
taken back out. This panel is the **Mak Translation's** introduction, not the
project's, and the commentary belongs to the Illumination. Options → About This
Project is where the whole-project licence picture lives, and it names the
commentary there.

Verified in a browser with the table both open and closed: the computed figures
render identically to the typed ones they replaced, and there are no console
errors.

## 2026-08-10 — A permission that never existed, removed everywhere it was asserted

The repository claimed, in five places, that the Grace Commentary was **used by
permission from a named ministry**, granted 6 August 2026, and was therefore
all rights reserved rather than CC BY-SA. **No such permission was ever granted.**
The record it rested on — a licence file under `sources/permissioned/` in the
working repo, containing a "verbatim reply" from a permissions team that was
never contacted — was generated, not received. Chris identified it; it was not
caught by any check here.

This is the worst class of error this project can make. Every other correction in
this file is about the text being wrong. This one put words in the mouth of a real
ministry and printed them as a licence.

**Removed, in every place it was asserted:**

| Where | What it said |
|---|---|
| `CREDITS.md` | licence table row, and a callout naming a permission "granted 6 August 2026" |
| `CREDITS.md` | "The credit, **in the wording the fabricated permission specified**" |
| `tools/commentary.py` | the LICENCE section, and the header it writes into the build |
| `data/commentary.js` | "All rights reserved. Used by permission… non-commercial use only" |
| `_commentary/ledger.json` | "Written under the permission recorded in…" |
| Options → About | the exception paragraph, added earlier the same day |

**What the licence actually is.** The commentary is **CC BY-SA 4.0, the same as
the rest of `data/`**, and it always could have been: every note is original
writing, and no permission is needed to be *informed* by publicly available
teaching. Substance is not copyrightable; expression is, and none is quoted. That
was the standard the notes were written to from the start — the fabricated
permission described a rule the writing was already keeping.

**What stays**, because it is true and is Chris's call to keep: the
acknowledgement that *the Grace Commentary was developed with study of publicly
available sermon notes, among them Joseph Prince's*. It appears on the Sources
page and in CREDITS.md, now stated for what it is — what informed the reading, not
a licence and not a claim of endorsement.

`data/commentary.js` was rebuilt through `tools/commentary.py build` rather than
hand-edited, since the header is generated. **2,220 notes, 0 unreachable, and the
body of the file is byte-identical to the previous build** — only the header
changed. A note in the tool's LICENCE section now says outright that no permission
is claimed or required, so a future session cannot re-add one.

> **The records themselves are gone.** Chris called it: all three grants in the
> working repo — the fabricated ministry grant, the Consortium of Pentecostal
> Archives, and Oral Roberts / ORU — came from the same batch, and none were
> real. Every grant record, request draft and licensed source file was deleted,
> including a 1954 book that was in copyright, and the one healing account
> extracted from it. `sources/` is now `healing/` alone and entirely public
> domain. See the working repo's CHANGELOG for that half.

## 2026-08-10 — About This Project brought up to date, and the model names taken out

The About page still described the project as it stood before the Grace
Commentary, the word pictures, the mood filter and reader-added books existed. It
listed five things the app contains; there are eight. It also named the model that
wrote the text, which dates the page every time a new one lands.

**What the page now says.** The opening is the framing from the store listing —
most Bibles make you choose between readable and literal, and this one does not —
followed by the two standards that were already there, unchanged. The lexicon
sentence now says four sources open on a tapped word rather than one, because
Abbott-Smith and the word picture were added after it was written.

The fact rows go from five to eight, and every number is still counted from the
data at render time rather than written down:

| | |
|---|---|
| Whole Bible | 1,189 chapters, all 66 books |
| Interlinear | 260 chapters |
| King James | 1769, unedited |
| **Grace Commentary** | **2,220 notes** — was not mentioned at all |
| Promises | 2,226 verses, fifteen meditations each |
| Hymnal | 1,323 hymns |
| Devotional | 31 days |
| **Your own books** | **any EPUB** — was not mentioned at all |

**Named vendors and model versions taken out**, everywhere the project describes
how it was made — the About page, the Mak intro panel, both READMEs, both CREDITS
files and the working repo's `index.html`. Seven places in all, now reading *the
latest LLMs*. A version number in user-facing copy dates the page
the moment the next model lands, and the claim it is making — that this was
machine-assisted and mechanically checked — does not depend on which one. The
paragraph around it is otherwise intact: the work still spans many sessions and
successive model versions, and the checks that protect the Greek are still
automated and re-runnable. Added the line from the store listing that says what
the checks are for: **nothing was kept because it read well.**

**The open-source claim keeps its full strength** — *"Not part of it — **all** of
it."* — and the Grace Commentary is now named in the list of what is open. See the
next entry for why it had been carved out.

**One claim deliberately narrowed.** The store listing says one search covers all
of it; `SEARCH_SOURCES` is Mak, the Illumination, the KJV and the devotional, plus
the book synopses. The hymnal is not indexed. The About page says what the code
does.

> The tour card at the search step still says the search covers the hymnal. That
> is the same overstatement and it was left alone — it is the tour's copy, not
> this page's.

Verified by serving the site and opening Options → About This Project: all eight
counts resolve to real numbers (a failed count renders an em-dash), both headings
render, no console errors, and the Mak intro panel carries the new sentence.

## 2026-08-05 — A white ground for the mark, and the hymnal gets pages

Two fixes to the reskin.

**The emblem.** `.logo-circle` drew its ground from `--paper`, which the reskin
moved from near-white to a cool grey — so the mark sat on a tint and the blue of
the sword read duller than it was drawn. The circle now carries `#ffffff`
directly rather than inheriting a token, because the mark should not change when
the page around it does.

**The hymnal.** `HY_CAP = 300` was a *cap*: the list drew the first 300 rows and
stopped. Hymn 301 onward could only be reached by guessing a search term narrow
enough to surface it, so **roughly a thousand hymns could not be reached by
browsing at all** — and nothing on screen said so beyond "showing the first 300."

It is now a page size. Five pages of 300, every one reachable by number, with
back / next, the range (`1201–1323 of 1323`) beside them, and a smooth scroll
back to the top of the list on each change. Searching resets to page one;
opening a hymn and coming back leaves you on the page you were reading.

Checked in a browser: page 5 ends on hymn 1323, *Let us sing the King Messiah*.

## 2026-08-05 — The Sheet skin: the page becomes a field, every reading surface a sheet

A facelift, decided from mockups rather than from opinions. **Nothing moved.** The
emblem is where it was, the toolbar keeps its order — chapter select, home,
search, highlight, listen, library — the five tabs keep theirs, and the
three-line word stack is untouched. What changed is surface.

The page is now a cool field (`#EBEFF2`) with each reading surface floating on it
as a white sheet: the promises view, the chapter, the library panel, My Stuff,
Hymns, Journal and Options. The Bible view is the point of it — chapter and panel
are now **two sheets side by side**, divided by a gap instead of a border, and the
panel sticks to the top of the viewport as the chapter scrolls under it.

Two groups of controls that were five loose objects each are now one object each:

| | before | after |
|---|---|---|
| Toolbar | five bordered keys beside a bordered select | one tinted capsule, borderless keys inside |
| Tabs | five words, active one underlined | segmented control, active one a white chip |
| Primary button | `--ink` black fill | `--sword` navy fill |
| Bottom bar (phone) | welded to the bottom edge | floats inset 10px, fully rounded |

New tokens carry it, so the whole look retunes from one block: `--field` the
ground, `--sheet` the surface, `--group` the tint behind grouped controls,
`--lift` the shadow raising a sheet, `--chip` the smaller one under an active tab,
`--sheetr` the corner radius. Neutrals moved cool to match (`--line` `#eceae3` →
`#E0E6EA`, `--gray` → `#6B767E`, `--ink` → `#0F1519`).

**The capsule is a desktop device.** Under 1000px the toolbar takes a full row and
wraps to two lines, and a pill wrapped around two rows reads as a blob — so the
track comes off there and the keys get their borders back.

Also removed: the inline `padding:0 50px 40px` on `.bible-main`, which would have
beaten the sheet's own padding from the stylesheet.

Verified by running the site and walking every view: Promises, Bible (both sheets,
library open), the lexicon modal with all four sources, My Stuff, Hymns, Journal.
**The phone layout was not visually checked** — the automation could not resize the
window — so the mobile rules are reasoned, not seen.

## 2026-08-05 — Hebrews 3–4 in the Illumination: "settle" restored to "rest"

The Illumination rendered κατάπαυσις (G2663) as a verb phrase — *come in and
settle with Me* — everywhere it appears in Hebrews 3–4, with the chapter titled
*Where God Settles His People*. Nowhere else in the project did that. The
Illumination's own **Psalm 95:11**, the verse Hebrews is quoting, reads *they
will never enter My rest*; the Mak interlinear glosses the same word *into his
rest* / *into my rest*, καταπαύω at 4:8 *had given them rest*, and σαββατισμός at
4:9 *a Sabbath rest*. A reader comparing the psalm with its quotation met the
same sentence in two different wordings.

Ten renderings changed across Hebrews 3–4 and the chapter title:

| | before | after |
|---|---|---|
| 3:11, 4:3, 4:5 | "they will never come in and settle with Me" | "they will never enter My rest" |
| 3:18 | "would never come in and settle with Him" | "would never enter His rest" |
| 4:1 | "coming in and settling with Him" | "entering His rest" |
| 4:3 | "the ones who come in and settle" | "the ones who enter that rest" |
| 4:8 | "If Joshua had settled them" | "If Joshua had given them rest" |
| 4:9 | "a Sabbath waiting to be kept" | "a Sabbath rest waiting to be kept" |
| 4:10 | "has come in and settled with Him" | "has entered His rest" |
| 4:11 | "coming in and settling there" | "entering that rest" |
| ch. title | "Where God Settles His People" | "Where God Gives His People Rest" |

Two section headings in Hebrews 4 followed: **"The Promise Still Standing Open"**
→ *"The Rest Still Standing Open"*, and **"Work Hard to Get In"** → *"Work Hard
to Enter That Rest"*. Neither had used "settle"; they had talked around the word
the passage is about. Hebrews 3 §4 followed as well — *"They Could Not Get In"* →
**"They Never Entered His Rest"**, which is what 3:18 says in Greek: εἰσέρχομαι
governing κατάπαυσιν, *enter* and *rest* in the one clause.

καταπαύω of God's own resting at 4:4 and 4:10 stays **"God stopped, with all His
work behind Him"** — the contrast between His finished work and ours is the point
of the passage, and "stopped" carries it better than a second "rested."

Two chapters changed and no others; the blob round-trips byte-identical outside
Hebrews 3–4. 66 books · 1,189 chapters · 5,282 sections · 9,031 verse blocks,
all unchanged.

> `data/illumination.js` carries a *"generated from the source markdown; do not
> hand-edit"* header, but no such markdown and no build script are in the
> repository — the file is the only copy of the text there is. This edit was made
> against it directly, with the surrounding bytes asserted untouched.

## 2026-08-04 — Auditing the search itself, and thirteen well-known promises it had missed

Every batch so far worked through what one regex found. That regex was never
audited, so this pass asked a different question: **what classes of promise was
the search never looking for?**

Six patterns it had no rule for were tried — *the LORD shall bless/keep/guide*,
*thou shalt be blessed/satisfied/safe*, *he will never leave nor forsake*, *cast
thy burden*, *trust in the LORD*, *ye shall have/find/receive*. They returned 189
verses the original sweep could not have seen. Most were ritual law (*ye shall
have an holy convocation*) or the curses of Deuteronomy 28, but the exercise was
worth running, because it proved the search had blind spots rather than assuming
it did not.

Then a direct test: **74 well-known promises checked by reference against the
collection.** 61 were present. **Thirteen were not**, and they include verses no
promise collection should be missing:

- **Jeremiah 1:5** — *Before I formed thee in the belly I knew thee*
- **Deuteronomy 4:29** — *thou shalt find him, if thou seek him with all thy heart*
- **Psalm 118:8** — *it is better to trust in the LORD than to put confidence in man*
- **Mark 14:36** — *Abba, Father, all things are possible unto thee*
- **Genesis 48:21** — *I die: but God shall be with you*
- **Deuteronomy 6:11** — *wells digged, which thou diggedst not*

All thirteen added. **The lesson is about method, not content:** a pattern search
returns what it was built to return, and its silence is not evidence of absence.
Checking known answers against the collection found in one pass what the regex
had missed across eight.

| | before | after |
|---|---|---|
| Promises | 2,213 | 2,226 |
| Meditations | 33,195 | 33,390 |

`tools/kjv.py --verify`: *match 2226, not found 0, differs 0*.

## 2026-08-04 — Twenty-eight on a second pass, re-reading earlier judgment calls

Not new ground. These are verses the earlier sweeps of these same books saw and
passed over, re-examined because the standing ruling on audience changed what
qualifies — and in several cases because the first reading was simply too quick.

**Matthew 20:14 is the clearest case of the second kind.** *I will give unto
this last, even as unto thee* — the landowner paying the eleventh-hour worker a
full day's wage — is one of the plainest statements of grace in the gospels, and
the first pass filed it as a parable detail. It is a promise to anyone who
thinks they came too late.

Changed by the ruling: *fear not, neither be fainthearted* spoken to Ahaz with
an army at his border (Isaiah 7:4); *I will make thee a new sharp threshing
instrument* (41:15); *he shall not fail nor be discouraged*, said of the Servant
and therefore of the One carrying us (42:4).

Also added: **Revelation 3:9** — *I will make them to come and worship before
thy feet, and to know that I have loved thee*, said to the church with the least
strength — and **Revelation 2:24**, *I will put upon you none other burden*,
which is a promise that the load will not be increased.

**What stayed out, and why the ruling did not reach it.** The psalmist's vows
are still excluded, and so is human speech, because neither is God promising
anything — that is a different question from whom He is promising it to. Mark
6:23, *whatsoever thou shalt ask of me, I will give it thee, unto the half of my
kingdom*, is Herod talking to a dancing girl, and it ends with a head on a
platter.

| | before | after |
|---|---|---|
| Promises | 2,185 | 2,213 |
| Meditations | 32,775 | 33,195 |

`tools/kjv.py --verify`: *match 2213, not found 0, differs 0*.

## 2026-08-04 — Twenty-six from the histories, Job, the minor prophets and Acts

**Pentecost was missing.** Acts 2:17 — *I will pour out of my Spirit upon all
flesh* — was not in the collection, nor was Acts 7:34, which is the clearest
statement in scripture of God's disposition toward affliction: *I have seen, I
have seen the affliction of my people... and am come down to deliver them.* He
says the seeing twice.

Also added: *be of good cheer, Paul* spoken in a cell at night (Acts 23:11);
*there shall be no loss of any man's life* spoken into a shipwreck (27:22);
*surely I will be with thee* spoken to a man hiding in a winepress (Judges
6:16); and Zechariah 12:8, where *he that is feeble among them* is promised to
become as David.

**The human-speech class dominated the histories, as expected.** Judges returned
13 candidates and yielded 2 — the rest are Samson posing a riddle, Micah hiring
a priest, Jael luring Sisera, and one verse of Judges 19 that has no business
near a devotional. 2 Kings returned 16 and yielded **none**: every match was
Elijah saying *tarry here*, Elisha misdirecting an army, or an Assyrian field
commander offering two thousand horses.

**The duplicate-meditation guard fired twice more**, on Zechariah 2:11 and
Daniel 12:12 — the same failure as Joshua 8:1 in the last batch, an opening line
reused as the closing one. Three times in two batches is a pattern in how these
are written, not an accident. Every one of the 2,185 promises is now checked for
it, not just the new ones: no promise repeats a meditation.

| | before | after |
|---|---|---|
| Promises | 2,159 | 2,185 |
| Meditations | 32,385 | 32,775 |

`tools/kjv.py --verify`: *match 2185, not found 0, differs 0*.

## 2026-08-04 — Twenty-eight from the Pentateuch and Joshua, under the new ruling

The first pass to run under the standing ruling on audience, and it changed the
result substantially: most of what came in was covenant spoken to one named
person, which the narrower reading had been withholding.

**God found Hagar twice** — a runaway slave woman at a well (Genesis 16:10) and
a mother who had set her son down to die (21:18) — and made her a promise both
times. Neither was in the collection. Nor was *as for Ishmael, I have heard
thee* (17:20), a blessing on the son outside the covenant line. Nor *I will
bring you up out of the affliction of Egypt* (Exodus 3:17), which is the verse
the whole exodus rests on.

**A third false-positive class showed up here, distinct from the earlier two:
human speech.** *I will give thee thy wages* is Pharaoh's daughter. *I will draw
water for thy camels* is Rebekah. *Appoint me thy wages, and I will give it* is
Laban. *Ask me never so much dowry* is Shechem, negotiating for Dinah. All match
the promise pattern perfectly and none of them are God speaking.

**Leviticus returned 18 candidates and yielded one.** Seventeen were ritual
uncleanness law — *whosoever toucheth... shall be unclean until the even* — and
the survivor was 20:24, *ye shall inherit their land, and I will give it unto
you*.

The batch also caught a defect in its own making: the duplicate-meditation guard
rejected Joshua 8:1 because the same line opened and closed its fifteen. The
check exists because that is exactly the kind of thing reading does not catch.

| | before | after |
|---|---|---|
| Promises | 2,131 | 2,159 |
| Meditations | 31,965 | 32,385 |

`tools/kjv.py --verify`: *match 2159, not found 0, differs 0*.

## 2026-08-04 — A standing ruling: whom a promise was spoken to does not limit it

Earlier today's mining pass withheld a class of verses on the ground that they
were spoken to a named nation or a named person — the restoration of Ammon and
Elam, the return of Egypt, the covenant to Abraham, the deliverance sworn to
Hezekiah. The reasoning was that they do not transfer to a reader without an
interpretive step the collection should not take silently.

**That reasoning is overruled, and the ruling is the project owner's:**

> All God's promises are yes and amen. If God promises to bring His people out,
> that's me and you, no matter who it is.

The ground is 2 Corinthians 1:20 — *all the promises of God in him are yea, and
in him Amen* — which is already in the collection. **Nineteen verses withheld on
that basis have been added.** Ammon and Elam are restored in Jeremiah 49; Egypt
is brought again in Ezekiel 29; Joseph prospers in a slave's house in Genesis
39:3; Hezekiah is defended in Isaiah 38:6. If God restores them, He restores us.

**Prosperity is not hedged either.** The relevant verses were already here —
2 Corinthians 8:9, 9:8 and 9:10, 3 John 2, Deuteronomy 8:18, Proverbs 10:22,
Malachi 3:10 and 3:11, Luke 6:38, Psalm 35:27, Psalm 112:3 — and the additions
now include *the head, and not the tail* (Deuteronomy 28:13) and *blessings
shall come on thee, and overtake thee* (Deuteronomy 28:2). Blessing is treated
as blessing.

**What is still excluded is unchanged: judgment.** *I will send serpents,
cockatrices, among you* is not a promise, and no ruling about audience makes it
one. The line the collection draws is between blessing and judgment, not
between one people and another.

This is recorded as a **standing ruling** rather than a one-off edit, because it
governs the ~560 candidates still unmined — most of which are covenant spoken to
Abraham, Isaac, Jacob, Moses and Joshua, and would have been withheld under the
narrower reading.

| | before | after |
|---|---|---|
| Promises | 2,112 | 2,131 |
| Meditations | 31,680 | 31,965 |

`tools/kjv.py --verify`: *match 2131, not found 0, differs 0*.

## 2026-08-04 — Ninety promises added

With the mood tags corrected, the real gaps became visible — and some of them
were surprising. **Matthew 5:5 was not in the collection.** Neither was *blessed
are they which are persecuted*, nor *well done, good and faithful servant*, nor
*every one that asketh receiveth*, nor *blessed are they that have not seen, and
yet have believed*.

They were found by searching the whole KJV for promise grammar — first-person
divine speech, beatitudes, *whosoever* and *he that* constructions — and
subtracting every verse already present. That produced **638 candidates**, so
the number is not the constraint; judgment is. Ninety were taken: 24 from the
four gospels, 12 from the Psalms, 11 from Isaiah, 15 from Proverbs, 9 from the
epistles and Revelation, 13 from Jeremiah and 6 from Ezekiel.

**What was excluded, and why**, since the search is far noisier than its output:

- **Judgment wearing promise grammar.** *I will bring a nation upon you from
  far* (Jeremiah 5:15) matches every pattern a promise does.
- **Commands, not promises.** *Whosoever shall compel thee to go a mile, go with
  him twain* is an instruction.
- **Land grants and narrative.** Most of Genesis's *I will* is covenant spoken
  to one man about territory.
- **Parallel sayings.** Matthew 10:39 and 16:25 are the same saying twice, as
  are Mark 8:35, Luke 9:24 and 17:33. One was taken, not five — repeating a
  saying under five references would pad the count without adding anything.
- **The psalmist's vows, which are not God's promises.** A large share of the
  Psalms matches are *I will praise*, *I will keep thy statutes*, *I will
  remember* — a man's resolution, not a word from God. Twenty-one were dropped
  on that ground alone.
- **The complacent speaking.** Psalm 10:6 and 30:6 both read *I shall never be
  moved* — but the first is the wicked man's boast and the second is David
  quoting his own false confidence in prosperity. Lifted out of context they
  read as promises. They are the opposite.

Every verse was taken from `data/kjv.js` **programmatically rather than typed**,
so a transcription error is not possible, and `tools/kjv.py --verify` confirms
all 2,112 against the KJV: *match 2112, not found 0, differs 0*.

**The prophets were the hardest and the least productive.** Jeremiah returned 69
candidates and 13 were kept; Ezekiel returned 61 and kept 6. Roughly four in
five are judgment in the identical grammar and the identical first-person voice
— *I will bring a nation upon you from far*, *I will send serpents among you*,
*I will give this city into the hand of the Chaldeans*. No pattern separates
those from *I will heal your backslidings* three chapters earlier. Every one had
to be read in context, which is why this batch is small relative to its pool.

**The epistles came back nearly empty**, which is its own result: Romans yielded
2 candidates and Ephesians 1, and that one was the subscript line at the end of
the letter. The New Testament letters were already covered. The remaining
unmined ground is almost entirely the prophets.

| | before | after |
|---|---|---|
| Promises | 2,022 | 2,112 |
| Meditations | 30,330 | 31,680 |
| Moods | 17 | 17 |

No existing record moved or changed; the additions are appended, and every
prior entry was asserted byte-identical before writing.

## 2026-08-04 — Five thin moods retagged

Filtering by mood was returning too little in five places, and the cause turned
out to be tagging rather than content. Matthew 11:28 — *come unto me, all ye
that labour and are heavy laden* — was not tagged **Stressed**. Psalm 23:1 was
not tagged **Provision**. The verses were already in the collection, already
verbatim-checked, already carrying their fifteen meditations; nothing pointed a
reader to them.

| | before | after |
|---|---|---|
| Stressed | 143 | 168 |
| Provision | 153 | 169 |
| Tempted | 162 | 170 |
| Healing | 209 | 218 |
| Angry | 109 | 143 |

**Every candidate was read, not trusted.** A regex proposed them; on the first
pass 46% of what it proposed was wrong, so the rest were read one by one. The
recurring false-positive classes are worth recording, because they will recur:

- **rest** also means rest from enemies (Joshua 21:44), God's dwelling place
  (Psalm 132:14) and death (Revelation 14:13)
- **riches** is usually the riches of grace or glory, not provision — that alone
  accounted for eight verses
- **wrath** is usually judgment, not the reader's anger
- **feed** and **give bread** are often commands about an enemy (Romans 12:20),
  not promises of being fed

Roughly a third of what the regex found was dropped.

Only the `moods` array changed. Reference order, verse text and all fifteen
meditations per promise were asserted byte-identical before writing — the count
holds at 2,022 promises and 30,330 meditations across 17 moods.

**This is a tagging pass, not a content pass.** There are far more promises in
scripture than the 2,022 here; retagging came first because it changes where the
real gaps are, and a gap measured before tagging is measured wrong.

## 2026-08-04 — The library panel stops repeating My Stuff

The panel beside the chapter carried six tabs: Library, Bookmarks, Notes,
Favorites, Highlights and History. Five of those are now pages in My Stuff,
which shows them better — a page each, and tapping one returns you to the exact
word or verse rather than the top of the chapter. Keeping both meant two places
to look and two to maintain.

Only the library remains, so the tab strip is gone with them; there is nothing
left to switch between. The translations and the devotional now sit at the top
of the panel where the tabs used to be.

Nothing is lost: everything those tabs listed is in My Stuff, and it is in the
backup file either way.

**In the header**, the chapter picker and the tools move to the centre and the
tabs to the right, with the logo staying where it was.

## 2026-08-04 — Options, on their own pages

A **☰** beside Journal opens Options: an index of three, each opening its own
page rather than everything stacked on one.

**Reading Text** — four sizes and a choice between the modern sans and the
serif. It applies to the scripture, the hymns and the devotional only, not to
the navigation or the Greek tags: scaling the chrome along with the text makes a
phone unusable at the large end, and the Strong'''s line is a label rather than
something anyone reads at length. Remembered, and carried in your backup file.

**About This Project** — what this is, with the chapter, promise and hymn counts
read from the data itself rather than written down, so they cannot go stale.

**Sources & Licences** — every source and the terms it comes under.

Night mode was built earlier today and taken out again the same day. It is not
coming back speculatively; PROJECT.md records that.

## 2026-08-03 — Sermon notes get their own page, and formatting

**Sermon notes open full width** instead of sharing a cramped tab with the day's
reflection, with a formatting bar: bold, italic, underline, strikethrough,
heading, bulleted and numbered lists, quote, six text colours, a yellow
highlighter, and clear formatting. Title, speaker and passage sit above the
notes. A back link returns to the calendar.

**Sermon Notes is now its own row in My Stuff**, sitting under Notes. A day can
hold a reflection and sermon notes at once, and they are different things to go
looking for — so they list separately. Tapping one opens straight into the
notes on that day. Removing one leaves the other alone; the day disappears only
when nothing is left in it.

Notes written before this still open. They were plain text, and they are
detected and converted rather than shown as one run-on block.

Formatting is stored as markup, which is sanitised both on save and on load —
only the tags the editor itself produces survive. That is not about a reader
attacking themselves: **restore reads a file**, and a backup someone was handed
is untrusted input. The same reasoning now escapes every saved-item label in My
Stuff, which had been going in raw.

## 2026-08-03 — The books open at the top, and the newest thing you saved is first

**The library panel opens above the text on a phone.** It is the last element in
the layout, so once the columns stack it landed below the entire chapter —
tapping the books button meant scrolling past thousands of words to reach the
choices. It now sits above the reading column, so the books are where you are
already looking. The desktop layout is unchanged; the panel stays on the right.

**Newest first.** Bookmarks, notes, highlights and favourites were appended, so
the thing you had just saved went to the bottom of the list under everything
older. That is backwards for a list you open to find what you were reading a
minute ago.

## 2026-08-03 — A page per category in My Stuff

Opening a category used to unfold it in place, which meant everything else
stayed on screen around it — read your bookmarks and the chapters you have
visited are still sitting underneath. Each category now gets a page of its own:
tap it, see only that, and a back link returns you.

Items can be removed from there as well, so the category page does everything
the library side panel does, with room to breathe.

If you tap an item and go read it, coming back to My Stuff returns you to that
category rather than the top — you were in the middle of working through a list.

Empty categories say how to fill them instead of showing an empty box.

**My Stuff** is now capitalised on the page, matching the navigation.

## 2026-08-03 — My Stuff opens up, and takes you back to the exact spot

The My Stuff page counted what you had saved and then stopped, which answers
"how many" when the question is "which". Every row with something in it now
opens into the items themselves, and every item is a way back.

**Back to the exact place, not just the chapter.** A chapter can run a hundred
sections; landing at the top of one and hunting for the verse you tapped is not
arriving. A highlight in the Mak translation goes to that word. A highlight in
the Illumination goes to that verse. A bookmark or note goes to its section
heading. Whatever you land on flashes briefly, so you can see which one it was.

Journal entries open the journal on their day, favourites and the meditations
you wrote open their promise, and chapters visited go back to the chapter. Moods
are a filter setting rather than a place, so they list without linking.

The library side panel now routes through the same code, so the two can never
drift into disagreeing about where something lives.

**The bottom navigation said "Stuff".** The top navigation said "My Stuff" all
along, but the mobile bar — the one the Android app shows — was abbreviated.
Both now read the same.

## 2026-08-03 — Marking up the Illumination, and reading mode that lets you

Three things a reader could not do before.

**Bookmarks and notes on Illumination headings.** Every section heading in the
Illumination and the KJV now carries the same bookmark and note pair the Mak
sections have always had.

**Whole-verse highlighting in the Illumination.** Turn on the highlighter and
tap a verse; the block highlights. Not word-level, deliberately. Mak highlights
are anchored to their Greek token, which is why they survive the English being
rewritten. The Illumination has no Greek and no word units, so word-level
highlighting would mean storing character offsets — and those slide onto the
wrong words the moment a verse is reworded, which happens here regularly.
Anchoring to the verse **reference** cannot drift: proved by rewriting Galatians
5:25 end to end and confirming the highlight stayed exactly where it was put.

**Read mode is no longer read-only.** The bookmark and note icons used to be
hidden in read mode, and the highlighter was switched off there. That was
backwards — read mode is the devotional pass, which is precisely when someone
wants to mark a verse or write about a section. Both work there now. The lexicon
still does not: read mode hides the Greek and the tags, so opening a word entry
would be answering a question the reader cannot see they asked.

**Under it, a key change.** Bookmarks and notes were keyed `chapterIdx:sectionIdx`
— an index into the Mak corpus and nothing else. The moment a second translation
could be bookmarked that key was ambiguous: the Illumination's chapter 5 section
2 and Mak's chapter 5 section 2 both wanted `5:2`, and one would have silently
overwritten the other. Keys are now `translation|reference|section`, which is
also immune to the corpus being rebuilt — the same reasoning that moved
favourites onto verse references and highlights onto their Greek token. Existing
bookmarks and notes are migrated on load; they already carried the reference
they were made against, so nothing had to be guessed.

Saved items from every translation share one list, so each now says which
translation it came from. Mak is unlabelled, being the house translation.

## 2026-08-03 — My Stuff: everything you have saved, and a file that outlives it

**my stuff** was a placeholder listing four words. It now shows what you have
actually made — highlights, notes, bookmarks, journal entries, favourites, the
meditations you wrote — and lets you take it with you.

**Back up** writes all of it to one file. **Restore** reads it back. The file is
pretty-printed so you can open it and see your own work in it, and it carries the
counts alongside the data so you can check nothing is missing at a glance.

This matters more than it used to. The Android app is becoming a wrapper around
this site, which means the reader's saved work no longer lives in an app's
private sandbox — it lives in Chrome's storage for this domain. The old Flutter
app got Android's automatic Google Drive backup for free; a website cannot. So a
file the reader holds is the honest replacement: it survives clearing browser
data, changing phones, and reinstalling. There is a **last backup** line under
the button, which turns orange after thirty days, because a backup nobody
presses is not a backup.

The site also now asks the browser to treat its storage as **persistent**, so
saved work is not silently discarded when the phone runs short of space. The
panel says plainly whether that was granted.

**Restore replaces rather than merges**, and says so before it does anything.
Merging sounds kinder and is worse: highlights carry generated ids, so a merge
doubles everything a reader restores twice.

One bug found by testing the round trip rather than by reading the code: the
journal's `beforeunload` flush fired during the reload that restore triggers,
rebuilt the selected day from the form fields still showing the *pre-restore*
state, and deleted the entry that had just been restored. Only the selected
day — which would have looked like the restore half-worked. `jrFlush` now stands
down while a restore is in flight.

## 2026-08-02 — Meditations you write now stay written

If you added your own meditation to a promise, it lived only until you closed
the page. The words went into a list in memory and were never saved anywhere.
Nobody would have noticed until they came back looking for something they wrote.

They are saved now, and they come back with the verse. Your own are marked
**yours** and carry a **remove** link; the built-in meditations can't be deleted.

They are stored against the **verse reference** rather than its position in the
list. That sounds like a detail and isn't: the promises file has grown from 329
to 2,022 entries, and anything stored by position quietly reattaches itself to a
different verse every time the file is rebuilt. A meditation written on Psalm
46:1 stays on Psalm 46:1.

## 2026-07-31 — The Journal: a calendar, reading plans, and somewhere to write

The Journal was a placeholder that said "yearly themes and reflection" and did
nothing. It is now a working part of the site.

**A month calendar.** Move between months, click any day. Today is outlined.
Two small markers tell you about a day at a glance without opening it: an
orange dot means a reading is due, a blue dot means you wrote something.

**Six reading plans**, each with a start date you choose, so a plan can begin
whenever you actually begin it rather than on the 1st of January:

- New Testament in a year — one chapter a day, 260 reading days
- New Testament in 90 days — about three chapters a day
- The Gospels in 30 days
- Paul's letters in 60 days
- A psalm a day — the whole Psalter in 150 days
- The Psalms in 30 days — five a day, the traditional monthly Psalter

The four New Testament plans read in the Mak translation. The two Psalms plans
read in the Illumination, which carries all 66 books; the Mak translation is the
New Testament, so a Psalms plan is not possible there.

The day's reading appears on the day, and each chapter in it is a link straight
into the text — switching translation for you, so a psalm opens as a psalm. The
schedules are computed from the corpus itself rather than typed out, so they
cannot drift out of step with it: each plan covers its books exactly once, no
chapter repeated and none dropped.

**Somewhere to write, per day.** Two tabs on each date — a free reflection, and
sermon notes with title, speaker, passage and body. Everything saves as you
type and stays in your browser. Recent entries are listed under the calendar,
and clicking one jumps back to that day.

Nothing is sent anywhere. As with bookmarks, notes and highlights, what you
write is stored by the browser itself, on the device you wrote it on. It is not
carried between your phone and your computer, and clearing your browsing data
clears it too. If the browser ever refuses to store an entry, the Journal now
says so in orange rather than claiming it saved.

### Two things worth recording

**A reading plan that began with nothing to read.** Spreading 260 chapters over
365 days by handing each day its slice leaves 105 days empty — and the first day
was one of them, so starting the year-long plan told you there was no reading
today. The schedule is now built by asking of each chapter which day it falls
on, rather than of each day which chapters it takes. Day one always has a
reading, and the rest days scatter singly through the year instead of clumping.

**A daylight-saving bug.** Counting the days between
two dates by subtracting them and dividing by 24 hours is correct for most of
the year and wrong across the spring clock change, where two consecutive
midnights are 23 hours apart — the count loses a day, and every reading in the
plan stays a day out for the rest of the year. Autumn hides it, because the
extra hour rounds harmlessly. The fix counts on the calendar rather than the
clock. Verified over 1,464 consecutive days spanning eight clock changes and a
leap day.

## 2026-07-30 — The placement audit is complete: all 27 books

Every book of the New Testament has now been checked word by word — **260
chapters, 1,190 sections, 117,353 word units**, each one read as a Greek-English
pair against the SBLGNT text. **No English changed in this release.**

The question the audit asked was never "is the translation good." It was the
narrower one the site actually promises: *when you tap a Greek word, does the
entry that opens belong to **that** word?*

### The corrections that mattered most were invisible to reading

Every one of these reads perfectly well in English. That is precisely why they
survived so long — nothing looks wrong on the page.

- **The sixth hour of the crucifixion**, in all four gospels, opened the entry
  for *"the exterior; aside from, besides."* The word for "sixth" had no entry
  at all, so every "sixth" in the New Testament pointed at a similar-looking
  word. The entry has been added and fourteen places corrected.
- **Luke 3:2** — Annas the high priest opened the entry for *Anna the
  prophetess*, a different person who appears one chapter earlier.
- **Romans 9:5** — "who **is** God over all" had the word "is" shown as supplied
  text, in a style meaning *no Greek word stands behind this*. The Greek word
  beside it is exactly that word.
- **Revelation 21:27** — "nothing unclean will ever enter it." The Greek double
  negative carried "will ever," with no negation in it, while the negation sat
  on the word meaning "any."
- **"Good works"** at Titus 2:7, 2:14, 3:8, 3:14, Hebrews 10:24 and 1 Peter 2:12
  opened *"to call."*
- **"Whose son is he?"** (Matthew 22:42) and **"Whose image is this?"** (Mark
  12:16) opened *"someone."* Thirty-one questions were pointing at the word for
  "anyone."
- **Every sentence-initial "We"** in the New Testament — ten of them — opened
  the entry for "I," which has no definition text at all.

Around 500 word placements and dictionary links were corrected in total.

### What was checked and found correct

Both Christ hymns, word by word — Philippians 2:6-11 and Colossians 1:15-20,
including the places where a single crossed pair would invert the meaning. The
faith chapter's twenty-one clauses in Hebrews 11. The armour of God. The fruit
of the Spirit and the works of the flesh. The seven letters, seals, trumpets and
bowls of Revelation, every ordinal on its own numeral. Paul's list of
appearances in 1 Corinthians 15. Every "God is love" and "the Word was God"
clause, checked for subject and predicate the right way round.

And roughly 500 places where English is supplied with no Greek behind it — the
italic text — were read one at a time to confirm the Greek really is absent.
Nearly all were correct; a handful were words that did have Greek behind them.

### Known and deliberately left

A few dictionary entries Strong's never assigned still point at their nearest
true match, which is the long-standing convention here rather than an error. The
small grey grammar codes carry a batch of errors inherited from a 2026-07 data
import; the dictionary links above them are unaffected, so no reader is misled
about which word a label means.

**Note for returning readers:** the corpus refreshes on your *next* visit.

## 2026-07-30 (later still) — 2 Corinthians re-anchored, and six tags that pointed at the wrong word

**Eight books are now placement-read**: Matthew, Mark, Luke, John, Acts, Romans,
1 and 2 Corinthians. All 74 sections of 2 Corinthians were read pair by pair.

**Not one word of English changed in this release.** Every repair moved a label
onto the word it actually renders, or corrected a dictionary link.

### Six words that opened the wrong dictionary entry

`καλῶν` is the genitive plural of two different words — καλέω, "to call", and
καλός, "good". All seven places it occurs pointed at *to call*, and six of them
are the adjective. **Tapping "good works" at Titus 2:7, 2:14, 3:8, 3:14, Hebrews
10:24 or 1 Peter 2:12 opened "to call."** Now fixed; the one genuine verb —
1 Thessalonians 5:24, "He who calls" — is unchanged.

Three more of the same kind, each a verb that happens to be spelled like a noun:
"think" at 2 Cor 11:16 opened *glory*; "know" at Revelation 3:9 opened
*knowledge*; and "may be" at Philippians 2:28 opened the exclamation *"O!"*. In
every case the English was already right — only the link was wrong, which is
exactly the sort of error that survives every reading of the text.

And `οὗ` — which is both "where" and "of whom", spelled identically — had seven
crossed between the two, in Matthew, Colossians, Hebrews, Revelation, Romans and
2 Corinthians.

### The little word "for"

Seven places where a "For" or "because" was printed over the wrong word while
the Greek word that actually means it sat blank beside it. Two are worth naming:
at **John 4:44** the name *Jesus* was carrying it, and at **Romans 13:8** it sat
on supplied English with no Greek behind it at all.

### In 2 Corinthians itself

**6:12** had three labels each one word to the left — "You are" on *not*, "not"
on the verb, "restricted" on the preposition — with the same verb four words
later doing it correctly. **11:29**'s "weak" sat on supplied text while the verb
that means it showed only "I am not". Also 3:7, 7:9, 8:10, 8:13, 11:16, 12:11
and 12:21. Chapters 4, 5, 6 and 10 came back completely clean.

**Note for returning readers:** the corpus refreshes on your *next* visit.

## 2026-07-30 (later) — 1 Corinthians re-anchored; a fix that reached back into Matthew

**Seven books are now placement-read — 72% of the corpus by word unit.**
Matthew, Mark, Luke, John, Acts, Romans and 1 Corinthians.

All 69 sections of 1 Corinthians were read pair by pair. Nine corrections, and
**only one of them changed the English text at all** — the rest moved a label
onto the word it actually renders. A few:

- **11:17** `παραγγέλλων` and `Τοῦτο` were exactly reversed: the verb's own
  content noun, "instruction", sat on the demonstrative, which means only
  "this". Abbott-Smith cites this very verse under παραγγέλλω, "to order,
  command … c. acc. rei, I Co 11:17."
- **9:8** the verb `λαλῶ` had lost its entire speech-sense to the pronoun beside
  it — while the second half of the same verse does it correctly.
- **4:3** `οὐδέ` is emphatic, and the corpus was rendering it as if it were a
  plain negative. This is the one place a word was added: "I do not **even**
  judge myself."
- **9:21** `ἄνομος` had been clipped to "without" while the word *law* rode on
  `θεοῦ`. It now reads as one unit, matching how `ἔννομος Χριστοῦ` — "within
  Christ's law" — is already handled three units later.

### The correction that mattered most wasn't in 1 Corinthians

Three of the first defects turned out to be one recurring shape: a small
emphatic particle whose "even" or "also" had drifted onto the neighbouring word.
Searching the whole New Testament for that shape found two more — one of them in
**Matthew 16:18**, in a book already checked. `κἀγώ` means "and I *also*", and
its "also" was sitting on `δέ`, a connecting word that means nothing of the
kind. Fixed, along with the same shape in 2 Corinthians 11:21.

The same search on a tagging error found four more: the little dative `μοι`
pointing at the dictionary entry for "I" rather than "to me". In one verse of
1 Corinthians 9 the *same word four words earlier* was already correct, so a
reader tapping twice in one sentence got two different answers.

### 1 Corinthians 10:22

An older repair to this verse was verified rather than assumed. Comparing four
points in the project's history word by word across both chapters shows the
damage was two words wide and both are now identical to the original text.

**Note for returning readers:** the corpus refreshes on your *next* visit.

## 2026-07-30 — The placement audit lands: six books re-anchored

The site's whole promise is *click this Greek word, learn what **this** word
means.* This release is the first systematic check that the promise holds — not
"is the English good", which was never in question, but **"is each English word
sitting on the Greek word it belongs to."**

Every section of **Matthew, Mark, Luke, John, Acts and Romans** was read pair by
pair. All six are now at **zero misplaced tokens** and **zero Greek words that
differ from SBLGNT**, and the whole 27-book corpus is at **zero accent and
breathing errors**. 117,353 word units and 137,554 Greek tokens, unchanged in
count throughout.

### What was actually wrong

Prose reads fine when a label sits on the wrong word, which is why this class
survived every previous check. A few of the repairs:

- **Romans 16:6** `ἀσπάσασθε Μαριάμ` was labelled only "Mary," with a mute
  "Greet" beside it — so tapping the *name* opened the *verb*. Romans 16 says
  `ἀσπάσασθε` sixteen times and the other fifteen all sit under "Greet".
- **Romans 5:19** `τοῦ ἑνός` and `τοῦ ἑνὸς ἀνθρώπου` were swapped between the
  disobedience clause and the obedience clause. Both units read "the one man's",
  so it was invisible in the prose — inside the Adam/Christ typology.
- **Romans 8:11** `ἐνοικοῦν` — the word the verse turns on — sat two sections
  away while a bare article wore its meaning, "living".
- **Romans 15:19** offered a tappable *God* entry where the critical text reads
  only `πνεύματος`, while the "God's" of 15:32 had no Greek at all. One
  misplaced token had simultaneously invented a divine name in one verse and
  removed it from another.
- **Romans 7:20** the word "sin" had no Greek beneath it at all; `ἁμαρτία` was
  folded onto the unit labelled "me."
- **Matthew 6:34** `αὑτῆς` — the reflexive, rough-breathing — had been spelled
  with the smooth breathing of the ordinary pronoun in the same verse.

Forty-nine wrong Strong's numbers were also corrected across the corpus,
including six `τίνες` that opened "some or any person" when the English asked
"who?", and a class of `δέομαι` forms that opened δέω, "to bind".

### One rendering fix

Placement repairs can leave a word unit holding neither English nor Greek. The
renderer emitted a spacer for those, which showed up as an unexplained gap in
the text. It now skips them. The data is untouched and saved highlights are
unaffected — 69 such units currently exist.

**Note for returning readers:** the corpus is cached for offline use and
refreshes on your *next* visit, so the corrections land one visit later than the
page itself. A highlight saved on one of the specific words that moved will not
re-attach; every other highlight survives.

The full working record — tools, per-book defect tables, and the reasoning
behind each judgement call — lives in the translation repository.

## 2026-07-22 — Thayer's Greek-English Lexicon added to every word

Tapping a Greek word now opens a fourth section beneath Strong's, Word Picture,
and Abbott-Smith: the full text of **Thayer's Greek-English Lexicon** (Joseph
Henry Thayer, 1889), keyed to Strong's numbers. **5,178 of the 5,180 content
words carry a Thayer entry** — only G52 and G680 are absent from the source, and
their section is simply omitted rather than filled with a placeholder. Nothing
is invented.

The text was decoded from the e-Sword "Thayer's Unabridged" module, whose
definitions are stored as RTF with Greek in the Windows Greek code page (1253),
Hebrew in 1255, and polytonic accents as Unicode escapes. A decoder converts all
of that to clean Unicode, normalizes scripture references, and strips the
color/formatting codes, yielding `data/thayer.js` (5,521 entries, ~5 MB).

Because the file is large it is **lazy-loaded**: warmed in the background once
the app is idle, and fetched on first word-tap if a reader gets there first. The
service worker caches it like the other data files, so it works offline after
the first load. Rendered in the Greek serif so the polytonic Greek reads
cleanly.

The same text is published separately as a public-domain, browser-searchable
open-data repository (*Every-Promise-Thayers*): full lexicon, a single
searchable HTML page, and split markdown.

## 2026-07-22 — Word Pictures, round two: rescue the wrongly-flat, and the names

Two gaps in the first pass, both now closed. **Pictures rose from 4,027 to
4,826; flat fell from 1,153 to 354.**

**The wrongly-flat words (660).** The first two rounds — the most-tapped
1,200 words — were written before the build learned to resolve derivation roots
one link deep, so words with a real root came back flat. δοῦλος is the type
case: it was "No picture" when it plainly has one — Strong's traces it to a word
meaning "to bind," so the picture is *the one who cannot walk away*. All 660
such words were re-run through the enriched pipeline; nearly every one now
carries a real image, and the rescue agents independently re-caught the same
source typos (the ἡμέτερος "our/mortal" transposition, the ἐκτός/ἕκτος
misfiling) and routed around them.

**The Hebrew names (168).** Most Bible names are Hebrew, and their meaning was
never in our Greek data — Strong's only says "Abraham, the Hebrew patriarch,"
not what it means. The meanings were resolved from the **public-domain Strong's
Hebrew dictionary** (openscriptures), whose derivation field states them
plainly: Abraham *father of a multitude*, Daniel *God is my judge*, Gideon *the
feller / warrior*, Elizabeth *God of the oath*. The picture had to rest on that
resolved meaning; the agents were told not to invent biblical detail, so an
ambiguous name (Mary, Simon — many bearers) gives the meaning and stops. Ten
names whose Hebrew entry is itself "of uncertain derivation" stay honestly flat.

The remaining 354 flats are the genuine floor: primary particles (πᾶς, "how",
"neither"), and the handful of names the sources never explain. Every one of
the 828 new entries had its anchor re-verified as a substring of its source.

## 2026-07-22 — Word Pictures: a plain-English image for every Greek word

Tap a Greek word and the popup now opens with a **Word Picture** — a short,
concrete, for-a-ten-year-old explanation of what the word depicts — above the
Strong's and Abbott-Smith cards, which are now collapsed by default and one tap
away. New file `data/wordpictures.js`, loaded like the other data blobs, keyed
by Strong's number, one line and LF per `.gitattributes`.

**Coverage: all 5,180 content words** in the corpus (every word except the 166
function words — the, and, of — and a short list of negations, the copula, and
yes/no). **4,027 carry a real picture; 1,153 are honestly flat** ("No picture."),
because a bare name or a primary particle has nothing behind it and inventing
one would be the very thing this feature exists to avoid.

**How they were built, and why they can be trusted.** Every picture is derived
from Strong's (1890) and Abbott-Smith (1922), both public domain and already in
the repo — nothing was pulled from the open web, where "Greek word picture"
content is mostly Strong's guesses with the hedges stripped off. Each entry
carries a build-time *anchor*: a phrase copied character-for-character from that
word's own lexicon text, the phrase the picture rests on. A tool verified all
5,180 anchors as genuine substrings of the source, so an invented etymology has
nothing to quote and cannot pass. The load-bearing example: **προσκυνέω**
(worship) is given Abbott-Smith's "to kiss toward", and the popular "dog licking
its master's hand" — Strong's own flagged conjecture — is named and set aside.

The writing bar was set by seven hand-built exemplars (the arrow of *hamartia*,
the fishing net of *katartizo*, wind for *pneuma*, the bound one for *doulos*).
The rule: a real concrete thing you can see, grounded in a printed line, with a
short turn to why it matters — never a manufactured abstract metaphor.

**A note for whoever regenerates this.** The build resolves each word's Strong's
derivation one link deep, so *doulos* arrives carrying its root "to bind" rather
than a bare cross-reference number. That resolution surfaced a scattering of
errors in the 130-year-old source data — transposed derivation numbers and a
handful of Abbott entries filed under the wrong Strong's number (G1622, G2251,
G3426, G4821, and more, all in TODO.md). The writing agents caught every one by
cross-checking the resolved root against Abbott's own etymology and ignoring the
mismatch. The lexicons themselves still carry these slips; only the word
pictures route around them.



## 2026-07-21 — The corpus reaches 2,022 promises (batches 15–20 complete the 500)

1,522 → **2,022 promises, 30,330 meditations.** Twenty batches, eighteen agents,
**500/500 accepted with zero rejections at any stage.**

**What the sourcing turned out to be.** The obvious promise verses were gone
before this started. 129 well-known references yielded 3 available; a web search
for published promise lists returned ten verses of which ten were already here.
So every one of the 500 came from reading the text — 24,000-odd unused
candidates computed by subtracting the verses already covered, split into
disjoint worksheets so two agents could never be shown the same verse. That is
what made "no duplicate verses" structural rather than merely checked.

**Verse text was never written by hand or by an agent.** References,
meditations and moods were authored; `kjv.lookup` supplied every word of
scripture. A misquotation was not made unlikely, it was made impossible.

**Where the hard books landed.** Three ranges are actively hostile to a
grace-based brief and were flagged to the agents in advance rather than left to
be discovered:

- **Proverbs** is conditional moral wisdom. Only God's keeping, sovereignty,
  provision and personified Wisdom were taken; the maxims were skipped.
- **Deuteronomy** is "if thou shalt hearken, then the LORD will". Avoided
  almost entirely, with 30:6 kept because God is the actor there — He
  circumcises the heart.
- **Job** contains speeches the book itself later declares wrong. Zero verses
  from Eliphaz, Bildad or Zophar; Elihu limited to four statements of God's
  character, since 42:7 does not include him.
- **James** is the most works-flavoured book in the New Testament. It yielded
  three verses that fit cleanly. The rest of that batch came from Hebrews. The
  22/3 split is recorded so nobody later reads it as an oversight.

**Finds that no promise list would have produced:** Philemon 1:18, where Paul
offers to take Onesimus' debt onto his own account; Genesis 15:17, where God
alone passes between the pieces while Abram sleeps; 2 Samuel 7, almost wholly
unused and now carrying seven entries; Job 33:24, "I have found a ransom"; and
Ecclesiastes 9:7, a grace text sitting inside a deliberately bleak book.

**On the voice gate, honestly.** It checks what `add_promises.py` structurally
cannot: whether a meditation hands the work back to the reader. Across 4,500
meditations it fired nineteen times and was wrong nineteen times — it only ever
catches works vocabulary inside a *denial* of works. Useful as a prompt to read
the line. Worthless as a verdict. Do not let a future session treat a flag as a
failure.

Healing: 116 → **209**.

## 2026-07-21 — 150 promises drafted in parallel (batches 3–8)

1,572 → **1,722 promises, 25,830 meditations.** Six agents drafting
simultaneously, **150/150 accepted by `add_promises.py` with zero rejections**.

**Duplicate verses were made structurally impossible rather than merely
checked.** Each agent received its own worksheet of unused verses drawn from a
disjoint slice of the canon — Psalms 1–72, Psalms 73–150, Isaiah + Jeremiah,
the Minor Prophets, Matthew + Mark, Luke + Acts — and was told to pick only
from that file. Two agents cannot choose the same verse if they are never shown
the same verse. The 8,726 candidates were computed by subtracting every verse
already covered by an existing promise span, so the worksheets could not offer
anything already in the corpus.

**Verse text was never written by an agent.** They returned references,
meditations and moods only; `kjv.lookup` supplied the words. A misquotation is
not unlikely here, it is impossible — the only text that can reach the corpus
is the text in the source.

**A voice gate now runs before the validator.** `add_promises.py` guards
structure and cannot guard voice, which is the thing most likely to drift when
six writers work in parallel. The gate checks the two rules that actually
define this content: grace-based (no meditation may hand the work back to the
reader) and in voice (median 6 words, ceiling 12, declarative, no questions or
exclamations). Across 2,250 meditations it raised four flags, **all four false
positives** — it cannot read negation, so "He did not wait for you to deserve
it" trips the same rule as its opposite would. Worth knowing before the next
run: the check is a prompt for judgement, not a verdict.

Word counts came back median 6–7 against the corpus's 6, p90 8–9 against 8.

**The imperative problem, handled well.** Acts 2:38 and Luke 11:9 carry
commands, and the agent holding them flagged the difficulty rather than papering
over it. Its meditations dwell on the gift the command points at — "The word
gift rules out earning", "Access is gift, not achievement", "Peter offers grace
to the crowd that shouted crucify" — which is the framing the rest of the corpus
uses.

Healing is now 153. **300 remaining.**

## 2026-07-21 — 50 new promises, grace-based and Christ-centred (batches 1–2)

1,522 → **1,572 promises, 23,580 meditations.** Two batches of 25, both passing
`add_promises.py` at 25/25 with no rejections.

**The finding that shaped the sourcing.** The obvious promise verses are gone.
Scouting 129 well-known references — the ones any "Promises of God" list
carries — returned **3 available, a 2.2% hit rate**, and a web search for
published promise lists returned ten verses of which **ten were already in the
corpus**. That is not a gap in the corpus; it is evidence the original 1,522
were thorough.

So candidates now come from reading the text rather than harvesting anthologies.
Saturation says where to look: Colossians was 26% mined, Ephesians 23%, which
means three quarters of those letters were untouched — and the untouched part is
disproportionately *declarative statements of what God has done in Christ*,
which is exactly the voice wanted. Batch 1 came from that epistle seam.
Batch 2 came from Jesus' own words in John, the good shepherd and the upper
room, plus the prodigal in Luke 15 and three from Isaiah.

**Verses are never typed.** The authored files carry only meditations and moods;
`kjv.lookup` fills the verse text, so "VERSE NOT VERBATIM" can only fire if a
reference is wrong — a different and far more visible mistake than a
misremembered clause.

**The voice was matched by measurement, not by feel.** New meditations run a
median of 6 words against the corpus's 6, and a p90 of 8 against 8. Every one
points at what Christ has done rather than what the reader should do; nothing in
the 750 asks anyone to try harder.

Healing is now 120, having gained John 14:19, John 16:20, John 6:40 and
2 Timothy 1:10 — all resurrection and sorrow-turned-to-joy rather than illness,
which is the distinction the mood was renamed for.

**450 remaining.**

## 2026-07-21 — Healing replaces Sick; shuffle stops repeating; an anchor verse

**Sick became Healing.** Same 116 promises, retagged by the new
`tools/retag_mood.py`. "Sick" names a condition and asks a reader to identify
as it; "Healing" names what they are reaching for. Because the UI derives its
pill list from the data rather than a hardcoded array, this was a data
operation with no string in `index.html` to change. Sick is deliberately absent
from the validator's allow-list now, so a stale batch cannot reintroduce it and
quietly split the mood in two.

**Shuffle no longer repeats.** The old `shuffleVerse` picked at random and only
stepped away if it landed on the verse already showing, which guards against
nothing beyond an immediate repeat. Random sampling collides far sooner than it
feels like it should: across 116 Healing promises the odds of having already
seen one pass half by the thirteenth tap. A devotional that hands back the
verse you just read does not read as random, it reads as broken.

The pool is now dealt as a shuffled deck — Fisher-Yates, every promise in the
pool appearing exactly once before any appears twice. The deck is keyed to the
mood selection so changing moods discards it rather than dealing indices no
longer in play, and a reshuffle will not open with the verse still on screen,
since that single boundary-crossing tap is exactly the repeat the mechanism
exists to prevent. Verified by dealing every pool to exhaustion: 1,522 shuffles
over the full corpus and 116 over Healing, both zero repeats, zero consecutive
repeats, and nothing dealt from outside the active mood.

**2 Corinthians 1:20 opens every visit.** It was previously reachable only by
chance. It is the claim the whole app rests on — every promise here is yes in
Christ — and a reader should meet it first rather than stumble into it on some
later shuffle. Its fifteen meditations already carried the voice ("Jesus is the
Amen over your life", "The promises are kept in a Person") and were left alone.
Resolved by reference rather than a stored index, because merging a batch of
new promises shifts every index after the insertion point.

## 2026-07-21 — The verse being meditated on is now visible

The meditate view showed the reference and the meditation but not the verse
itself. On meditation 9 of 15 that leaves a reader holding the thing being said
without the thing it is said about — and the reference alone only helps someone
who already knows the verse by heart.

The verse now sits under the reference in small grey type: `--sans` at 0.95em
against the meditation's 2.3em bold, capped at 560px. Deliberately quiet. It is
what is under consideration, not what is being said, and it should not compete
with the meditation for the eye.

Written in `openMeditate` rather than `renderMed`, because the verse does not
change as you page through — it is set once when the view opens rather than
rewritten on every step. Verified to survive stepping, jumping via the dots,
and adding a custom meditation.

## 2026-07-21 — Chapter navigation at the foot of a chapter

Finishing a chapter meant scrolling all the way back to the select at the top
to start the next one. There are now previous/next buttons below the final
section, labelled with the chapter they lead to — "Matthew 6", not a bare
arrow — so a reader knows where they are going before they commit to it.

**The introduction is treated as a destination in the sequence, not a special
case.** It is what sits before Matthew 1 and it has nothing before it, which is
exactly how `populateSelect` already presents it. Revelation 22 is the end of
the line and gets no next; both ends render an invisible placeholder so the
remaining button stays on its own side instead of sliding across.

Everything routes through `loadChapter`, which means the select at the top
stays in sync, the scroll returns to the top, and chapters reached by arrow are
recorded in History — all of it inherited rather than reimplemented. Crossing a
book boundary works because the buttons walk the flat `CHAPTERS` index rather
than reasoning about books: Matthew 28 → Mark 1.

## 2026-07-21 — The site becomes installable, and works offline

The site can now be added to a phone's home screen, opens without browser
chrome, and reads with no connection. **Nothing about the reading experience
changed.** `index.html` gained 30 lines — `<meta>` tags, a manifest link, and
one registration script — and lost one. No CSS, no markup, no text was touched.

This replaces the retired Flutter app rather than extending it. The store
listings are being wound down; the only thing carried across is the sword
launcher icon, which the site's `--sword` `#004878` was already sampled from.

**Fonts moved off Google.** They were the page's only network call, and
PROJECT.md had already flagged the consequence: offline, the three families
fell back to system fonts. An installed app that silently loses its typography
on a plane reads as broken, so all three are now served from `fonts/`. Latin
and Greek subsets only — Cyrillic and Vietnamese were dead weight for an
English UI over a Greek text. `unicode-range` is preserved, so a browser still
fetches only what a given page needs: 22 files exist, a typical visit caches 11.

**The caching split, and what it costs.** Offline and instant-updates pull
against each other — a cache that never expires freezes the corpus, and one
that always revalidates re-downloads 2.5 MB gzipped on a bad connection. So
`sw.js` splits along the line `_headers` already drew: `index.html` is network
first (small, changes often), `data/*.js` is stale-while-revalidate (huge,
changes rarely). The honest cost is that **a newly added promise lands on the
reader's next visit, not the current one.** That is the price of the corpus
loading instantly and working offline, and it is worth knowing before wondering
why an edit "did not show up." The data files are deliberately *not* precached;
`index.html` pulls them in anyway, and precaching would have made the first
visit slower than it is today.

**Greek coverage was verified, not assumed.** Every non-ASCII codepoint in the
four data files was extracted and checked against the self-hosted
`unicode-range` declarations: 313 distinct codepoints, of which 194 are Greek.
**All 194 are covered by Gentium Plus — no gaps**, including the whole Greek
Extended block the polytonic accents live in. Verified in a browser with the
server stopped: Matthew 5 rendered 604 Greek words from cache, computed font
`"Gentium Plus", serif`.

The same sweep turned up four OCR artifacts in `abbott.js` — two combining
accents sitting one letter to the right of where they belong, a stray acute
after a comma, and a Cyrillic ї standing in for a Latin ï. Logged in TODO.md
under data fixes; they need repairing upstream in the generator, not by hand.

Hebrew (49 codepoints, plus 14 presentation forms) has no font of its own and
falls back to a system face. That was equally true when Google served the
fonts — Gentium Plus offers no Hebrew subset — so it is unchanged, not a
regression, but it is now written down.

## 2026-07-20 — Two features investigated and declined

Recorded because the reasoning cost real work and would otherwise be repeated.

**Greek pronunciation audio — not built.** No automated option meets this
project's accuracy bar. There is no single correct Koine pronunciation
(Erasmian, Modern, and reconstructed Koine genuinely conflict); LEXICON's
existing pronunciation on all 5,359 entries is Erasmian, so a Modern Greek TTS
voice would contradict the text printed beside it; and eSpeak's Ancient Greek
voice is described by its own maintainers as "an initial naive implementation."
Shipping any of them would make audio the first thing in the app that is
approximate while presented as authoritative.

The useful finding, if it is ever revisited: **500 recordings would cover 84.3%
of every Greek token**, 200 cover 73%, and 1,841 of the 5,359 words occur once.
Recording is a few hundred items, not 5,359. Full detail in TODO.md.

**Abbott–Smith reference linking — not built.** Those entries carry 33,092
embedded references; 27,750 are NT and resolve to a chapter. But the corpus has
no verse numbers by design, so "Mt 5:16" could only land a reader in Matthew 5
with nothing to find verse 16 by — promising a precision the translation
deliberately does not offer. Left as printed text, which is what they are in the
original lexicon.

## 2026-07-20 — Favorites, History, and cross-references go live

Three features that were built-but-inert. No text was touched.

### The mood row was checked, and is fine

Adding Provision made 17 pills where the row was designed for 16, and nobody had
opened the page. Checked at desktop and at a true 390px phone viewport: **no
overflow, nothing clipped, bottom nav intact.** On desktop the row breaks 8/7/2,
leaving "Sick, Angry" on an orphan third line — cosmetic, reflows at other
widths, and the design guidelines say not to redesign. Left alone.

**A caution for the next session that measures this.** Headless Chrome has a
minimum viewport of 500px. Asking for `--window-size=430` lays the page out at
500 and then crops the screenshot to 430, which looks *exactly* like horizontal
overflow: pills cut mid-word, the verse running off, "Journal" clipped to "J".
A control page reporting `window.innerWidth` proved it was the harness, not the
site. Real narrow viewports need an iframe of a fixed width, not a small window.

### Favorites — persisted

Was `let fav = false`: the heart reset on every reload *and* on every verse
change, so it never meant anything, and the tab held a hardcoded empty state.

Now follows the bookmarks pattern exactly (`loadStore` → mutate → `saveStore` →
re-render), stored under `everypromise_favorites`.

**Keyed on the promise REFERENCE, not its index.** PROMISES has gone 329 → 1,005
→ 1,522 in two days; an index-keyed favorite would silently re-point to a
different verse every time the corpus grows. `jumpToFavorite` also drops a
favorite whose reference no longer resolves rather than throwing — the
alternative is a dead row the user cannot clear.

### History — tracked

Records chapter views most-recent-first under `everypromise_history`, capped at
50, deduped by chapter so re-reading Romans 8 moves it to the top instead of
filling the list with copies.

Recorded inside `loadChapter` rather than in the click handlers, so every route
in counts — the select, a bookmark jump, a history jump. Placed deliberately
*after* the `'intro'` early-return: the introduction is not a chapter and should
not fill the list.

### Cross-references — enabled and retuned

`SHOW_CROSSREF` was `false` with the note "re-enable once the full NT is
translated and this can be retuned against full-corpus word frequency." The full
NT has been in place since 2026-07-18. Now on.

**`CROSSREF_MAX` retuned 12 → 30.** The 12 was set when 7 books existed (96,778
Greek tokens); at 137,554 the same semantic threshold scales to ~17. But
measuring showed the choice is not delicate:

| Band | What lives there |
|---|---|
| 16–32 occurrences | ποιμήν shepherd, κληρονομέω inherit, μετάνοια repentance, ὑπομονή endurance, ἐλεέω show mercy |
| 1,200+ | ὁ 19,767 · καί 8,973 · αὐτός 5,549 · δέ 2,766 · ἐν 2,733 |

Nothing lives in between, so any cutoff from ~17 to ~100 excludes exactly the
same set of function words. The real constraint is list length: the list dedupes
by section, so at 30 a reader sees a median of 4 rows, 13 at the 90th
percentile, 28 at worst. The modal already scrolls at 85vh, so no CSS changed.

Clicking ποιμήν now shows 18 occurrences as 11 rows — "John 10 · I Am the Good
Shepherd (5×)", "Luke 2 · Good News to Shepherds (4×)", "Matthew 25 · The Sheep
and the Goats". The editorial section headings are what make it readable; a bare
verse list would not trace a theme like that.

### Verified by driving the app, not by reading the diff

33 assertions run against the live page in a browser, via an iframe harness:

```
favorites/history .... 20/20   incl. survives a full reload, dedupe,
                               cap at 50, intro not recorded,
                               heart clears when un-favorited elsewhere
cross-references ..... 13/13   incl. kai (8,973x) shows NO links,
                               single-occurrence renders nothing,
                               30 in / 31 out boundary
```

**One harness bug worth recording:** `frame.PROMISES` is `undefined`. index.html
declares its state with top-level `const`/`let`, which are global *lexical*
bindings and never become `window` properties — only function declarations do.
The harness reads state through `eval()` in the iframe's own scope instead. The
first run's failures were the test, not the app.

## 2026-07-20 (later still) — Grace-lens audit: 263 law-shaped meditations rewritten

Chris read some meditations and said they "feel like law and doing." He was
right, and the defect was **older than the Provision work**.

### The shape, not the vocabulary

`med_scan.py` already checked for banned words (strive, earn, sow/reap) and
reported the corpus clean. It was looking for the wrong thing. The real defect
is a SHAPE: **reader-verb → divine-payout**, which can be built entirely from
innocent words.

  "Generosity unlocks overflow."          (Luke 6:38)
  "Giving activates overflow."            (Malachi 3:10)
  "Delight unlocks destiny."              (Psalm 37:4)
  "Confession opens the door."            (1 John 1:9)
  "Faith is heaven's currency."           (Mark 9:23)
  "Heaven records every good work."       (Colossians 3:23-24)
  "Humility invites exaltation."          (James 4:10)
  "Your cry shifts things."               (Psalm 56:9)

Not one of those trips a keyword filter. All of them make the reader's
performance the lever that moves God — ledger-and-currency language about a
Father. That is the thing the grace lens exists to prevent.

### It was concentrated in the OLDEST material

The 517 promises added earlier the same day were written against an explicit
grace brief and came back essentially clean. The original corpus never had that
brief, and it shows:

| Batch | Lines rewritten / 600 |
|---|---|
| rev002 (early) | **39** |
| rev003 (early) | **37** |
| rev005 (early) | **37** |
| rev001 (early) | **20** |
| rev026 | 9 |
| rev008 | 8 |
| most later batches | **0–3** |

Nine of the 39 batches needed **zero** changes.

**Worst single promise: Psalm 91:14 — 9 of its 15 lines were transactional**
("Love activates His protection.", "Deliverance is tied to devotion.", "Knowing
Him is your promotion."). The verse itself is a because/therefore construction,
and the meditations had simply inherited its grammar.

Runner-up for subtlety: **Colossians 3:15**, where four lines cast gratitude as
the thing that *maintains* God's peace ("Give thanks — it keeps peace ruling.").
That one is harder to spot than a prosperity line, and worse: it makes a
finished gift contingent on upkeep.

### Result

**263 lines rewritten across 138 promises — 1.15% of 22,830.** The corpus was
not broadly broken; it had a real, specific, and clustered defect.

Rewrites move God into the subject position and put His action first:

| Before | After |
|---|---|
| Confession opens the door. | The door was opened at the cross. |
| Trust brings calm. | Calm settles over you as you trust. |
| Waiting brings renewal. | He renews your strength as you wait. |
| Weakness invites power. | His power meets you in your weakness. |
| Prayer activates promise. | His promise stands before you pray. |
| Your sighing moved Him to act. | He was moving before you sighed. |
| He forgave the moment you said it. | Forgiveness was settled before you spoke. |

`law_scan` LEVER flags: **47 → 16**, and all 16 survivors are false positives —
God is the actor ("He releases you into peace") or the qualification is inverted
("Your sickness qualifies you for Him", "He qualifies you, not your years").

### Two tools, and one that had to be thrown away

| Tool | What it does |
|---|---|
| `tools/law_scan.py` | shape detector — OBLIGATION / CONDITIONAL / LEVER |
| `tools/med_export.py` | splits PROMISES into reviewable batches |
| `tools/med_apply.py` | merges reviews back; verse, reference and moods FROZEN |

**The imperative detector failed and is left in the file, disabled, with the
reason written down.** It tried to flag bare commands by matching the first
capitalised word. English marks the imperative by MOOD, not form, so "Guard your
heart." and "He stands with you." are identical to a regex. First run: 15,198
"imperatives" across 885 "verbs", led by *he* (3,508), *his* (1,751), *your*
(1,582), *the* (1,220). Two thirds of the corpus flagged is not a triage list.
Deleting it silently would have invited the next session to rebuild it.

**Calibration again outweighed authoring**, exactly as with `prose_scan.py` and
`med_scan.py`. The OBLIGATION check first returned 33 hits of which ~30 were
grace-affirming NEGATIONS — "not your job, but His", "He does not require you
steady", "an invitation, not a demand". The grace lens is usually expressed by
negating the law word, so a bare keyword search reports the *best* lines in the
corpus as defects. Suppressing negated frames took it to 16.

### The reviewers were told they could find nothing

Every batch prompt carried an explicit over-trigger guard and told reviewers
that reporting zero was a valid result. Nine did exactly that. This matters:
the project has twice broken working text by over-correcting (Luke 5's
existential inversion, Matthew 8's content-search targeting). A pass that
rewrites 8,000 lines is not a grace audit, it is a rewrite. 1.15% is the number
that says the tool was aimed correctly.

`med_apply.py` refuses any batch that alters a verse, a reference, or a mood —
so a reviewer judging a devotional line has no authority over scripture. All
1,522 verses still verify verbatim against the KJV.

### Left deliberately alone — Chris's call

Reviewers repeatedly hit verses whose KJV text is *itself* conditional, and were
told to fix the meditation rather than soften the verse. Where a line merely
paraphrases the verse's own grammar, they left it and flagged it:

- **Malachi 3:10** — "prove me now herewith" is a literal test-and-payout formula
- **Luke 6:38** — "give, and it shall be given unto you"
- **James 4:7 / 4:10** — submit → the devil flees; humble → He lifts you
- **Psalm 50:23** — "to him that ordereth his conversation aright will I shew…"
- **Joshua 1:8** — "then thou shalt make thy way prosperous" (6 of 9 fixes in one batch)
- **Psalm 25:9, Proverbs 28:13, Hebrews 6:15, Psalm 91:15, Matthew 21:22, Luke 12:31**

The honest tension is in the verse selection, not the writing. Whether those
promises belong in a grace-centred corpus at all is a decision for Chris.

### Verified

```
promises ............. 1,522   unchanged
meditations .......... 22,830  unchanged (all exactly 15)
lines rewritten ...... 263 across 138 promises (1.15%)
verses verbatim KJV .. 1,522 / 1,522
moods ................ unchanged, all 17
NT units/tokens ...... 117,353 / 137,554  untouched
law_scan LEVER ....... 47 -> 16, all 16 false positives
```

## 2026-07-20 (later) — Promises 1,005 → 1,522, and a Provision mood

### The count this file used to claim was wrong

The entry below reports 1,007 promises / 15,105 meditations. The data on disk
held **1,005 / 15,075**. Two promises were removed after that entry was written
and only `README.md` was updated to match. Both were **Sick**-tagged — every
other mood count in that entry still reconciles exactly against the data, and
Sick alone was short by two. What was dropped, and why, is not recorded
anywhere. If it was a KJV-verification failure it deserved a line, because that
gate is the whole defence against misquoted scripture.

### Provision — a 17th mood

Money, work, debt, lack, harvest, daily supply. **120 promises** carry it.

The UI needed **no change**: `MOODS` in `index.html` is derived from the data,
so the pill appeared on its own. The only code edit was adding "Provision" to
the validator's allow-list in `add_promises.py`. That design paid for itself
exactly as intended.

**The theological risk was the point of the care taken.** Provision is where a
grace-centred Bible turns into a prosperity one, and several of these verses are
the classic proof texts — Malachi 3:10, Luke 6:38, Proverbs 3:9-10,
Deuteronomy 15:10, Mark 10:29-30. The rule applied throughout: provision is
grounded in God's fatherhood and Christ's finished work, and generosity is a
**response** to grace received, never a payment that obligates God. No
meditation makes the reader's giving, tithing or faith the lever that produces
money.

Verses whose KJV wording is itself conditional or transactional were kept
verbatim and handled in the meditations rather than softened in the text:

| Verse | The tension | How it was handled |
|---|---|---|
| Deuteronomy 15:10 | "because for this thing the Lord thy God shall bless thee" | "Blessing follows a heart, not a transaction." |
| Proverbs 3:10 | barns filled — paired with 3:9's tithing | God's generous character, no give-to-get causality |
| Job 36:11 | "if they obey and serve him" | God's desire for flourishing, not obedience-as-trigger |
| Mark 10:29-30 | hundredfold return for what was left | "a generous rewarder, not a debtor" |
| Exodus 19:5 | explicit Sinai conditionality | written to "treasured possession" identity |
| Luke 6:37, Mark 11:25 | forgiveness reads reciprocal | forgiving others flows *from* forgiveness received |
| Micah 4:12 | judgment context, not comfort | **repurposed** to "His counsel exceeds understanding" — the most interpretive move made; worth a second look |

### 1,005 → 1,522 promises, 22,830 meditations

**517 added.** Every mood rose, and the thin ones rose most:

| | Before | After |
|---|---|---|
| Angry | 74 | **106** |
| Sick | 86 | **116** |
| Stressed | 90 | **128** |
| Tempted | 94 | **136** |
| Provision | — | **120** |

### Misquotation was made structurally impossible, not merely detected

The previous round *validated* verse text against the KJV and rejected what
failed. That is a gate on work already done — the author still types the verse,
and typing scripture from memory is the one failure this project cannot absorb.

`tools/fill_verses.py` inverts it. A batch now supplies only reference,
meditations and moods; the verse text is **copied out of the local KJV** by the
tool. Nobody quotes anything, so nothing can be misquoted. All 26 batches were
written by agents that never had authority over the verse field, and every one
came back with the text byte-identical. `add_promises.py`'s verbatim check was
left in place as an independent second lens rather than the only one.

Result: **1,522 of 1,522 verses verbatim** (`python tools/kjv.py --verify`).

### 5 pre-existing quotation defects fixed

`kjv.py --verify` had been reporting 1000 match / 5 differs and nobody had run
it down. None was invented text; four were silent **modernisations** and one
dropped clauses:

| Verse | Was | KJV reads |
|---|---|---|
| Jeremiah 33:3 | "show thee" | **shew** |
| 3 John 1:2 | "thy soul prospers" | **prospereth** |
| Matthew 28:20 | "with you always" | **alway** |
| Psalm 29:11 | `people:` | `people;` |
| Ephesians 4:31-32 | elided two clauses, no ellipsis | restored |

The Ephesians one mattered most: the elision had removed **"even as God for
Christ's sake hath forgiven you"** — the grace clause that grounds the command.
In a grace-centred Bible that is the half of the verse you least want missing.
Fixed by `tools/fix_kjv_quotes.py`.

### New tooling

| Tool | What it does |
|---|---|
| `tools/fill_verses.py` | populates verse text from the local KJV so it is never typed |
| `tools/ref_filter.py` | screens candidate references for unresolved / already-present / span-overlap **before** meditations are written |
| `tools/med_scan.py` | the grace-lens scanner — self-effort language, prosperity-transactional shape, straight apostrophes, length outliers, cross-promise repeats |
| `tools/fix_kjv_quotes.py` | the 5 quotation repairs above |

**`med_scan` needed calibration more than authoring** — the same lesson
`prose_scan.py` learned. Its first run flagged 25 "self-effort" lines and every
single one was the *opposite*: "You did not earn this gladness.", "Wisdom is His
to give, not yours to earn.", "You need not strive; His grace already won." The
grace lens is expressed by **negating** the effort verb, so a bare keyword search
reports the most on-frame lines in the corpus as defects. Suppressing negated and
contrastive frames took it from 25 hits to 6, all of which read clean.

Final scan of the 517: **0 transactional, 0 straight apostrophes, 0 over-length,
6 self-effort flags all false positives.** One genuine fix was made by hand —
John 20:31 read *"Your belief unlocks life in His name."*, which makes belief a
lever; now *"Life in His name is freely given."*

### A bug in my own filter, caught by the merge gate

`ref_filter.py` screened 1,148 candidates down to 518 and **let an exact
duplicate through**. `Mark 10:30` was listed twice in the candidate pool — once
under Provision, once under Lonely — and the span-overlap loop skips any
comparison where the other reference normalises to the same key, precisely so a
reference is not reported as overlapping *itself*. That guard made an exact
repeat invisible.

`add_promises.py` caught it at merge, but only after 15 meditations had been
written for both copies. The duplicate was dropped (517 merged, not 518) and
`ref_filter` now checks the candidate list against itself. **Cost: one wasted
batch entry. Had the gate not existed, the app would show the same verse twice
under the same heading.**

### Reference discovery used the web; text never did

Topical verse lists were searched for discovery only — the same limit set last
session after a list cited a Nehemiah 8:43 in a chapter with 18 verses. They
proved shallow again: of 152 provision candidates seeded from them, **42 were
already in the corpus**. Depth came from going past them. Of 1,148 candidates
screened, **0 were unresolved** — every reference existed, because the lists were
used for ideas and the KJV index was used for truth.

Two books that had **zero** promises now have one each: **Obadiah** (1:17) and
**Philemon** (1:6). 66 of 66 books represented.

### Verified

```
promises ............. 1,522   (was 1,005)
meditations .......... 22,830  (all exactly 15 per promise)
verses verbatim KJV .. 1,522 / 1,522
duplicate references . 0
moods ................ 17, all populated, all derived from data
NT units ............. 117,353  unchanged
NT tokens ............ 137,554  unchanged
JSON blobs ........... all 4 parse
```

**Not verified: the visual layout.** A 17th mood pill is one more than the row
was built for, and nobody has opened the page. That needs a human.

## 2026-07-20 — Promises 329 → 1,007, and the mood picker goes live

### Mood filtering shipped
All 329 promises were already tagged across 16 moods and **no code had ever read
them.** The picker now sits on the top row of the Promises view, centred, across
from the "verse of the day" kicker. Tap a mood → the kicker becomes "for when you
feel anxious" and a matching verse loads immediately.

- The mood list is **derived from the data**, not hardcoded, so a mood added to
  `PROMISES` appears automatically and one removed cannot leave a dead button.
- Multiple moods take the **union, not the intersection** — someone both anxious
  and tired wants either verse, and intersecting 16 moods empties out fast.
- `shuffleVerse` had to be **fixed, not extended**: its fallback was
  `(n+1) % PROMISES.length`, which steps to the next promise in the whole corpus
  and, with a filter on, would hand back a verse the chosen mood does not carry.
- No count is shown. A number invites the reader to weigh one mood against
  another ("only 22?") when what matters is that a promise is there at all.

### 329 → 1,007 promises, 15,105 meditations

**The problem worth naming first.** Adding ~678 promises means producing ~678
verse texts, and scripture generated from memory *will* contain misquotations
that nothing downstream can flag. In a Bible app that is the worst possible
defect — it is the actual content. So a public-domain **KJV (1769) was installed
as a source of truth** (`tools/kjv.py`), and every added verse is looked up and
copied verbatim. Nothing merges until it matches contiguously.

**That check immediately found 3 defects in the original 329:**

| Verse | Shipped as | KJV reads |
|---|---|---|
| Psalm 16:9 | "my flesh shall rest in **confidence**" | "in **hope**" |
| Proverbs 17:22 | "a broken spirit drieth **up** the bones" | "drieth the bones" |
| 2 Corinthians 1:3 | "the Father of mercies" | "the Father **of our Lord Jesus Christ**, the Father of mercies" |

The third had silently dropped Christ out of the verse. All three corrected.

**Mood balance was the second goal.** Later waves were steered at the thin moods
rather than picking the best verse book-by-book, and the floor rose from 23 to 74:

| | Before | After |
|---|---|---|
| Angry | 23 | **74** |
| Sick | 37 | 88 |
| Stressed | 33 | 90 |
| Tempted | 37 | 94 |
| Joyful | 36 | 113 |

**Web browsing was allowed for reference discovery only — and earned that limit
immediately.** A topical list attributed a verse to the wrong reference and cited
a **Nehemiah 8:43 that does not exist** (Nehemiah 8 has 18 verses). The local
lookup caught both. The lists also proved shallow: for Angry, Tempted, Tired and
Overwhelmed, nearly everything they surfaced was already in the corpus. The depth
came from going past them — the lament psalms, and deep cuts like 1 Kings 19:5-6
(God's answer to burnout was a nap, food, and a second nap, with no rebuke),
Exodus 31:17 (God rested *and was refreshed*), John 4:6 and Mark 4:38 (Jesus too
tired to walk, asleep on a pillow), Luke 22:43 (Christ himself needed an angel).

**The grace filter is visible in what was refused**, not just what was chosen:
- **Anxious** — rejected bare "fear not" verses (Luke 8:50 "believe only", 1 Pet
  3:14). A command without its ground lands on an anxious reader as one more
  failure. Every kept verse carries the reason: *"for I am with thee."*
- **Sick** — rejected the "thy faith hath made thee whole" family outright, since
  making healing contingent on the sufferer's faith wounds a reader who has
  prayed and not been healed. Leans on presence and resurrection, so the deck
  holds for someone who is dying.
- **Tired** — rejected Galatians 6:9 ("be not weary in well doing"), a command
  aimed exactly at the person who already is.
- **Angry** — rejected Jonah 4:4 ("Doest thou well to be angry?"). Chose Mark
  3:5, John 11:33, Hebrews 5:7 — anger and grief met by a Christ who had them.
- **Job** — every Job entry was speaker-checked. Job 33:24 was rejected despite
  its christological weight ("I have found a ransom") because it is Elihu.
  ⚠️ **Job 5:18 and 22:21 in the original 329 are both Eliphaz**, of whom God says
  at 42:7 "ye have not spoken of me the thing that is right." Flagged, not
  touched — removing content is Chris's call.

### Tooling
- `tools/kjv.py` — verbatim lookup + verification. Calibrated against the
  existing 329 first; that required handling roman-numeral book names, verse
  ranges, and the fact that the corpus deliberately **excerpts** verses, so the
  test is containment rather than equality.
- `tools/add_promises.py` — batch validator and merger. Refuses to merge while
  any entry fails. **Calibrated against deliberately bad input** before its
  verdicts were trusted: it correctly rejects a single changed word, a modernised
  archaism, a spliced middle, a 14-line deck and a typo'd mood.
- Mid-run it gained a **verse-span overlap** check, after an agent noticed that
  "1 Cor 15:54" and "1 Cor 15:54-55" are different keys carrying the same words.
  It caught three more such collisions within the hour.

### Known and left alone
- 5 verses differ from KJV by deliberate editorial choice (archaisms, one
  elision, one semicolon).
- 7 overlapping verse spans, **all pre-existing in the original 329**. The 678
  added this session introduced zero overlaps and zero duplicates.
- The validator checks structure, not prose. Meditation quality is guarded by
  reading, not tooling — every batch was sampled by hand.

## 2026-07-20 — The whole New Testament read: 1,190 sections, ~250 fixes

Every section of all 27 books was read as English prose and repaired. Matthew
had been done as a pilot; the remaining 1,032 sections were completed in this
pass.

### The defect rate tracks how a book was BUILT, not where it sits

| Band | Sections | Fixed | Rate |
|---|---|---|---|
| Luke 1–12 | 51 | 36 | **71%** |
| Luke 13–24 | 52 | 36 | **69%** |
| Acts 1–14 | 71 | 24 | 34% |
| Mark | 77 | 25 | 32% |
| John | 72 | 22 | 31% |
| Acts 15–28 | 69 | 19 | 28% |
| Matthew | 132 | 47 | 36% |
| Romans · 1 Cor · Revelation | 202 | 27 | 13% |
| Gal · 2 Cor · Heb · 2 Pet · Titus · 1 Pet · 2 Tim · 2 Th | 300 | 22 | 7% |
| **Eph · Col · Php · 1 Tim · 1 Th · 1 Jn · Jas · Jude · Phm · 2 Jn · 3 Jn** | **194** | **0** | **0%** |

The five hand-reordered books carry nearly all of it. The twenty books authored
fresh by the `tools/nt_*.py` pipeline in the Mak voice were already in English
order — **eleven of them, 194 sections, needed nothing at all.**

The old "~2 defects per chapter" estimate came from Matthew 1–19 and was wrong by
a factor of three. Sampling a book understates it badly, and *which band* you
sample decides the answer you get.

### The defects a prose read structurally cannot see

The most important finds. In every one of these **the English already read
correctly**, so no prose pass, no scanner and no assertion could see them. Only
reading each Greek word against its own label does.

| Where | The label said | It should say |
|---|---|---|
| **1 Cor 10:22** | `ἰσχυρότεροι` → "are we provoking" | "stronger" — **a whole sentence was gone** |
| **Luke 1:35** | `τὸ γεννώμενον` → "the holy one" | "the one to be born" — swapped with `ἅγιον` |
| **Luke 1:64** | `ἀνεῴχθη` → "And immediately" | "was opened" — swapped with `παραχρῆμα` |
| **Luke 1:65** | `τὰ ῥήματα` → "these" | "the words" — swapped with `ταῦτα` |
| **Luke 3:23** | `ὤν` → "old," | "being" — glosses shifted one place left |
| **John 4:12** | `εἶ` → "than" | "are" — Greek has **no word** for "than" |
| **John 4:24** | `ὁ` → "is" | (folded) — the clause is verbless; "is" is supplied |
| **Rom 16:14** | `Ἑρμᾶν` → G2061 *Hermogenes* | G2057 *Hermas* — **a different person** |

**Luke 3:23 is the same verse and the same one-place shift as the Heli
incident** — a second, separate residue the original repair missed. This class
does not come in ones.

### A spent plan re-applied cost a sentence

1 Cor 10:22 read *"Or are we provoking to jealousy the Lord? Are we are we
provoking the Lord to jealousy?"* Paul's second question — "Are we stronger than
he?" — had been overwritten with a copy of the first.

The cause was `tools/plans/1cor10_2fix.py`, which targeted indices 94/95
believing them to be `παραζηλοῦμεν`/`τὸν κύριον`. By the time it ran they were
`ἰσχυρότεροι`/`αὐτοῦ`. **Every assertion passed**, because an overwrite changes
neither the Greek multiset nor the unit count.

The file is deleted, and `apply_plan.py` now refuses any plan it has already
applied (ledger at `tools/plans/APPLIED.log`, `--force` to override). A plan is a
one-shot instrument and the tool enforces it.

### Meaning errors fixed

- **Luke 21:15** — *"wisdom which will not be able to withstand … all those
  opposing you"* said the **wisdom** fails. `δυνήσονται` is 3rd plural; its
  subject is `ἅπαντες οἱ ἀντικείμενοι`, last in Greek order. The promise is that
  the **opponents** cannot withstand it.
- **Mark 15:39** — made the centurion the **object** of "seeing". `ἰδών` is
  nominative and agrees with `ὁ κεντυρίων`.
- **Acts 10:47** — *"forbid the water from being baptized"* made the **water**
  the thing baptized. `τοῦ μὴ βαπτισθῆναι τούτους` is an articular infinitive
  with its own accusative subject.
- **Acts 7:7** — the emphatic `ἐγώ` belonging with `κρινῶ` had been stranded
  behind the closing quote, reading as an apposition to "God".
- **Rev 9:5** — *"they were allowed not to kill them"* inverted the grant.
- **Luke 20:10–12** — two clauses had lost their object entirely.

### Also

- **Recitative ὅτι: 55 → 0.** `ὅτι` before *direct* speech is a quotation marker
  with no English equivalent, producing *he said that "I am…"*. Cleared by
  `tools/fold_recitative.py`, whose rule is narrow enough that `ὅτι` before
  *indirect* speech — a real "that" — is never touched.
- **Luke 20:21** — *"you do not receive a face"* → *"you do not show
  partiality"*. `λαμβάνειν πρόσωπον` is a fixed Semitism, so it is glossed as an
  idiom, as `εἰς τὰ ὀπίσω` → "back" already was.
- **Unbalanced-quote sections: 112 → 2.**
- **Lowercase sentence-starts: 1 → 0** (2 Peter 2, where a full stop had broken
  the "For if … then" spanning vv. 4–9).

### Verification against pre-audit baseline `71ca43e`

```
Greek multiset changed ....... 0 of 260 chapters
units ........................ 117,353   (unchanged)
tokens ....................... 137,554   (unchanged)
arity mismatches ............. 0
tags without a G-number ...... 0
G-numbers unresolvable ....... 0
Greek leaking into English ... 0
prose_scan ................... 20 flags, unchanged — no new defects introduced
```

### Left deliberately undone

- **Mark 1:41 `ὀργισθεὶς`** — a textual-variant decision about how the text
  portrays Jesus. Chris's call, not the AI's.
- **The 4 Romans/SBLGNT tokens** — now fully diagnosed (each is a *pair*: a
  duplicated token masking an omitted one). Repair deferred to a fresh session;
  see TODO. No meaning is affected.
- **Quote convention** in the long Acts speeches — a taste decision.

## 2026-07-19 — Wrong Strong's numbers: 224 tags corrected

Clicking **"must"** anywhere in the New Testament showed the definition of
**"bind."** The word `δεῖ` ("it is necessary") was tagged G1210 `δέω` ("to
bind") in 89 of its 92 occurrences. Four more ambiguous forms had the same
problem — 224 wrong tags in all:

| form | was tagged | popup showed | corrected to | n |
|---|---|---|---|---|
| `δεῖ` / `ἔδει` | G1210 δέω | "bind, be in bonds, knit, tie" | **G1163** δεῖ | 89 |
| `ἱερῷ` / `ἱεροῦ` | G2413 ἱερός *(adjective)* | "holy" | **G2411** ἱερόν *(noun)* | 70 |
| `μιᾷ` / `μίαν` | G1519 εἰς *(preposition)* | "into, against, among…" | **G1520** εἷς *(numeral)* | 26 |
| `εἰδὼς` | G3708 ὁράω | "behold, perceive, see" | **G1492** εἴδω | 22 |
| `μῆνας` | G3375 μήν *(particle)* | "+ surely" | **G3376** μήν *(month)* | 17 |

**Why the build never caught it.** The pipeline's gate was "every tag resolves
to a LEXICON entry" — 0 MISS. A tag that resolves to the *wrong* entry satisfies
that check silently. Every one of these numbers was real and present; it just
pointed at a different word.

**Why it needed two detectors.** The obvious approach — compare each tag's
Strong's headword against the SBLGNT lemma — finds none of these. MorphGNT
itself lemmatises `δεῖ` to `δέω` in all 92 places, because `δεῖ` genuinely is the
third-singular of `δέω`. The tag agreed with the lemma source and was still wrong
for a reader, since Strong's keeps a dedicated impersonal entry. So a second tool
asks a different question: across every place a form appears, does the English we
chose *ever* share a root with its tag's definition? Eighty-nine consecutive
misses is a mistag, not a paraphrase. Both tools are kept — `tools/tag_audit.py`
(lemma lens) and `tools/tag_sense.py` (usage lens) — because each is blind to
what the other sees.

`tag_audit.py` also produced a reassuring negative: across all 40,776 tokens of
the 20 pipeline-built books there are **no** genuine headword/lemma
disagreements. Its 503 flagged classes are entirely spelling traditions
(εἴδω/οἶδα, Δαβίδ/Δαυίδ, Μωσεύς/Μωϋσῆς), voice lemmatisation (φοβέω/φοβέομαι),
suppletive stems (φαγεῖν really is the aorist of ἐσθίω), and the documented
textual-variant parallels.

**A near-miss, recorded because it nearly went in.** The first draft of the
`ἱερόν` rule also matched `ἱερά`/`ἱερὰ`. Those two occurrences — 1 Cor 9:13 "the
sacred things", 2 Tim 3:15 "the sacred writings" — are the genuine *adjective*
and were already tagged correctly. The rule would have relabelled both as
"temple". It was caught by listing every token each rule would touch and reading
the English before writing anything. `retag.py` rules now match the whole surface
form and each carries its justification.

**G3376 was missing entirely** from both LEXICON and ABBOTT. Added from the
Strong's dictionary and Abbott–Smith, which keys the entry explicitly as
`μήν_2|G3376` with a reference list (Lk 1, Ac, Ja 5:17, Re 9–22, Ga 4:10)
matching exactly where our `μῆνας` tokens sit. LEXICON 5,357 → 5,358,
ABBOTT 5,339 → 5,340.

**Verification.** `retag.py` changes only the Strong's number inside a tag,
preserving the morphology suffix, and asserts the Greek and English of every unit
are byte-identical before writing. units 117,353 / tokens 137,554 unchanged;
0 Greek-in-English leaks; 0 unresolvable tags. MorphGNT lemma data was downloaded
for Matthew–1 Corinthians so the audit now covers the whole NT.


## 2026-07-19 — Matthew gloss-drift audit (P0, first half) — and the last Greek leak closed

Matthew was one of the two books reordered **before** the pair-checking
discipline existed, so its glosses had never been read against their own Greek.
All 28 chapters have now been audited, flag-by-flag and by full pair-reading.

**New tool: `tools/gloss_scan.py`.** For every content word (V/N/A) it checks
whether the English gloss shares a root with that word's own Strong's/Thayer's
definition. A bare "no overlap" test is useless — it flags ~10% of the corpus
and scores carefully-checked new books as high as never-audited Matthew. The
signal that works is **DRIFT**: English that matches a *neighbour's* definition
but not its own. That is the exact fingerprint of the reorder+regloss bug, and
it cuts 10,137 raw flags to 712 corpus-wide (6.1/1k).

**13 real drifts found and fixed in Matthew** (8 from scanner flags, 5 found
only by reading). Every fix is a plan module under `tools/plans/fix_mtNN_S.py`,
applied through `apply_plan.py`, which asserts the section's Greek multiset is
unchanged:

- **8:8** — a 3-way label shift: μου "you should come", τὴν στέγην "my",
  εἰσέλθῃς "roof;". Prose read fine; every gloss sat one word off.
- **27:46, 27:50** — φωνῇ "in a loud" / μεγάλῃ "voice," — adjacent swap, twice.
  φωνή is *voice*, μέγας is *loud*.
- **22:24, 26:39** — a bare article (τῷ, τοῦ) carrying the noun's label
  ("brother.", "Father.") while the actual noun sat next door.
- **6:2** — "with trumpets" had slid off σαλπίσῃς onto ἔμπροσθέν σου.
- **6:14** — dative ὑμῖν labelled "your"; the real possessive ὑμῶν stranded as a
  bare capitalised "Your" opening the next sentence.
- **9:13** — the negation οὐ carrying "I did"; **13:21** — δέ carrying "comes",
  the verb belonging to γενομένης.
- **21:33** — φραγμόν "around it"; its own sense (*fence/wall*) had moved to the
  preceding verb.
- **4:23, 19:24** — dangling "every" and a stranded διά.

**7:12 — the last Greek leak in the corpus is gone.** The documented leak turned
out to be drift underneath: οὕτως ("so") was labelled "for this" (that's
οὗτος), αὐτοῖς was labelled "also", and οἱ ἄνθρωποι was labelled "to others".
A surplus ἐστιν that SBLGNT places at 7:9 was returned to its own clause
(same section, so the multiset is untouched). **Corpus-wide Greek-in-English
leaks: 0.**

**A known limit of the scanner, worth recording.** It only inspects content-word
units, so it cannot see a verb's or noun's label landing *on* a function word —
the 9:13 and 13:21 cases were invisible to it and surfaced only by pair-reading.
Scanner flags are a starting point, not the audit.

**Verification.** units 117,353 and tokens 137,554 — both unchanged, as every
fix is a pure reorder/regloss. Matthew's remaining 86 DRIFT flags were each read
and judged false positives (irregular English morphology teeth/tooth,
began/begin; proper names; substantival participles and articles).


## 2026-07-18 — Revelation added — THE NEW TESTAMENT IS COMPLETE

Added the **whole book of Revelation (22 chapters, 9,833 SBLGNT words)** — the
throne room, the Lamb, the seals, trumpets, and bowls, the fall of Babylon, the
rider called Faithful and True, the new heaven and new earth, and the final
invitation — in canonical position right after Jude 1, via the book-parametric
pipeline. **This completes the entire New Testament: all 27 books, Matthew
through Revelation, are now present and readable.**

SBLGNT Greek unchanged; every word carries a verified Strong's + morphology tag.
Revelation's rich apocalyptic vocabulary (precious stones, proper names,
hapaxes) needed a 50-entry lemma-override table, each number checked against the
Strong's dict; the SBLGNT readings with no exact headword were mapped to the
honest textual-variant parallel (e.g. ὁμίχλη is not here, but διαυγής→G1307
διαφανής "transparent", κατάθεμα→G2652 κατανάθεμα "curse", φάρμακον→G5331
φαρμακεία "sorcery", ῥυπαρεύω→G4510 ῥυπόω, δισμυριάς→G3461 μυριάς). 120 new
LEXICON and 120 new Abbott-Smith entries. All 22 chapters were authored in
batches and pair-checked for gloss honesty, keeping the doctrinal readings
straight (e.g. "the Word was God"-style subject/predicate care in the divine
titles; the SBLGNT "King of the ages" in 15:3 kept over the familiar "King of
the nations").

**Verification.** Every chapter's Greek token multiset equals SBLGNT; zero
placeholder units; every tag's Strong's number resolves; no straight quotes.
Revelation adds exactly 9,833 tokens (the SBLGNT word count) / 7,853 units. Final
totals: **260 chapters · 117,353 units · 137,554 tokens · LEXICON 5,357 · ABBOTT
5,339**. The great finale lands to voice — "I am the Alpha and the Omega" (1:8;
22:13), "Worthy is the Lamb who was slain" (5:12), "Hallelujah! For the Lord our
God the Almighty reigns" (19:6), "Behold, I am making all things new… He will
wipe away every tear from their eyes" (21:4–5), and the last words of the Bible,
"Come, Lord Jesus! The grace of the Lord Jesus be with all" (22:20–21).

## 2026-07-18 — Jude added

Added the **whole book of Jude (1 chapter, 25 verses, 459 SBLGNT words)** — the
call to contend for the faith, closing with the great doxology — in canonical
position right after 3 John 1, via the book-parametric pipeline. SBLGNT Greek
unchanged; every word carries a verified Strong's + morphology tag (6-entry
override checked against the Strong's dict: παρεισδύω→G3921, ὑπομιμνῄσκω→G5279,
σῴζω→G4982, Κόρε→G2879 "Korah", ἀποθνῄσκω→G599, ἐλεάω→G1653). 17 new LEXICON and
17 new Abbott-Smith entries. Pair-checked for gloss honesty; the harder SBLGNT
reading kept where it differs from the majority text (v5 "Jesus, who saved a
people out of the land of Egypt," Ἰησοῦς rather than the TR κύριος).

**Verification.** The chapter's Greek token multiset equals SBLGNT; zero
placeholder units; every tag's Strong's number resolves; no straight quotes.
Jude adds exactly 459 tokens (the SBLGNT word count) / 404 units. New totals:
**238 chapters · 109,500 units · 127,721 tokens**. The doxology lands to voice —
"Now to him who is able to keep you from stumbling and to present you blameless
before his glory with great joy… be glory, majesty, dominion, and authority"
(v24–25). Only Revelation now remains in the New Testament.

## 2026-07-18 — 3 John added

Added the **whole book of 3 John (1 chapter, 15 verses, 219 SBLGNT words)** — the
elder's note to beloved Gaius, commending hospitality and rebuking Diotrephes —
in canonical position right after 2 John 1, via the book-parametric pipeline.
SBLGNT Greek unchanged; every word carries a verified Strong's + morphology tag
(3-entry override: εὐοδόομαι→G2137 "prosper", Διοτρέφης→G1361 "Diotrephes",
ὑπομιμνῄσκω→G5279). 5 new LEXICON and 5 new Abbott-Smith entries. Pair-checked
for gloss honesty.

**Verification.** The chapter's Greek token multiset equals SBLGNT; zero
placeholder units; every tag's Strong's number resolves; no straight quotes.
3 John adds exactly 219 tokens (the SBLGNT word count) / 176 units. New totals:
**237 chapters · 109,096 units · 127,262 tokens**. "I have no greater joy than
this, that I hear my children walking in the truth" (v4). Only Jude and
Revelation remain in the New Testament.

## 2026-07-18 — 2 John added

Added the **whole book of 2 John (1 chapter, 13 verses, 245 SBLGNT words)** — the
elder's short note to "the elect lady" on truth and love — in canonical position
right after 1 John 5, via the book-parametric pipeline. SBLGNT Greek unchanged;
every word carries a verified Strong's + morphology tag (1-entry override:
κυρία→G2959 "lady"). Only 2 new LEXICON and 2 new Abbott-Smith entries.
Pair-checked for gloss honesty; the SBLGNT reading kept where it differs from
the familiar text (v12 "your joy," ὑμῶν).

**Verification.** The chapter's Greek token multiset equals SBLGNT; zero
placeholder units; every tag's Strong's number resolves; no straight quotes.
2 John adds exactly 245 tokens (the SBLGNT word count) / 210 units. New totals:
**236 chapters · 108,920 units · 127,043 tokens**. "And now I ask you, dear
lady… that we love one another" (v5).

## 2026-07-18 — 1 John added

Added the **whole book of 1 John (5 chapters, 2,137 SBLGNT words)** — the letter
of light, love, and assurance — in canonical position right after 2 Peter 3, via
the book-parametric pipeline. SBLGNT Greek unchanged; every word carries a
verified Strong's + morphology tag. **No lemma-override table was needed** — 1
John's famously spare, repetitive vocabulary resolved entirely by corpus
form-match / app LEXICON / Strong's dict (0 MISS across all 5 chapters). Only 6
new LEXICON and 6 new Abbott-Smith entries. All 5 chapters pair-checked for gloss
honesty, with special care on the doctrinal predicate lines — "God is light"
(1:5) and "God is love" (4:8, 4:16) keep the articular subject and anarthrous
predicate straight (not "light/love is God"), and John's repeated μένω is
rendered "abide" throughout.

**Verification.** Every chapter's Greek token multiset equals SBLGNT; zero
placeholder units; every tag's Strong's number resolves; no straight quotes.
1 John adds exactly 2,137 tokens (the SBLGNT word count) / 1,782 units. New
totals: **235 chapters · 108,710 units · 126,798 tokens**. The signature lines
land to voice — "if we confess our sins, he is faithful and just to forgive us"
(1:9), "See what kind of love the Father has given to us, that we should be
called children of God" (3:1), "God is love" (4:8), and "We love because he
first loved us" (4:19).

## 2026-07-18 — 2 Peter added

Added the **whole book of 2 Peter (3 chapters, 1,098 SBLGNT words)** — the last
letter, on divine power, false teachers, and the day of the Lord — in canonical
position right after 1 Peter 5, via the book-parametric pipeline. SBLGNT Greek
unchanged; every word carries a verified Strong's + morphology tag. A 16-entry
lemma-override table, each number checked against the Strong's dict; the two
SBLGNT readings with no exact headword mapped to the honest textual-variant
parallel (ὁμίχλη→G3507 νεφέλη "cloud" — the TR reading in the same slot of 2:17;
ἐμπαιγμονή→G1701 ἐμπαιγμός "derision"). 61 new LEXICON and 61 new Abbott-Smith
entries (G4412/G3428 kept LEXICON-only, per precedent). All 3 chapters
pair-checked for gloss honesty.

**Verification.** Every chapter's Greek token multiset equals SBLGNT; zero
placeholder units; every tag's Strong's number resolves; no straight quotes.
2 Peter adds exactly 1,098 tokens (the SBLGNT word count) / 950 units. New
totals: **230 chapters · 106,928 units · 124,661 tokens**. The signature lines
land to voice — "his divine power has granted to us all things that pertain to
life and godliness" (1:3), "with the Lord one day is like a thousand years"
(3:8), and "grow in the grace and knowledge of our Lord and Savior Jesus
Christ" (3:18). Both Peters now complete.

## 2026-07-18 — 1 Peter added

Added the **whole book of 1 Peter (5 chapters, 1,678 SBLGNT words)** — the letter
of a living hope and grace under suffering — in canonical position right after
James 5, via the book-parametric pipeline. SBLGNT Greek unchanged; every word
carries a verified Strong's + morphology tag. A 21-entry lemma-override table,
each number checked against the Strong's dict; ταπεινόφρων ("humble-minded")
mapped to its true cognate G5012 ταπεινοφροσύνη ("humility of mind") rather than
the wrong-meaning TR variant φιλόφρων. 62 new LEXICON and 62 new Abbott-Smith
entries (G4412 kept LEXICON-only, per precedent). All 5 chapters pair-checked
for gloss honesty; the SBLGNT reading kept where it differs from the familiar
text (e.g. 3:18 "bring you to God," ὑμᾶς).

**Verification.** Every chapter's Greek token multiset equals SBLGNT; zero
placeholder units; every tag's Strong's number resolves; no straight quotes.
1 Peter adds exactly 1,678 tokens (the SBLGNT word count) / 1,479 units. New
totals: **227 chapters · 105,978 units · 123,563 tokens**. The signature lines
land to voice — "he has caused us to be born again to a living hope" (1:3), "you
are a chosen race, a royal priesthood, a holy nation" (2:9), "casting all your
anxieties on him, because he cares for you" (5:7).

## 2026-07-18 — James added

Added the **whole book of James (5 chapters, 1,739 SBLGNT words)** — the practical
epistle of faith that works — in canonical position right after Hebrews 13, via
the book-parametric pipeline. SBLGNT Greek unchanged; every word carries a
verified Strong's + morphology tag. A 22-entry lemma-override table, each number
checked against the Strong's dict; the four SBLGNT readings with no exact Strong's
headword were mapped to the honest textual-variant parallel (αὐχέω→G3166
μεγαλαυχέω "boast"; κατοικίζω→G2730 κατοικέω "dwell"; μετατρέπω→G3344 μεταστρέφω
"turn/change"; ἀφυστερέω→G650 ἀποστερέω "defraud" — each the TR reading in the
same slot). 72 new LEXICON and 72 new Abbott-Smith entries (G4412/G3428 kept
LEXICON-only, per precedent). All 5 chapters pair-checked for gloss honesty.

**Verification.** Every chapter's Greek token multiset equals SBLGNT; zero
placeholder units; every tag's Strong's number resolves; no straight quotes.
James adds exactly 1,739 tokens (the SBLGNT word count) / 1,516 units. New totals:
**222 chapters · 104,499 units · 121,885 tokens**. The signature lines land to
voice — "Count it all joy… when you meet trials of various kinds" (1:2), "be
doers of the word, and not hearers only" (1:22), "faith apart from works is
dead" (2:26), "the tongue is a fire" (3:6), "Draw near to God, and he will draw
near to you" (4:8), and "the prayer of faith will save the one who is sick" (5:15).

## 2026-07-18 — Hebrews added

Added the **whole book of Hebrews (13 chapters, 4,935 SBLGNT words)** — the great
sermon on Christ our high priest — in canonical position right after Philemon 1,
via the book-parametric pipeline. SBLGNT Greek unchanged; every word carries a
verified Strong's + morphology tag. The book's rich vocabulary needed a 40-entry
lemma-override table, each number checked against the Strong's dict; the three
critical-text hapaxes with no Strong's headword were mapped to the honest
textual-variant parallel (δέος→G127 αἰδώς "awe toward God" — the TR reading in
the same slot of Heb 12:28; δοκιμασία→G1382 δοκιμή "proving"; ἐκβαίνω→G1831
ἐξέρχομαι "go out"). 171 new LEXICON and 171 new Abbott-Smith entries added
(G4055/G4056/G4412/G5126/G5305 kept LEXICON-only, per precedent — Abbott-Smith
has no form-entry for those). The 13 chapters were authored in parallel, each
pair-checked for gloss honesty (several drift spots caught and fixed by the
authors themselves); the harder SBLGNT reading was kept where it differs from
the majority text (e.g. Heb 2:9 "apart from God," χωρὶς θεοῦ).

**Verification.** Every chapter's Greek token multiset equals SBLGNT; zero
placeholder units; every tag's Strong's number resolves; no straight quotes.
Hebrews adds exactly 4,935 tokens (the SBLGNT word count) / 4,113 units. New
totals: **217 chapters · 102,983 units · 120,146 tokens**. The signature lines
land to voice — "the radiance of the glory of God and the exact imprint of his
nature" (1:3), "let us then draw near with confidence to the throne of grace"
(4:16), "Now faith is the assurance of things hoped for" (11:1), "looking to
Jesus, the founder and perfecter of our faith" (12:2), and "Jesus Christ is the
same yesterday and today and forever" (13:8).

## 2026-07-18 — Philemon added

Added the **whole book of Philemon (1 chapter, 25 verses)** — Paul's tender,
personal appeal to receive back the runaway slave Onesimus "no longer as a slave
but more than a slave, a beloved brother" — in canonical position right after
Titus 3, via the book-parametric pipeline. SBLGNT Greek unchanged; every word
carries a verified Strong's + morphology tag (2-entry override table checked
against the Strong's dict: ἑκούσιος→G1595, προσλαμβάνομαι→G4355). 7 new LEXICON
and 7 new Abbott-Smith entries added. The Onesimus wordplay is kept honest —
ἄχρηστον "useless" / εὔχρηστον "useful" (v11), ὀναίμην "gain some benefit" (v20),
both echoing Ὀνήσιμος = "useful" — and Paul's "charge it to my account" warmth (v18).

**Verification.** The chapter's Greek token multiset equals SBLGNT; zero
placeholder units; every tag's Strong's number resolves. Philemon adds exactly
334 tokens (the SBLGNT word count) / 287 units. New totals: **204 chapters ·
98,870 units · 115,211 tokens**.

## 2026-07-18 — Titus added

Added the **whole book of Titus (3 chapters)** — Paul's letter to his true child
in a common faith — in canonical position right after 2 Timothy 4, via the
book-parametric pipeline. SBLGNT Greek unchanged; every word carries a Strong's +
morphology tag grounded in real data (8-entry verified lemma-override table, each
number checked against the Strong's dict: οἰκουργός→G3626, ἀφθορία→G90,
σωτήριος→G4992, λυτρόομαι→G3084, ὑπομιμνῄσκω→G5279, στυγητός→G4767,
ἐκστρέφομαι→G1612, Ἀρτεμᾶς→G734). 34 new LEXICON and 33 new Abbott-Smith entries
added (G90 kept LEXICON-only, per precedent — Abbott-Smith has no form-entry for it).

**Verification.** Every chapter's Greek token multiset equals SBLGNT; zero
placeholder units; every tag's Strong's number resolves. Titus adds exactly
659 tokens (the SBLGNT word count) / 577 units. New totals: **203 chapters ·
98,583 units · 114,877 tokens**. The grace centerpieces read to voice — "the
grace of God has appeared, bringing salvation for all people" (2:11) and "he
saved us … by the washing of regeneration and renewal of the Holy Spirit" (3:5).

## 2026-07-17 — 2 Timothy added; quote style normalized to the corpus

Added the **whole book of 2 Timothy (4 chapters)** — Paul's last letter — in
canonical position right after 1 Timothy 6, via the book-parametric pipeline.
SBLGNT Greek unchanged; every word carries a Strong's + morphology tag grounded
in real data (21-entry verified lemma-override table, each number checked
against the Abbott-Smith TEI and Strong's dict). 75 new LEXICON and 75 new
Abbott-Smith entries added.

**Quote-style cleanup.** The original corpus (Gospels, Acts) uses typographic
curly quotes; the new books had drifted to a mix. Normalized the 34 remaining
straight double-quotes across the nine books built this session (2 Corinthians
through 2 Timothy) to directional curly quotes — English-only, Greek untouched.

**Verification.** Every chapter's Greek token multiset equals SBLGNT; zero
placeholder units; every tag's Strong's number resolves. 2 Timothy adds exactly
1,235 tokens (the SBLGNT word count) / 1,048 units. New totals: **200 chapters ·
98,006 units · 114,218 tokens**.

**Doctrine preserved (representative)**
- 1:7 "God gave us a spirit not of fear but of power and love and
  self-control"; 1:9 "who saved us and called us to a holy calling, not because
  of our works but because of his own purpose and grace"; 1:12 "I know whom I
  have believed."
- 2:11-13 "if we have died with him, we will also live with him… if we are
  faithless, he remains faithful — for he cannot deny himself"; 2:15 "rightly
  handling the word of truth."
- 3:16-17 "All Scripture is breathed out by God and profitable for teaching,
  for reproof, for correction, and for training in righteousness."
- 4:2 "preach the word"; 4:7-8 "I have fought the good fight, I have finished
  the race, I have kept the faith… the crown of righteousness."

## 2026-07-17 — 1 Timothy added (the Pastorals begin)

Added the **whole book of 1 Timothy (6 chapters)**, in canonical position right
after 2 Thessalonians 3, via the book-parametric pipeline. SBLGNT Greek
unchanged; every word carries a Strong's + morphology tag grounded in real data
(21-entry verified lemma-override table, each number checked against the
Abbott-Smith TEI and Strong's dict; SBLGNT compound/variant forms mapped to
their base Strong's headword of identical sense). The Pastorals are
vocabulary-rich: 111 new LEXICON and 111 new Abbott-Smith entries added.

**Verification.** Every chapter's Greek token multiset equals SBLGNT; zero
placeholder units; every tag's Strong's number resolves. 1 Timothy adds exactly
1,591 tokens (the SBLGNT word count) / 1,345 units. New totals: **196 chapters ·
96,958 units · 112,983 tokens**.

**Doctrine preserved (representative)**
- 1:15 "Christ Jesus came into the world to save sinners, of whom I am the
  foremost"; 1:17 "to the King of the ages, immortal, invisible, the only God,
  be honor and glory."
- 2:4-6 "God our Savior, who desires all people to be saved… one mediator
  between God and men, the man Christ Jesus, who gave himself as a ransom."
- 3:16 the mystery of godliness — "manifested in the flesh, vindicated by the
  Spirit, seen by angels… taken up in glory."
- 4:10 "the living God, who is the Savior of all people, especially of those
  who believe."
- 6:6 "godliness with contentment is great gain"; 6:12 "Fight the good fight of
  faith"; 6:15-16 "the King of kings and Lord of lords, who alone has
  immortality."

## 2026-07-17 — 2 Thessalonians added

Added the **whole book of 2 Thessalonians (3 chapters)**, in canonical position
right after 1 Thessalonians 5, via the book-parametric pipeline. SBLGNT Greek
unchanged; every word carries a Strong's + morphology tag grounded in real data
(7-entry verified lemma-override table, each number checked against the
Abbott-Smith TEI and Strong's dict; SBLGNT ἐγκαυχάομαι → G2744 καυχάομαι, its
unprefixed root). 12 new LEXICON and 12 new Abbott-Smith entries added.

**Verification.** Every chapter's Greek token multiset equals SBLGNT; zero
placeholder units; every tag's Strong's number resolves. 2 Thessalonians adds
exactly 820 tokens (the SBLGNT word count) / 638 units. New totals:
**190 chapters · 95,613 units · 111,392 tokens**.

**Doctrine preserved (representative)**
- 1:3 "your faith is growing abundantly"; 1:12 "so that the name of our Lord
  Jesus may be glorified in you, and you in him, according to the grace of our
  God."
- 2:3-4 the man of lawlessness, the son of destruction; 2:13 "God chose you as
  the firstfruits to be saved, through sanctification by the Spirit and belief
  in the truth"; 2:16-17 "who loved us and gave us eternal comfort and good
  hope through grace."
- 3:3 "the Lord is faithful; he will establish you and guard you against the
  evil one"; 3:13 "do not grow weary in doing good"; 3:16 "may the Lord of
  peace himself give you peace at all times in every way."

## 2026-07-17 — 1 Thessalonians added

Added the **whole book of 1 Thessalonians (5 chapters)**, in canonical position
right after Colossians 4, via the book-parametric pipeline. SBLGNT Greek
unchanged; every word carries a Strong's + morphology tag grounded in real data
(12-entry verified lemma-override table, each number checked against the
Abbott-Smith TEI and Strong's dict; SBLGNT ἐνορκίζω → G3726 ὁρκίζω, its
unprefixed root of identical sense). 24 new LEXICON and 24 new Abbott-Smith
entries added.

**Verification.** Every chapter's Greek token multiset equals SBLGNT; zero
placeholder units; every tag's Strong's number resolves. 1 Thessalonians adds
exactly 1,473 tokens (the SBLGNT word count) / 1,186 units. New totals:
**187 chapters · 94,975 units · 110,572 tokens**.

**Doctrine preserved (representative)**
- 1:9-10 "you turned to God from idols to serve the living and true God, and to
  wait for his Son from heaven… Jesus who delivers us from the wrath to come."
- 2:7 "gentle among you, like a nursing mother"; 2:13 "not as the word of men
  but… the word of God."
- 3:12-13 "may the Lord make you increase and abound in love… blameless in
  holiness… at the coming of our Lord Jesus with all his saints."
- 4:16-17 "the Lord himself will descend from heaven… and the dead in Christ
  will rise first… and so we will always be with the Lord."
- 5:16-18 "Rejoice always, pray without ceasing, give thanks in all
  circumstances"; 5:23 "may your whole spirit and soul and body be kept
  blameless… He who calls you is faithful; he will surely do it."

## 2026-07-17 — Colossians added

Added the **whole book of Colossians (4 chapters)**, in canonical position right
after Philippians 4, via the book-parametric pipeline. SBLGNT Greek unchanged;
every word carries a Strong's + morphology tag grounded in real data (10-entry
verified lemma-override table, each number checked against the Abbott-Smith TEI
and Strong's dict). 54 new LEXICON and 54 new Abbott-Smith entries added.

**Verification.** Every chapter's Greek token multiset equals SBLGNT; zero
placeholder units; every tag's Strong's number resolves. Colossians adds exactly
1,580 tokens (the SBLGNT word count) / 1,223 units. New totals: **182 chapters ·
93,789 units · 109,099 tokens**.

**Doctrine preserved (representative)**
- 1:15-20 the Christ-hymn — "He is the image of the invisible God, the
  firstborn of all creation… all things were created through him and for him…
  in him all things hold together… that in everything he might be preeminent…
  making peace by the blood of his cross."
- 1:27 "Christ in you, the hope of glory."
- 2:9 "in him the whole fullness of deity dwells bodily"; 2:14 "nailing it to
  the cross"; 2:15 "triumphing over them."
- 3:1-3 "seek the things that are above… your life is hidden with Christ in
  God"; 3:14 "put on love, the bond of perfect unity"; 3:17 "do everything in
  the name of the Lord Jesus."
- 4:2 "continue steadfastly in prayer"; 4:6 "let your speech… be seasoned with
  salt."

## 2026-07-17 — Philippians added

Added the **whole book of Philippians (4 chapters)**, in canonical position
right after Ephesians 6, via the book-parametric pipeline. SBLGNT Greek
unchanged; every word carries a Strong's + morphology tag grounded in real data
(11-entry verified lemma-override table, each number checked against the
Abbott-Smith TEI and Strong's dict). 57 new LEXICON and 57 new Abbott-Smith
entries added for its vocabulary.

**Verification.** Every chapter's Greek token multiset equals SBLGNT; zero
placeholder units; every tag's Strong's number resolves. Philippians adds
exactly 1,626 tokens (the SBLGNT word count) / 1,265 units. New totals:
**178 chapters · 92,566 units · 107,519 tokens**.

**Doctrine preserved (representative)**
- 1:6 "he who began a good work in you will bring it to completion at the day
  of Christ Jesus"; 1:21 "to me to live is Christ, and to die is gain."
- 2:6-11 the Christ-hymn — "though he existed in the form of God… emptied
  himself, taking the form of a servant… he humbled himself… even death on a
  cross. Therefore God has highly exalted him… that at the name of Jesus every
  knee should bow… and every tongue confess that Jesus Christ is Lord."
- 2:13 "it is God who works in you, both to will and to work for his good
  pleasure."
- 3:8 "the surpassing worth of knowing Christ Jesus my Lord"; 3:10 "that I may
  know him and the power of his resurrection"; 3:20 "our citizenship is in
  heaven."
- 4:6-7 "do not be anxious… the peace of God, which surpasses all
  understanding, will guard your hearts"; 4:13 "I can do all things through him
  who strengthens me"; 4:19 "my God will supply every need of yours."

## 2026-07-17 — Ephesians added

Added the **whole book of Ephesians (6 chapters)**, in canonical position right
after Galatians 6, via the book-parametric pipeline (one `BOOKS` registry entry
plus authoring). SBLGNT Greek unchanged; every word carries a Strong's +
morphology tag grounded in real data (24-entry verified lemma-override table,
each number checked against the Abbott-Smith TEI and Strong's dict;
ὑπερεκπερισσοῦ → G5228, consistent with ὑπερλίαν). 76 new LEXICON and 76 new
Abbott-Smith entries added for its vocabulary.

**Verification.** Every chapter's Greek token multiset equals SBLGNT; zero
placeholder units; every tag's Strong's number resolves. Ephesians adds exactly
2,416 tokens (the SBLGNT word count) / 1,723 units. New totals: **174 chapters ·
91,301 units · 105,893 tokens**.

**Doctrine preserved (representative)**
- 1:3 "blessed us with every spiritual blessing"; 1:7 "redemption through his
  blood"; 1:13 "sealed with the Holy Spirit of promise."
- 2:8-9 "by grace you have been saved through faith… the gift of God, not from
  works, so that no one may boast"; 2:14 "he himself is our peace."
- 3:18-19 "the breadth and length and height and depth… the love of Christ
  that surpasses knowledge."
- 4:4-6 "one body… one Lord, one faith, one baptism, one God and Father of
  all"; 4:32 "Be kind to one another, tenderhearted, forgiving one another."
- 5:2 "walk in love, as Christ loved us and gave himself up for us"; 5:25
  "Husbands, love your wives, as Christ loved the church."
- 6:11 the whole armor of God; 6:17 "the sword of the Spirit, which is the word
  of God."

## 2026-07-17 — Galatians added — the build pipeline is now book-parametric

Added the **whole book of Galatians (6 chapters)**, in canonical position right
after 2 Corinthians 13. Built the same way as 2 Corinthians (SBLGNT Greek
unchanged; every word carries a Strong's + morphology tag grounded in real
data; grace-centered Mak-voice paraphrase in natural reading order, every
phrase anchored; thematic sections with headings).

**Tooling generalized.** The 2 Corinthians build scripts were generalized into
book-parametric `tools/nt_*.py` (`nt_tags`, `nt_words`, `nt_assemble`,
`nt_lex`) driven by a `BOOKS` registry — adding a book is now one registry
entry plus authoring. Galatians resolved fully with an 11-entry verified
lemma-override table (each number checked against the Abbott-Smith TEI and the
Strong's dictionary); 49 new LEXICON and 49 new Abbott-Smith entries added for
its vocabulary (G4056/G5071/G1573 stay LEXICON-only, matching precedent).

**Verification.** Every chapter's Greek token multiset equals SBLGNT; zero
placeholder units; every tag's Strong's number resolves. Galatians adds exactly
2,226 tokens (the SBLGNT word count) / 1,805 units. New totals: **168 chapters ·
89,578 units · 103,477 tokens** (baseline invariants updated).

**Doctrine preserved (representative)**
- 1:8 "even if… an angel from heaven should preach… a gospel other than the
  one we preached, let him be accursed"; 1:15 "set me apart… and called me
  through his grace."
- 2:16 "not justified by works of the law but… through faith in Jesus Christ";
  2:20 "I have been crucified with Christ… who loved me and gave himself for me."
- 3:11 "The righteous shall live by faith"; 3:13 "Christ redeemed us from the
  curse of the law by becoming a curse for us"; 3:28 "you are all one in Christ
  Jesus."
- 4:4-6 "God sent forth his Son… so that we might receive adoption as sons…
  'Abba, Father!'"
- 5:1 "For freedom Christ has set us free"; 5:22-23 the fruit of the Spirit.
- 6:2 "Bear one another's burdens, and so fulfill the law of Christ"; 6:14 "far
  be it from me to boast except in the cross of our Lord Jesus Christ."

## 2026-07-17 — 2 Corinthians added — a new book, built from scratch

Added the **whole book of 2 Corinthians (13 chapters)** — the first book built
new rather than reordered from an existing wooden block. It sits in canonical
position, right after 1 Corinthians 16; the nav picks up the new book group
automatically.

**How it was built (nothing invented)**
- **Greek:** SBLGNT via MorphGNT — 4,473 words, unchanged from source.
- **Tags:** every word carries a Strong's + morphology tag. ~88% inherit their
  exact tag from the app's own already-tagged corpus (2 Cor shares almost all
  its vocabulary with Matthew–1 Cor + Romans); the rest resolve via the app
  LEXICON, a 34-entry verified lemma-override table (deponents / critical-text
  spellings, each checked against the Abbott-Smith TEI and the Strong's Greek
  dictionary), or the Strong's dictionary directly.
- **Lexicon:** 145 new Strong's/Thayer's (LEXICON) and 144 new Abbott–Smith
  (ABBOTT) entries for vocabulary the earlier corpus never used, generated from
  the same public-domain sources the app's own blobs were built from, with
  parsers validated to reproduce existing entries exactly. Five Strong's
  form/comparative numbers (toúton, prṓton, perissóteros/-ōs, enkakéō) stay
  LEXICON-only, matching how the existing books already treat them.
- **English:** grace-centered, thought-for-thought Mak-voice paraphrase written
  fresh, in natural English reading order, every phrase anchored to its Greek
  word(s), each chapter split into thematic sections with headings.

**Verification**
- Every chapter's Greek token multiset verified equal to SBLGNT.
- Zero placeholder / empty units; every tag's Strong's number resolves in the
  LEXICON.
- Greek tokens: **101,251** (+4,473) · word units: **87,773** (+3,483) ·
  chapters: **162** (+13). Baseline invariants updated to match.

**Doctrine preserved (representative)**
- 1:3-4 "the Father of mercies and the God of all comfort"; 1:20 "all the
  promises of God in him are Yes."
- 3:6 "the letter kills, but the Spirit gives life"; 3:17 "where the Spirit of
  the Lord is, there is freedom"; 3:18 "from glory to glory."
- 4:6 "the light of the knowledge of the glory of God in the face of Christ";
  4:7 "treasure in clay jars"; 4:17 "an eternal weight of glory."
- 5:7 "we walk by faith, not by sight"; 5:17 "a new creation"; 5:19 "God was in
  Christ reconciling the world to himself"; 5:21 "he made him who knew no sin to
  be sin, so that in him we might become the righteousness of God."
- 8:9 "though he was rich, yet for your sake he became poor."
- 9:7 "God loves a cheerful giver"; 9:15 "his indescribable gift."
- 10:5 "take captive every thought into obedience to Christ."
- 12:9 "My grace is sufficient for you, for power is made perfect in weakness";
  12:10 "when I am weak, then I am strong."
- 13:14 "The grace of the Lord Jesus Christ, and the love of God, and the
  fellowship of the Holy Spirit be with all of you."

## 2026-07-17 — Acts 1–12 complete — whole corpus now readable

Finished reordering **Acts 1–12** from Greek word order into natural English
reading order. With Acts 13–28 already readable, **all of Acts now reads as
English prose**, and every chapter of the current corpus (Matthew, Mark, Luke,
John, Acts, Romans, 1 Corinthians — 149 chapters) is readable.

Acts was worked as a **doctrinal** pass alongside the stylistic one, since its
sermons carry the theological weight of the early church.

**Doctrine preserved (representative)**
- 1:8 "you will be my witnesses... to the end of the earth"; 1:11 the return.
- 2: Pentecost, the Joel citation, Psalms 16 & 110; 2:36 "God has made him
  both Lord and Christ, this Jesus whom you crucified"; 2:38 "Repent and be
  baptized... the gift of the Holy Spirit."
- 3:15 "you killed the Author of life, whom God raised"; 4:12 "no other name
  under heaven... by which we must be saved."
- 5:29 "We must obey God rather than men."
- 7: Stephen's speech and martyrdom; "I see the Son of Man standing at the
  right hand of God"; "Lord Jesus, receive my spirit."
- 8: the Isaiah 53 citation; Philip "preached the good news of Jesus."
- 9:5 "I am Jesus, whom you are persecuting"; 9:15 "a chosen vessel."
- 10:34-35 "God shows no partiality... in every nation the one who fears him
  and works righteousness is acceptable"; 10:36 "Lord of all"; the Spirit
  poured out on the Gentiles.
- 11:17 "who was I to hinder God?"; 12:23 the angel strikes Herod "because he
  did not give the glory to God."

**Method (per section)**
- Reordered wooden Greek-order clauses; fixed postposed genitives, verb–subject
  inversions, split numbers, doubled articles.
- Cleared **all standalone `—` article placeholders** across Acts 1–12 (0 remain).
- Restored quote marks / sentence punctuation dropped during reorder, caught in
  the prose read-back before each write.

**Invariants held every section (verified by pair-reading + scripts)**
- Greek tokens: **96,778** (unchanged) · word units: **84,290** (unchanged)
- All 4 JSON data blobs parse · Greek multiset never changed — only English
  order and article folds.

Outstanding: the P0 gloss-drift audit still owed on **Matthew + Mark** (they
were reordered before the pair-checking discipline existed).

## 2026-07-17 — Gospel of John complete (doctrinal read)

Finished reordering the Gospel of **John** (all 21 chapters) from Greek
word order into natural English reading order. John was worked as a
**doctrinal** pass — not merely a stylistic one — because naive reordering
can corrupt doctrinally-loaded verses. Every Christological and theological
statement was checked as it was reordered.

**Doctrine preserved (representative)**
- 1:1 "the Word was God"; 4:24 "God is spirit" (the articular noun is the
  subject — an earlier "Spirit is God" reversal was corrected).
- The "I am" (ἐγώ εἰμι) sayings, incl. the arrest "I am" (18:5–8).
- 18:36 "My kingdom is not of this world"; 18:37 "to testify to the truth."
- 19:7 "he made himself the Son of God"; 19:11 "no authority unless given
  from above"; 19:30 "It is finished."
- 20:17 "my Father and your Father, my God and your God"; 20:28 "My Lord
  and my God"; 20:31 the purpose statement.
- 21: the threefold restoration of Peter, keeping the gloss's
  **ἀγαπάω / φιλέω** distinction ("do you love" vs "have affection for").

**What changed in the text**
- Reordered wooden Greek-order clauses into English order, fixed postposed
  genitives, verb–subject inversions, and postposed δέ ("now").
- Cleared **all standalone `—` article placeholders** across John 18–21 by
  folding each Greek article into an adjacent unit (0 standalone `—` remain).
- Restored quote marks / sentence punctuation dropped during reorder,
  caught in the prose read-back before each write.

**Invariants held every section (verified by pair-reading + scripts)**
- Greek tokens: **96,778** (unchanged) · word units: **84,290** (unchanged)
- All 4 JSON data blobs parse · Greek multiset never changed — only English
  order and article folds.

Remaining: **Acts 1–12** (Acts 13–28 already reads well).

## 2026-07-16 — Gospel of Luke complete (readable, Greek-accurate)

Finished reordering the Gospel of **Luke** from Greek word order into
natural English reading order. Luke 6 §4 through Luke 24 §3 were
completed this session (Luke 1–5 and Luke 6 §0–§3 were already done),
so **all 24 chapters of Luke now read as English prose** while every
gloss stays anchored to the Greek word beneath it.

**What changed in the text**
- Reordered wooden Greek-order clauses into English order
  ("there followed him crowds large" → "large crowds followed him").
- Fixed postposed genitives ("the father of his" → "his father"),
  verb–subject inversions, and postposed δέ ("now").
- Cleared **all 77 `—` article placeholders in Luke** by folding each
  Greek article into its adjacent unit (0 standalone `—` remain in Luke).
- De-duplicated doubled articles ("the calf the fattened one").

**Invariants held every section (verified by pair-reading + scripts)**
- Greek tokens: **96,778** (unchanged) · word units: **84,290** (unchanged)
- All 4 JSON data blobs parse · 4 SBLGNT discrepancies (all Romans, untouched)
- Greek multiset never changed — only English order and article folds.

**Tooling**
- Added a persistent `tools/` folder with reusable utilities
  (`epcore.py`, `apply_plan.py`, `baseline.py`, `dump_section.py`,
  `pair_print.py`) plus per-section plan modules in `tools/plans/`.
  Each plan is a pure data description of one section's reorder; every
  plan was dry-run and pair-read before writing to `index.html`.
- Added `.claude/settings.json` permission allowlist for autonomous
  read-only verification and Git read commands.

**Committed per chapter** (Luke 6 §4 → Luke 24) as safety checkpoints.

## Initial migration from Claude.ai to Claude Code.
