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

Nothing here is wired into `index.html` yet. This directory is source
material only.
