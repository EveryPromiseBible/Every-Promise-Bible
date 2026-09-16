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

**Not yet audited this way:** Mark, Galatians, Ephesians, Philippians,
Colossians, Titus, Hebrews, 1 & 2 Timothy (compiled into `data/weust.js`
but not yet checked against MorphGNT), and 1 & 2 Peter, 1-3 John, Jude
(finished in `Weust/*.json` but not yet compiled into `data/weust.js` at
all — `data/weust.js` currently has 10 of the 16 books). Next up: Mark.
