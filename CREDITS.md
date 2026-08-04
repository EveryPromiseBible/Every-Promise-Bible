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

The 2,046 promise verses in `data/promises.js` are quoted from the **King James
Version (1769)**.

Every verse was copied from a machine-readable KJV rather than written from
memory, and is checked against it (`tools/kjv.py --verify`). Some entries quote a
contiguous clause rather than a whole verse; none paraphrase or splice.

**A note on KJV rights:** the KJV is public domain in the United States and most
of the world. In the United Kingdom it remains under perpetual Crown copyright,
administered by Cambridge University Press. Devotional and scholarly quotation is
long-established practice, but if this project is ever distributed commercially
in the UK it is worth confirming the position.

## Hymns — The Christian Hymn Book, 1870

The 1,323 hymns in `data/hymns.js` are transcribed from:

**The Christian Hymn Book: A Compilation of Psalms, Hymns and Spiritual Songs,
Original and Selected: Revised and Enlarged.** Compiled by Alexander Campbell and
others; revised by Isaac Errett, W. K. Pendleton, W. T. Moore, T. M. Allen and
A. S. Hayden. Cincinnati: H. S. Bosworth, 1870.
Project Gutenberg ebook 46041 — <https://www.gutenberg.org/ebooks/46041>

Published 1870, so the text is **public domain in the United States**: copyright
has expired on anything first published before 1931. Project Gutenberg's licence
covers its transcription and is not claimed over the underlying text.

**Modifications: none to the words.** `tools/hymns_build.py` extracts the hymns
mechanically and changes no line. What it does do is presentational, and worth
stating:

- **The title shown is the hymn's FIRST LINE.** The hymnal heads each hymn with a
  scripture theme instead of a name — the hymn everyone calls "Rock of Ages" is
  headed *"And that rock was Christ."* First lines are how hymnals have always
  been indexed and how a reader looks a hymn up. The scripture theme and its
  reference are kept and shown beneath the title.
- **Inline verse numbers are dropped**, because the app numbers the verses
  itself. Left in, the source's `2` would read as the first word of the line.
- Trailing full stops are trimmed from author names and metre labels.

364 of the 1,323 carry no author in the source; those are shown without one
rather than guessed at.

**Hymns still in copyright are not here and cannot be**, since the source predates
them. *How Great Thou Art* (Hine's English text, 1949), *He Lives* (1933) and
*Victory in Jesus* (1939) are commonly assumed to be old enough and are not.

## The translations and original writing

Three of the four texts in this app are original work by the project owner,
produced with **Claude (Anthropic)** — most recently **Claude Opus 5** — and
released under CC BY-SA 4.0. The work spans many sessions and successive model
versions; Opus 5 is the current one, not the only one that touched it.

### The Mak Translation — `data/chapters.js`

A **word-for-word** English New Testament: every English word is anchored to the
specific Greek word it renders.

**Modifications, stated plainly for CC BY:** the English is arranged in English
word order rather than Greek word order, which is what makes it readable; the
Greek order remains recoverable from the tags. Words supplied for the sake of
English, carrying no Greek, are marked as such in the rendering rather than left
to look like translation. **The Greek underneath is unchanged** — no word added,
removed, or moved between chapters, and `tools/wordcounts.py` proves it book by
book.

### The Illumination Translation — `data/illumination.js`

A loose, thought-for-thought paraphrase of the whole Bible — 66 books, 1,189
chapters, 9,031 verse blocks — composed in original modern English **from the
public-domain 1769 Authorized Version**, not from the Greek and Hebrew.

**What that means for its text, stated plainly:** it follows the textual
tradition the King James translators worked from, where the Mak interlinear
follows the SBLGNT, a modern critical edition. The two differ in a handful of
well-known places. This is a difference of underlying manuscripts and is
disclosed in the app itself, on the Options → The Texts page.

**Modifications:** the wording is original throughout — a paraphrase, not an
edit of the AV. Structurally it adds what the source has none of: a title for
every chapter, headings dividing 5,282 sections by subject, verses grouped into
blocks of a single thought rather than numbered singly, and a synopsis for each
of the 66 books.

### The Thirteenth Disciple — `data/devotional.js`

A devotional narrative, not a translation: *A Gospel Narrative in Thirty-One
Days*, walking beside Jesus from the Jordan to the Ascension. Roughly 32,000
words of original prose.

Each of the 31 days records the **harmony** of gospel passages it retells, so a
reader can go to the accounts themselves rather than taking the narrative's word
for anything. Scripture quoted inside the narrative is drawn from the
public-domain sources credited above.

It is a retelling and is presented as one. It is not scripture and does not
stand in for it.

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
