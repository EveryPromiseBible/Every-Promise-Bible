# Every Promise

A Bible built to be two things at once, where both are required:

> **Easy to read** — can you follow it without stopping?
> **Honest underneath** — does every English word describe the Greek word beneath it?

A beautiful sentence with the wrong word under it is a broken product, not a
stylistic quibble. Everything in this repository exists to keep both true at the
same time.

**Everything here is open source** — the app, the four texts, the lexicons, the
hymnal, the tools that assembled every file, and the commit history recording
each correction and the reason for it.

Live at <https://everypromisebible.com> · on Google Play as **Every Promise**.

---

## The four texts

### The Mak Translation — `tx.01`

A **word-for-word** English New Testament laid over the SBLGNT. Every English
word sits on the specific Greek word it came from, so tapping a word tells you
what *that word* means rather than what the sentence roughly means.

Each word renders as a three-line stack — the English, its Greek, and the
Strong's number with the grammar. Words supplied for the sake of English, with
no Greek behind them, are set in **black italic**, so a reader can always see
what came from the text and what did not.

The English is arranged in **English** order rather than Greek order, which is
what makes it readable. The Greek order stays recoverable from the tags, and the
invariant that must never break is that every Greek word appears exactly once.

| | |
|---|---|
| Chapters | 260 — the complete New Testament |
| Sections | 1,190 |
| Word units | 117,353 |
| Greek tokens | 137,554 |

### The Illumination Translation — `tx.02`

A different job entirely. Where Mak is anchored to the Greek word by word, the
Illumination is **free prose**: a loose, thought-for-thought paraphrase of the
whole Bible in original modern English, composed from the public-domain 1769
Authorized Version.

It is built for a reader who finds older translations hard going — long passages
with no signposts, sentences whose shape has drifted out of modern English. So
it is **organised by subject**. Every chapter carries a title, every section a
heading, and verses are grouped into blocks of a single thought rather than
chopped into numbered fragments. Each book opens with a synopsis of its own.

| | |
|---|---|
| Books | 66 — Old and New Testament |
| Chapters | 1,189 |
| Sections | 5,282, each with its own heading |
| Verse blocks | 9,031 |
| Book synopses | 66 |

**On its underlying text.** Because it was composed from the 1769 Authorized
Version, it follows the Greek text the King James translators used. The Mak
interlinear follows the SBLGNT, a modern critical edition. The two differ in a
handful of well-known places, so a verse can read differently here than in the
interlinear. That is a difference of underlying manuscripts, not of carelessness,
and it is stated in the app as well as here.

### The King James Version — `tx.03`

The Authorized Version of 1769, unedited: 66 books, 1,189 chapters. It is here so
the older wording is always a tap away, and so the Illumination can be read
against the text it was made from.

### The Thirteenth Disciple — `dv.01`

Not a translation but a devotional — *a gospel narrative in thirty-one days*,
walking beside Jesus from the Jordan to the Ascension. Original work, roughly
32,000 words.

Each day carries the **harmony** of gospel passages it draws on, so a reader can
go and read the accounts being retold rather than taking the retelling's word for
it. Days are narrative prose, read straight through rather than looked up.

---

## Around the texts

**Promises** — 2,093 verses, each with 15 short meditations, hand-tagged across
17 moods so they can be filtered by how a reader is actually feeling. Every
verse is checked against the KJV rather than trusted: `tools/kjv.py --verify`.

**Hymns** — 1,323 from *The Christian Hymn Book* (Cincinnati, 1870), public
domain, 25,154 lines. Indexed by first line, as hymnals have always been.

**Journal** — a month calendar, six reading plans computed from the corpus so
they cannot drift out of step with it, a daily reflection, and sermon notes with
formatting.

**My Stuff** — highlights, notes, bookmarks, journal entries, favourites and the
meditations a reader wrote, each on its own page, each linking back to the exact
word or verse. And a backup file: everything written, in one `.json` the reader
keeps.

Nothing a reader writes leaves their device. No accounts, no sign-in, no
analytics, no tracking.

---

## Why the Greek can be trusted

Rearranging English is exactly what can leave a label sitting on the wrong Greek
word. So the claims here are checkable rather than asserted.

| | Greek here | Greek in SBLGNT |
|---|---|---|
| All 27 books | **137,554** | **137,554** |

Every book matches individually. Not one Greek word has been added, removed, or
moved between chapters.

```bash
python tools/wordcounts.py     # Greek word counts vs SBLGNT, book by book
python tools/kjv.py --verify   # every promise verse against the KJV
python tools/swap_scan.py      # finds English labels on the wrong Greek word
python tools/prose_scan.py     # mechanical prose defects
python tools/hymns_build.py    # rebuilds the hymnal from its source
```

`CHANGELOG.md` records every correction, **including the mistakes found in this
project's own earlier work** — a whole sentence of Paul's that had been
overwritten, four pairs of glosses wearing each other's labels, a name tagged as
the wrong person, three misquoted verses. They are documented rather than quietly
fixed, because a translation you cannot audit is one you have to take on faith
twice.

## What is in here

```
index.html              the entire app — no framework, no build step
data/chapters.js        the Mak interlinear (260 chapters)
data/illumination.js    the Illumination (66 books)
data/kjv.js             the Authorized Version, 1769
data/devotional.js      The Thirteenth Disciple (31 days)
data/hymns.js           1,323 public-domain hymns
data/promises.js        2,093 promises, 31,395 meditations
data/lexicon.js         Strong's / Thayer's — 5,367 entries
data/thayer.js          the full Thayer's entries
data/abbott.js          Abbott-Smith — 5,340 entries
data/wordpictures.js    word pictures
data/commentary.js      commentary notes
data/wordcounts.js      generated proof table
tools/                  the checking and build tooling (Python)
```

About 27 MB of data behind a 230 KB app. The service worker caches it, so after
one visit the whole thing works with no connection.

## Running it locally

```bash
python -m http.server 8000
```

Then open <http://localhost:8000>. Do not just double-click `index.html` — the
data loads from a subdirectory and some browsers block that on `file://`.

Deployment is in [DEPLOY.md](DEPLOY.md). The Android app is a Trusted Web
Activity around this site, so publishing here publishes there: no rebuild, no
store review.

## How it was made

The Mak Translation, the Illumination and The Thirteenth Disciple were produced
with **Claude (Anthropic)** — most recently **Claude Opus 5** — working against
the SBLGNT, MorphGNT, Strong's, Thayer's and Abbott-Smith. The work spans many
sessions and successive model versions; Opus 5 is the current one, not the only
one that touched it. The tooling in `tools/` exists because a language
model will produce fluent, confident, wrong output, and fluency is not evidence.
Every check in this repository was calibrated against known defects before its
verdicts were trusted.

As these models improve, the text can be revised again — the checks that protect
the Greek are automated and re-runnable.

## Honest limitations

- **The prose has had one full pass.** All 1,190 Mak sections were read and
  repaired, but a second reading would find more.
- **The invisible defect class is narrowed, not closed.** `swap_scan.py` detects
  English labels that have swapped places, but cannot see a swap where the wrong
  label is a common word, and it only looks within a small window.
- **The Illumination has had no equivalent audit.** It has no word-level Greek
  anchoring, so the checks that protect Mak do not apply to it and cannot.
- **Meditation quality is guarded by reading, not tooling.** The validator checks
  structure — 15 entries, no duplicates — not whether a line is good.
- **Some editorial choices are deliberate and arguable.** A few verses quote a
  contiguous clause rather than a whole verse; five KJV quotations keep
  modernised archaisms. `CREDITS.md` states these.

Corrections are welcome. If something reads wrongly, or a label sits on the wrong
word, open an issue.

## License

| Part | License |
|---|---|
| Code (`tools/`, the app) | MIT — [LICENSE](LICENSE) |
| Translation and data (`data/*.js`) | CC BY-SA 4.0 — [LICENSE-DATA](LICENSE-DATA) |

They differ because the morphology derives from MorphGNT, which is ShareAlike —
so this text cannot be enclosed. Anyone may use, improve or build on it, but no
one can take it, change it, and lock the result away.

Full attribution and the statement of modifications: [CREDITS.md](CREDITS.md).
