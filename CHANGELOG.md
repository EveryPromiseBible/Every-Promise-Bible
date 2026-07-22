# CHANGELOG

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
