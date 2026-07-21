# Every Promise — the Mak Translation

An interlinear Greek New Testament built on a single rule:

> **Every English word sits on the specific Greek word it came from.**

Tap any Greek word and the popup tells you what *that word* means — not what the
sentence roughly means. The English is arranged to read naturally rather than to
copy Greek word order, and the Greek underneath is unchanged.

Alongside it every promise from across the Bible, each with 15 short
meditations, filterable by how you are actually feeling.

---

## Why the Greek can be trusted

Rearranging English is exactly what can leave a label sitting on the wrong Greek
word. So the claims here are made checkable rather than asserted.

| | Greek here | Greek in SBLGNT |
|---|---|---|
| All 27 books | **137,554** | **137,554** |

Every book matches individually. Not one Greek word has been added, removed, or
moved between chapters. English runs about 1.29× the Greek — 177,853 words —
which is why it needs more room to say the same thing.

Run it yourself:

```bash
python tools/wordcounts.py     # Greek word counts vs SBLGNT, book by book
python tools/kjv.py --verify   # every promise verse against the KJV
python tools/swap_scan.py      # finds English labels on the wrong Greek word
python tools/prose_scan.py     # mechanical prose defects
```

`CHANGELOG.md` records every correction, **including the mistakes found in this
project's own earlier work** — a whole sentence of Paul's that had been
overwritten, four pairs of glosses wearing each other's labels, a name tagged as
the wrong person, three misquoted verses. They are documented rather than
quietly fixed, because a translation you cannot audit is one you have to take on
faith twice.

## What is in here

```
index.html            the entire app — no framework, no build step
data/chapters.js      the interlinear New Testament (260 chapters, 1,190 sections)
data/lexicon.js       Strong's / Thayer's entries
data/abbott.js        Abbott-Smith entries
data/promises.js      Every Bible Promise, with  meditations
data/wordcounts.js    generated proof table
tools/                the checking and translation tooling (Python)
```

## Running it locally

```bash
python -m http.server 8000
```

Then open <http://localhost:8000>. Do not just double-click `index.html` — the
data loads from a subdirectory and some browsers block that on `file://`.

Deployment instructions are in [DEPLOY.md](DEPLOY.md).

## How it was made

The translation was produced with **Claude (Anthropic) Fable 5**, working against the
SBLGNT, MorphGNT, Strong's, Thayer's and Abbott-Smith. The tooling in `tools/`
exists because a language model will produce fluent, confident, wrong output,
and fluency is not evidence. Every check in this repository was calibrated
against known defects before its verdicts were trusted.

As these models improve, the text can be revised again — the checks that protect
the Greek are automated and re-runnable.

## Honest limitations

- **The prose has had one full pass.** All 1,190 sections were read and repaired.
- **The invisible defect class is narrowed.** `swap_scan.py` detects
  English labels that have swapped places.
- **Meditation quality is guarded by reading, not tooling.** The validator checks
  structure — 15 entries, no duplicates — not whether a line is good.
- **Some editorial choices are deliberate and arguable.** A few verses quote a
  contiguous clause rather than a whole verse; five KJV quotations keep
  modernised archaisms. `CREDITS.md` states these.

Corrections are welcome. If something reads wrongly, or a label sits on the
wrong word, open an issue.

## License

| Part | License |
|---|---|
| Code (`tools/`, the app) | MIT — [LICENSE](LICENSE) |
| Translation and data (`data/*.js`) | CC BY-SA 4.0 — [LICENSE-DATA](LICENSE-DATA) |

They differ because the morphology derives from MorphGNT, which is ShareAlike —
so this text cannot be enclosed. Anyone may use, improve or build on it, but no
one can take it, change it, and lock the result away.

Full attribution and the statement of modifications: [CREDITS.md](CREDITS.md).
