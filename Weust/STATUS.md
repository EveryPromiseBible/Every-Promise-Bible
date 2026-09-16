# Wuest word-study commentary — status

## What this is

Original, verse-by-verse Greek word-study commentary, informed by Kenneth
Wuest's *Word Studies in the Greek New Testament* but **not** a reword or
paraphrase of his text. Wuest chose which Greek words in a verse are worth
stopping on — that selection is followed. The explanation of each word (what
it means, what its tense/case/mood implies, why it matters) is freshly
composed from those grammatical facts, in original sentences, with his own
prose and his citations of other scholars (Robertson, Vincent, Thayer,
Swete, etc.) set aside entirely and never quoted or closely paraphrased.

Each verse entry has two parts:
- **`text`** — the word-by-word commentary, one call-out per Greek word/
  phrase worth noting, in source-verse order.
- **`translation`** — a fresh, original, deliberately literal rendering of
  the verse that bakes the grammatical nuance (tense, mood, voice) directly
  into the English verb constructions rather than smoothing it into normal
  fluent prose — composed independently from the `text` field's grammatical
  facts, not from Wuest's own translation lines.

Wuest covered 16 books of the New Testament with this kind of running
commentary (the rest of his compilation is a separate vocabulary list and
several topical essay collections, out of scope here). This directory holds
one JSON file per finished book: `[{ "label": "Book C:V", "text": "...",
"translation": "..." }, ...]`, one entry per verse or small verse-range,
matching however Wuest himself grouped that discussion.

**Nothing of Wuest's own text is stored anywhere in this repo** — only the
original commentary and translations built from it.

## Progress — 16 of 16 books done, 1,185 entries

All books Wuest covered with running verse-by-verse commentary are now
finished.

| Book | Entries | Status |
|---|---:|---|
| Mark | 364 | done |
| Romans | 156 | done |
| Galatians | 142 | done |
| Ephesians | 66 | done |
| Philippians | 52 | done |
| Colossians | 44 | done |
| Titus | 21 | done |
| Hebrews | 155 | done |
| 1 Timothy | 42 | done |
| 2 Timothy | 35 | done |
| 1 Peter | 46 | done |
| 2 Peter | 21 | done |
| 1 John | 24 | done |
| 2 John | 4 | done |
| 3 John | 4 | done |
| Jude | 9 | done |

Every entry's `text` field has a blank-line break inserted before each
sentence that introduces a new quoted word/phrase not yet discussed in
that entry — retrofitted onto the first 10 books, built in from the start
for the last 6. A structure pass across all 16 files (every entry has
exactly `label`/`text`/`translation`, both fields non-empty, full verse
coverage per book with no gaps or duplicate labels) has been run and
passes clean as of this commit.

## Next steps

1. Run a closer human/editorial QA pass on a larger sample than the
   automated structural check covers — spot-check several entries per
   book for tone consistency and confirm nothing reads as a close
   paraphrase of Wuest's own prose or his citations of other scholars.
2. Design and build the site integration — most likely a tab in the
   Library alongside the translations, plus a "personal" row in the
   word-lookup popup that jumps straight to a tapped word's verse
   commentary when one exists (mirroring how Strong's/Thayer's/
   Abbott-Smith already work), falling back to a searchable index when it
   doesn't. Because this is original writing rather than reproduced text,
   none of the earlier passphrase/private-Worker/personal-only machinery
   is needed — it can just be a normal public feature.

This directory is source material; the compiled, site-facing copy lives in
`data/weust.js` (`const WEUST = {"BookName": [entries...], ...}`), wired
into `index.html`'s word-lookup popup (`weustVerseLookup`, `renderWeust`) —
each entry keyed by verse label, one call-out group per verse under a
"Commentaries" fold alongside Grace Commentary.

## Tense audit against the actual Greek — Romans (156/156 checked)

Every entry's word-selection has always been "informed by Wuest but not
verified against Wuest's actual book" (see the top of this file) — the
grammatical claims (tense, mood, voice) were reasoned out at authoring time
but never checked against a real tagged Greek text. Asked to actually check
one, starting from a flagged concern at Romans 5:17.

The repo already has real ground truth for this: `tools/data/66-Ro-morphgnt.txt`
(SBLGNT via MorphGNT) tags every word's part of speech, tense, voice, and
mood. Built a one-off script pulling every verb/participle per verse,
flagged the categories most likely to carry tense-critical nuance if missed
(present participles, perfects, imperfects, subjunctives — 80 of 156 entries
had at least one), and read through all of them checking whether the
`translation` field's English verb construction actually reflects that
tense's force, the same way an editor would with a Greek text open beside
the draft.

Most of Romans was already sound — durative present participles regularly
got "keeps on," "is continually," "habitually," or a plain progressive;
perfects regularly got "have/has ___-ed, and it stands"-style completed-
with-present-result phrasing; stative verbs (*oida*, *thelō*, *echō*) were
correctly left as plain English present, since English doesn't have a
natural progressive for "know"/"want"/"have." Two real misses found and
fixed:

1. **5:17 — "those who receive" dropped the tense entirely.** *Lambanontes*
   (λαμβάνοντες) is a present participle, durative, deliberately contrasted
   with the aorist "reigned" one clause earlier (death seized the throne in
   one decisive act; grace is pictured as something laid hold of
   continuously). The `text` field never even mentioned this participle.
   Fixed the translation to "those who **are receiving**" and added the
   contrast to the commentary.
2. **13:2 — the same verb given two different tense treatments in one
   verse.** *Anthistēmi* (ἀνθίστημι) appears twice: the indicative
   ("resisteth the ordinance of God") was correctly rendered with its
   perfect force ("has set himself in **permanent opposition**"), but the
   participle three words later ("they that resist") — same lemma, same
   perfect tense — was flattened to a plain present, "those who are so
   opposing." Fixed to "those who **stand in that permanent opposition**,"
   matching the perfect-force phrasing already used for the first
   occurrence in the same verse.

Re-verified: still 156/156 entries, re-spliced into `data/weust.js`, and
confirmed live via `weustVerseLookup()` in a running instance of the site —
1,077 total entries across all 10 currently-compiled books, zero structural
errors.

## Tense audit against the actual Greek — Mark (364/364 checked, clean)

Same method, against `tools/data/62-Mk-morphgnt.txt`. 276 of 364 entries had
at least one present participle, perfect, imperfect, or subjunctive worth
checking — a much higher share than Romans, since Mark's narrative style
leans hard on participles and Wuest's own commentary tracks that closely.
Read through every one of them against the translation.

**No fixes needed.** The book was already handling this well and
consistently: imperfects almost always got "kept on ___-ing" or "was
continually ___-ing" (not just a flat English past); perfects regularly got
the "has ___-ed, and stands/remains so" double phrasing (5:34's "your faith
has saved you, and the salvation stands"; 7:29's "the demon has gone out...
and remains gone"; 11:21's "has withered away"); stative verbs (*oida*,
*echō*, *eimi*) were left as plain English present/past rather than forced
into an awkward progressive, matching how Romans handles the same verbs.
Historical presents (very frequent in Mark's Greek) were correctly left as
Wuest himself renders them — his real practice keeps many of them ("and
they come," "and he says to them") rather than smoothing every one into
past tense, and that's what's reflected here too.

## Tense audit against the actual Greek — Galatians (142/142 checked)

Same method, against `tools/data/69-Ga-morphgnt.txt`. 79 of 142 entries had
a present participle, perfect, imperfect, or subjunctive worth checking.

One real fix, and it's the same *shape* of miss as Romans 13:2 — the same
verb given two different tense treatments within one short letter. 5:2-3
correctly makes a point of *peritemnō*'s (περιτέμνω) present-tense
participle: "the participle for 'circumcised' is present tense, aimed at
anyone in the act of receiving the rite, not at those already done." But
6:13 — same lemma, same present participle in the source Greek
(*peritemnomenoi*, περιτεμνόμενοι) — was rendered "those who **are
circumcised**," reading like a settled past state rather than an ongoing
one, and the commentary never mentioned the tense at all. Fixed the
translation to "those who **are having themselves circumcised**," matching
5:3's phrasing exactly, and added a note to the commentary pointing back to
5:2-3 so the parallel is explicit.

## Tense audit against the actual Greek — Ephesians (66/66 checked, clean)

Same method, against `tools/data/70-Eph-morphgnt.txt`. 40 of 66 entries
flagged. **No fixes needed** — if anything this book is where the project's
handling of the perfect tense is at its best, since Ephesians is full of
Wuest's signature territory (positional truth, "by grace you have been
saved"): 2:5/2:8's "you have been in a saved state ... and you remain so"
and 4:18's "who have been permanently darkened ... who stand alienated"
both nail the perfect's completed-action-with-abiding-result force exactly.

## Tense audit against the actual Greek — Philippians (52/52 checked, clean)

Same method, against `tools/data/71-Php-morphgnt.txt`. 28 of 52 entries
flagged. **No fixes needed.** Notably clean handling of *hyparchō*
(ὑπάρχω) at 2:6 — "who, **continuing to subsist** in the outward expression
of God" — which is the classic Wuest crux verse: *hyparchō* implies a prior,
continuing essential state, not the plain copula *eimi* would give, and the
distinction is preserved correctly. *Peithō*'s (πείθω) perfect participle
also recurs three times (1:6, 1:14, 1:25) and gets the same "settled
persuasion/conviction" treatment every time — the kind of same-verb
consistency Romans 13:2 and Galatians 6:13 missed.

## Tense audit against the actual Greek — Colossians (44/44 checked, clean)

Same method, against `tools/data/72-Col-morphgnt.txt`. 26 of 44 entries
flagged. **No fixes needed** — this book has some of the most consistent
perfect-tense handling in the whole corpus: 1:16's "stand created," 1:23's
"having been placed on a foundation with the present result that you stand
firmly grounded," 2:10's "having been completely filled full, with the
present result that you stand in a state of fulness," and 4:2's "I have
been bound and remain bound" all spell out the completed-action-with-
abiding-result force explicitly rather than leaving it implicit.

## Tense audit against the actual Greek — Titus (21/21 checked, clean)

Same method, against `tools/data/77-Tit-morphgnt.txt`. 19 of 21 entries
flagged. **No fixes needed** — 1:15's "have been defiled" and 3:11's "has
been twisted out of joint ... standing self-condemned" both handle the
perfect correctly.

## Tense audit against the actual Greek — Hebrews (155/155 checked, clean)

Same method, against `tools/data/79-Heb-morphgnt.txt`. 104 of 155
entries flagged — Hebrews is grammatically dense and heavy on the perfect
tense (its whole argument leans on completed-with-abiding-result
theology). **No fixes needed.** 10:10's "we have been made holy, and stand
holy still," 12:2's "has sat down and remains seated," and 13:23's "has
been set free and remains so" are all excellent, precise handling of
exactly the tense the book's argument depends on most.

## Tense audit against the actual Greek — 1 & 2 Timothy (42 + 35 checked, clean)

Same method, against `tools/data/75-1Ti-morphgnt.txt` and
`tools/data/76-2Ti-morphgnt.txt`. 27 of 42 and 24 of 35 entries flagged
respectively. **No fixes needed in either.** 2 Timothy in particular is a
standout: 2:19's "God's firm foundation has stood, and stands now," 4:7's
"I have fought the good fight to its finish, and I am resting now in its
victory," and 4:8's "who have set their love, and kept it set, on his
appearing" all handle the perfect with real precision.

This closes out the audit of every book currently compiled into
`data/weust.js` (10 of 16): **3 fixes total across 1,077 entries** — Romans
5:17, Romans 13:2, Galatians 6:13 — the rest (Mark, Ephesians, Philippians,
Colossians, Titus, Hebrews, 1 & 2 Timothy) came back clean.

**Remaining work:** 1 & 2 Peter, 1-3 John, and Jude are finished in
`Weust/*.json` but were never compiled into `data/weust.js` at all (a
separate gap found during this audit, unrelated to tense — see the top of
this file). They need both the tense audit and the compile step. Next up:
1 Peter.
