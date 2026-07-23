# Credits and sources

Every Promise is built on freely licensed scholarly work. This file records what
was used, under what terms, and — as CC BY requires — **what was changed.**

## Licensing at a glance

| Part of this repository | License |
|---|---|
| Code (`tools/`, the app code in `index.html`) | MIT — see [LICENSE](LICENSE) |
| Translation and data (`data/*.js`) | CC BY-SA 4.0 — see [LICENSE-DATA](LICENSE-DATA) |

The two differ because the data builds on a ShareAlike source. See LICENSE-DATA.

---

## Greek text — SBLGNT

**The Greek New Testament: SBL Edition**, edited by Michael W. Holmes.
Society of Biblical Literature and Logos Bible Software.
<https://sblgnt.com> — licensed **CC BY 4.0**.

The complete SBLGNT text is embedded in `data/chapters.js`.

**Modifications to the Greek text: none.** The Greek is reproduced word for
word. This is checked mechanically rather than asserted: `tools/wordcounts.py`
compares this app's Greek word count against the source for all 27 books, and
the introduction above Matthew 1 publishes the result.

| | Greek here | Greek in SBLGNT |
|---|---|---|
| All 27 books | 137,554 | 137,554 |

Every book matches individually. What *has* been added alongside the Greek is an
English rendering and reference tags; the Greek words themselves are unaltered
and no word has been added, removed, or moved between chapters.

## Morphology — MorphGNT

**MorphGNT SBLGNT**, morphological parsing and lemmatization.
<https://github.com/morphgnt/sblgnt> — licensed **CC BY-SA 3.0**.

The grammar codes on each word (`V-AAI-3S`, `N-GEN`, `ART` and so on) derive
from MorphGNT. **This is the source whose ShareAlike condition determines the
license of the data in this project.**

**Modifications:** parsing codes are carried across as published. They were used
to verify Strong's number assignments, which corrected 224 wrong tags plus a
further handful found later; those corrections are to *this project's* tags, not
to MorphGNT's data.

## Lexicons

**Strong's Exhaustive Concordance** (1890) — public domain. Assembled into
`data/lexicon.js`.

**Thayer's Greek-English Lexicon of the New Testament**, Joseph Henry Thayer
(1889) — public domain. The full unabridged text, keyed to Strong's numbers, in
`data/thayer.js`. It was decoded to Unicode from a community digitization (the
e-Sword "Thayer's Unabridged" module): the definitions are stored as RTF with
Greek in the Windows Greek code page (1253), Hebrew in 1255, and polytonic
accents as Unicode escapes, all of which a decoder (`tools/thayer_parse.py`,
driven by `tools/build_thayer.py`) converts to clean polytonic Unicode.
Scripture references are normalized and the color/formatting codes dropped;
definition text is otherwise as published.

**A Manual Greek Lexicon of the New Testament**, G. Abbott-Smith (1922) —
public domain. Assembled into `data/abbott.js`.

**Modifications:** entries were reformatted into JSON and restricted to the
vocabulary appearing in this New Testament. Definition text is otherwise as
published. One missing entry (G2057, Ἑρμᾶς) was added by hand from Strong's.

## Promise verses — King James Version

The 1,005 promise verses in `data/promises.js` are quoted from the **King James
Version (1769)**.

Every verse was copied from a machine-readable KJV rather than written from
memory, and is checked against it (`tools/kjv.py --verify`). Some entries quote a
contiguous clause rather than a whole verse; none paraphrase or splice.

**A note on KJV rights:** the KJV is public domain in the United States and most
of the world. In the United Kingdom it remains under perpetual Crown copyright,
administered by Cambridge University Press. Devotional and scholarly quotation is
long-established practice, but if this project is ever distributed commercially
in the UK it is worth confirming the position.

## The translation itself

The **Mak Translation** — the English rendering, its arrangement, the section
headings, and the promise meditations — is original work by the project owner,
produced with **Claude (Anthropic)** and released under CC BY-SA 4.0.

**Modifications, stated plainly for CC BY:** the English is a thought-for-thought
rendering arranged in English word order rather than Greek word order. Each
English phrase is anchored to the specific Greek word it renders. The Greek
underneath is unchanged.

## Fonts

Space Grotesk, JetBrains Mono and Gentium Plus, served by Google Fonts under the
SIL Open Font License. They are linked, not redistributed here.

---

## Verifying any of this

The claims above are meant to be checked, not trusted:

```
python tools/wordcounts.py     # Greek word counts vs SBLGNT, per book
python tools/kjv.py --verify   # every promise verse against the KJV
python tools/swap_scan.py      # detects English labels on the wrong Greek word
python tools/prose_scan.py     # mechanical prose defects
```

`CHANGELOG.md` records every correction made, including the mistakes found in
this project's own earlier work.
