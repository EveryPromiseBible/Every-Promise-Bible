# PROJECT.md — Every Promise

> Complete developer handoff. Written for an AI agent with no access to prior conversations.
> **App:** `index.html` — ~230 KB, no framework, no build step, no dependencies.
> **Data:** `data/*.js` — ~27 MB across twelve files, loaded by `<script src>`.
> Serve the directory and open it; do not double-click `index.html`, because the
> data loads from a subdirectory and some browsers block that on `file://`.

> **Last full doc refresh: 2026-08-04.** Sections below marked with a date were
> rewritten then. If you find a claim that contradicts the code, trust the code
> and fix the line — a handoff document that lies is worse than none.

---

# Project Overview

## What this project is

**Every Promise** is a single-file web application containing a **Greek–English interlinear New Testament**. It is not a conventional Bible app. Its defining feature is that **every English word is anchored to a specific Greek word from the SBLGNT** (SBL Greek New Testament), and clicking any word opens its Strong's/Thayer's and Abbott–Smith lexicon entries.

The English is original work called the **"Mak Translation"** (`tx.01` in the UI). It is described as **word-for-word**: every English word sits on the specific Greek word it came from. It is grace-centered and reads as modern prose rather than a wooden gloss, but the anchoring is the point — no English word floats free of its Greek.

> The app said "thought-for-thought" until 2026-08-04, when Chris changed it to word-for-word in both places a reader meets the claim. "Word-for-word" here means the ANCHORING, not Greek syntax: the English is still arranged in English order. Do not let the phrase tempt you into re-ordering anything toward Greek.

**It is no longer only an interlinear.** Three more texts ship alongside it — see *The four texts* below.

The rendering makes this visible. Each word appears as a vertical three-line stack:

```
     Paul            ← English, bold, colored
    Παῦλος           ← Greek, same color, Gentium Plus serif
  G3972 N-NOM        ← Strong's + morphology, small gray mono
```

Supplied English words with no Greek behind them (added for flow) render in **black italic** with the Greek and tag lines blanked — so the reader can always see what came from the Greek and what didn't.

## The overall purpose and vision

The owner (Chris) is building a Bible that is **simultaneously devotional and rigorous**. The two goals are in permanent tension and both are required:

1. **Easy to read and makes sense.** This is the stated standard, given verbatim. Not "faithful to Greek syntax." Not "matches my style." *Can a reader follow this without stopping?*
2. **Every gloss honestly describes the Greek word beneath it.** The entire promise of the product is: *click this Greek word, learn what **this word** means.* A beautiful sentence with a drifted gloss is a **broken product**, not a stylistic quibble.

Around the interlinear sits a devotional layer: a promises/meditations engine, and planned Prayer and Journal spaces.

**Theological frame:** grace-centered, in the tradition of Joseph Prince. Promise meditations were hand-tagged with a "grace lens" — no self-effort language.

---

# Current Status

## What has already been completed

### Corpus

| | |
|---|---|
| Chapters | **260** |
| Word units | **117,353** |
| Greek tokens | **137,554** |
| Strong's/Thayer's entries | **5,367** |
| Abbott–Smith entries | **5,340** |
| Promise verses | **2,022** (15 meditations each, 17 moods) |

All 27 books, in canonical order. **The corpus is complete** and has been since
2026-07-31.

### The four texts *(rewritten 2026-08-04)*

| | UI code | What it is | Scope |
|---|---|---|---|
| **Mak Translation** | `tx.01` | The word-for-word interlinear. Every English word anchored to its Greek. | NT — 260 chapters, 1,190 sections, 117,353 units |
| **Illumination** | `tx.02` | Free prose paraphrase of the whole Bible, composed from the 1769 AV. Organised by subject. | 66 books, 1,189 chapters, 5,282 sections, 9,031 verse blocks, 66 synopses |
| **King James** | `tx.03` | The Authorized Version, 1769, unedited. | 66 books, 1,189 chapters |
| **The Thirteenth Disciple** | `dv.01` | A devotional narrative, not a translation. 31 days, Jordan to Ascension, ~32,000 words. Each day names the gospel harmony it retells. | 31 days |

**The Illumination follows a different Greek text than Mak does.** It descends
from the 1769 AV and so follows the tradition behind it; Mak follows SBLGNT. They
differ in a handful of well-known places. This is disclosed to readers in
Options → The Texts and in CREDITS.md. It is not a defect and must not be
"fixed."

**Only Mak has word-level Greek anchoring.** Every check in `tools/` that
protects the Greek applies to Mak alone. The Illumination has no alignment data
to check, and inventing some would be worse than having none.

### Greek accuracy — verified against SBLGNT

Every chapter checked word-by-word against **MorphGNT/SBLGNT**
(`github.com/morphgnt/sblgnt`). `tools/wordcounts.py` regenerates the proof table
shown above Matthew 1.

**All 27 books match: 137,554 Greek tokens here, 137,554 in SBLGNT.** No word
added, removed, or moved between chapters. The four long-standing Romans
discrepancies were closed on 2026-07-30 — see CHANGELOG.

### Readability — all books read as English

Every book has had a full prose pass and a full placement audit: 260 chapters,
1,190 sections, every unit read as a Greek/English pair. The "wooden" bands that
earlier versions of this document listed for Luke, John and Acts are gone.

That does **not** mean the prose is finished. One full pass has been made, and a
second reading would find more — see *Honest limitations* in README.md.

## What is currently being worked on *(2026-08-04)*

**No translation work is outstanding.** Recent sessions have been product work:
the Android wrapper, backup and restore, the hymnal, the options pages.

## Everything once listed here as unbuilt is now built

For a future session that finds an older copy of this file — these were all
listed as placeholders or inert:

| Was | Now |
|---|---|
| Prayer view — placeholder | Replaced by **Hymns**: 1,323 public-domain hymns, searchable |
| Journal view — placeholder | Calendar, six reading plans, daily reflection, sermon notes with formatting |
| My Stuff view — placeholder | Highlights, notes, bookmarks, journal, favourites, meditations — a page each, plus backup and restore |
| Favorites + History tabs — no logic | Working, and moved into My Stuff |
| Search — inert | Working, indexes every translation |
| Mood filtering — data unused | Working, 17 moods |
| Rest of the NT — 20 books missing | Complete, all 27 |

## What still needs to be built

1. **Listen / TTS** — button rendered, still inert
2. **Share** — button rendered, still inert
3. **Home button** — rendered, still inert
4. **Cross-references** — built, disabled behind `SHOW_CROSSREF = false`. The full
   corpus now exists, so the original blocker is gone; it needs retuning against
   full-corpus word frequency and testing.
5. **Play listing screenshots** — still show the retired Flutter app.

---

# Architecture

## Top-level shape

No bundler, no framework, no npm, no server. **Vanilla HTML + CSS + ES6.** Serve
the directory and it works. Any build step would be a regression.

**It is no longer one file.** The app was a single ~7.5 MB HTML document; the
data now lives in `data/*.js`, each loaded by an ordinary `<script src>` before
the application code. This is what makes 27 MB of corpus survivable: the browser
caches each file separately, and the service worker can revalidate the small,
often-changed `index.html` while serving the huge, rarely-changed data from cache.

```
index.html                (~230 KB — the entire app)
├── <head>
│   ├── fonts + manifest + theme-color
│   └── <style>                        one block, ~700 lines
├── <body>
│   ├── <header>          brand · bible toolbar · nav-stack (tabs + options mark)
│   ├── <main>            #view-promises, #view-meditate      ← ONLY these two
│   ├── #view-bible       outside <main>, full-width layout
│   ├── #view-mystuff     index + a page per category
│   ├── #view-hymns       index + reader          (was #view-prayer)
│   ├── #view-options     index + a page per topic
│   ├── #view-journal     calendar + panel, and the sermon-notes page
│   ├── .bnav             mobile bottom nav — five tabs, ends on Journal
│   ├── #defOverlay       lexicon modal
│   └── #noteOverlay      note modal
└── <script src="data/*.js"> ×12, then the application code

data/   chapters.js 5.4 MB · illumination.js 4.8 MB · kjv.js 4.4 MB
        thayer.js 5.0 MB · abbott.js 2.5 MB · promises.js 1.5 MB
        wordpictures.js 1.4 MB · lexicon.js 1.2 MB · hymns.js 1.1 MB
        commentary.js 6.7 MB · devotional.js 230 KB · wordcounts.js 1 KB
```

> ⚠️ **Each data file's payload is exactly ONE LINE.** `const CHAPTERS = [...]`
> and its siblings are single lines, and the Python tools rewrite them by
> replacing that line wholesale:
> ```python
> lines[i] = 'const CHAPTERS = ' + json.dumps(ch, ensure_ascii=False) + ';'
> ```
> **Never pretty-print them.** A formatter would explode each file to millions of
> lines and break every tool that touches it.

> ⚠️ **`<main>` holds only promises and meditate.** Every other view sits outside
> it for full-width layout — and an empty `<main>` still carries its padding, so
> `sv()` hides it when the active view is not inside it. Removing that puts a
> 130 px band of nothing above five of the seven views.

## Data schemas

### `CHAPTERS` — array of 260   *(the Mak Translation)*

```js
{
  ref: "Matthew 1",              // "{Book} {chapter}" — the ONLY chapter identifier
  sections: [
    {
      heading: "The Genealogy",  // editorial section title, NOT from Greek
      words: [ [english, greek, tags], ... ],
      notes: []                  // present on every section, EMPTY everywhere. Unused.
    }
  ]
}
```

**There are no verse numbers anywhere in the data.** Sections are the only subdivision. This is a real constraint — it's why the 4 remaining Romans errors can't be pinned mechanically.

### The word unit — `[english, greek, tags]`

The core data structure. A 3-element array.

| Field | Meaning |
|---|---|
| `english` | Display English. May be multiple words ("of the Presentation"). May be `""`. |
| `greek` | Greek token(s), space-separated. May hold several ("τῶν προφητῶν"). May be `""`. |
| `tags` | ` · `-separated (space, U+00B7, space). One tag per Greek token. Format `G{num} {morph}`. |

Four valid states:

| `english` | `greek` | Renders as | Meaning |
|---|---|---|---|
| set | set | colored 3-line stack, clickable | normal word |
| set | `""` | **black italic**, Greek/tag lines hidden | **supplied filler** — English added for flow |
| `""` | set | Greek+tag visible, English blank | **folded particle** — untranslatable δέ/γάρ etc. |
| `""` | `""` | nothing | shouldn't exist |

**Multi-token folding.** A unit may carry several Greek words with matching tags:

```js
["God's", "τοῦ θεοῦ", "G3588 ART · G2316 N-GEN"]
```
Clicking shows **both** lexicon entries stacked, separated by `.def-divider`.

### `LEXICON` — object keyed by `"G26"`

```js
{ greek, translit, pronunciation, derivation, definition, kjv }
```

### `ABBOTT` — object keyed by `"G26"`

```js
{
  lemma, occurrencesNT, form, etymology,
  senses: [ { num, text, subsenses: [ { num, text, subsenses: [...] } ] } ],  // RECURSIVE
  synonyms
}
```
Senses render as a collapsible accordion; `renderSubsenses()` recurses.

### `PROMISES` — array of 2,022

```js
{
  reference: "Psalm 46:1",
  verse: "God is our refuge and strength...",
  meditations: [ "God is your refuge.", ... ],   // EXACTLY 15, always
  moods: ["Anxious", "Broken", ...]
}
```

**17 moods, hand-tagged.** Mood filtering is live — the data is used, not
waiting. Favourites and custom meditations key on `reference`, never on index:
PROMISES has grown 329 → 1,005 → 1,522 → 2,022, and anything index-keyed
silently re-points to a different verse on every rebuild.

### `ILLUMINATION` — array of 1,189   *(added 2026-08-04)*

Three consts in `data/illumination.js`, all one line each:

```js
const ILLUMINATION_BOOKS  = [ { name:"Genesis", order:1, testament:"OT", chapters:50 }, ... ]  // 66
const ILLUMINATION_INTROS = { "Genesis": <synopsis>, ... }                                     // 66
const ILLUMINATION = [
  {
    ref: "Galatians 5",                  // "{Book} {chapter}"
    title: "Freedom, the Spirit, and the Fruit",
    sections: [
      {
        heading: "Keep in Step",
        verses: [ ["5:25–26", "Since we live in the Spirit, ..."] ]   // [ref, text]
      }
    ]
  }
]
```

**A verse block is a THOUGHT, not a verse.** `"5:25–26"` is one entry holding
both verses, because the paraphrase renders them as a single sentence. Never
assume one block equals one verse.

The KJV in `data/kjv.js` uses the **same shape** (`KJV_BOOKS`, `KJV`), which is
why both are driven by one reader through the `CORPUS` registry. `KJV` has no
intros; `title` and `heading` are empty strings there.

### `DEVOTIONAL` — object   *(added 2026-08-04)*

```js
{
  title: "The Thirteenth Disciple",
  subtitle: "A Gospel Narrative in Thirty-One Days",
  front: [ {k, t}, ... ],          // front matter, destination 0
  days: [
    {
      n: 1,
      title: "Come and See",
      harmony: "John 1:19-51",     // the gospel passages this day retells
      opening: [ ... ],            // the short italic block
      body: [ {k, t}, ... ]        // k: p prose · q quote · attr · h heading
    }
  ]
}
```

Destination 0 is the front matter, not a reading — `openSomewhereRandom()` draws
from `1 + random(days.length)` for exactly that reason.

### `HYMNS` — object   *(added 2026-08-03)*

```js
{
  source: "The Christian Hymn Book, Cincinnati 1870 (Project Gutenberg 46041). Public domain.",
  hymns: [
    {
      n: 261,                       // the hymnal's own number
      title: "Rock of ages, cleft for me",   // THE FIRST LINE, not a name
      author: "Toplady",
      meter: "7s, 6 lines",
      theme: "And that rock was Christ",     // the scripture heading
      ref: "1 Cor. 10:4",
      verses: [ ["line", "line", ...], ... ]
    }
  ]
}
```

**`title` is the first line.** The hymnal heads each hymn with a scripture theme
rather than a name — the one everyone calls "Rock of Ages" is headed *"And that
rock was Christ."* First lines are how hymnals index and how a reader looks one
up. Regenerate with `tools/hymns_build.py`; do not hand-edit.

### Reader settings — `everypromise_settings`

`{ size, font }` — the reading scale and face. Written by `optSet()`, applied by
`applySettings()` **before first render**, and carried in the backup file.

## JavaScript

No framework. Global functions, `onclick=` attributes in markup, direct DOM manipulation. **Match this style.** Do not introduce React/Vue/jQuery.

### View router

```js
function sv(name)   // "set view" — the router. Toggles .active on .view elements.
```
Views: `promises`, `meditate`, `bible`, `mystuff`, `prayer`, `journal`. Also syncs `[data-v]` nav buttons and shows/hides the bible toolbar.

### Rendering pipeline

```
loadChapter(idx)
  └── buildSection(section, chapterIdx, sectionIdx)   ← per section
        └── per word: build .unit > .eng + .grk + .tag
```

**Color assignment (`buildSection`):**
```js
let colorIdx = 0;
section.words.forEach(triple => {
  if (grk === "") { /* filler — no color, no colorIdx increment */ }
  else { const color = PALETTE[colorIdx % PALETTE.length]; colorIdx++; }
});
```
- `colorIdx` **resets to 0 at each section**
- Filler units **do not consume a color**
- Cycles through 36 colors

**Word keys:** `` `${chapterIdx}:${sectionIdx}:${wordIdx}` `` — used for highlights.
**Section keys:** `` `${chapterIdx}:${sectionIdx}` `` — used for bookmarks/notes.

> ⚠️ **Both keys are positional.** Inserting or deleting a unit silently re-points every saved highlight after it. Reordering *within* a section shifts them too. This is real technical debt.

### `OCCURRENCE_INDEX`

Built at load. Maps `"G26"` → every place that Strong's number occurs corpus-wide. Powers cross-references. `CROSSREF_MAX = 12` — above that a word is "too common (grammatical) to usefully list."

`SHOW_CROSSREF = false`. The comment says: *"re-enable once the full NT is translated and this can be retuned against full-corpus word frequency."*

### Persistence

`localStorage`, keys prefixed `everypromise_`:

| Key | Shape |
|---|---|
| `everypromise_bookmarks` | `{key, chapterIdx, sectionIdx, ref, heading}` |
| `everypromise_notes` | `{key, chapterIdx, sectionIdx, ref, heading, text}` |
| `everypromise_highlights` | `{key, chapterIdx, sectionIdx, ref, heading, eng, grk}` |

`loadStore()` / `saveStore()` both try/catch and fail silently. **Favorites and History have UI tabs but no storage code.**

### Modes

| Mode | Mechanism |
|---|---|
| **Read mode** | `body.read-mode` — CSS hides `.grk`/`.tag`, disables clicks, hides section actions |
| **Highlight mode** | `body.highlight-mode` — cursor `cell`; clicks toggle highlight instead of opening lexicon |

Both are **CSS-driven off body classes**. No re-render. Keep it that way.

## CSS

Single `<style>` block. **CSS custom properties on `:root`.** BEM-ish flat class names, no preprocessor, no utility framework.

Only one media query: `@media(max-width:1000px)` — hides top nav, shows `.bnav` bottom bar, stacks the bible layout, hides the wordmark.

## Important design decisions (and why)

| Decision | Rationale |
|---|---|
| **Single file, no build** | Portability. Emailable, archivable, runs from `file://` forever. |
| **Data inlined, not fetched** | No CORS, no server, works offline from disk. |
| **Units in ENGLISH order, not Greek order** | The English must read naturally. Greek order is recoverable via tags. **See below.** |
| **Greek multiset is the invariant, not sequence** | Since units are English-ordered, sequence *must* differ from SBLGNT. What must never change is that every Greek word appears exactly once. |
| **Sections, not verses** | Editorial/devotional feel. Costs precision (can't pin errors to a verse). |
| **Vanilla JS** | No toolchain to rot. |
| **Color cycling per section** | Visual anchor between English and Greek without needing a line. |
| **Two lexicons stacked** | Strong's = quick; Abbott–Smith = scholarly depth. |

> **The English-order decision is the single most important architectural fact.** Units are stored in the order the *English* reads. So `Counter(greek_tokens)` must match SBLGNT exactly, but `list(greek_tokens)` will not. Any check asserting sequence equality is wrong.

---

# Features

## Currently working *(rewritten 2026-08-04)*

### Promises (landing view)
- Verse of the day — drawn from 2,022; **2 Corinthians 1:20 is the anchor**, shown on every load rather than a random pick
- **Shuffle** — new verse, from a shuffled deck rather than repeated random draws
- **Meditate** — opens the meditation stepper
- **Favourite** — heart toggle, **persisted**, keyed on the verse reference
- **Mood filter** — 17 moods, live

### Meditate
- 15 meditations per verse, one at a time, large type
- Prev/Next with disabled states at bounds
- Dot indicator — click to jump; blue dot = user-added
- **Add your own** — **persisted**, keyed on reference, removable

### Bible (the core)
- Four texts through one toolbar: Mak, Illumination, KJV, devotional
- Testament filter for the two whole-Bible texts; hidden for Mak, which is NT only
- Three-line word stacks, 36-colour cycling per section
- **Tap any word → lexicon modal** with Strong's + Abbott–Smith
- **Study/Read toggle** — Read hides Greek and tags for clean prose
- **Highlight mode** — works in Study *and* Read; whole-verse highlighting in the Illumination
- **Section bookmark and notes** — on Mak sections and on Illumination/KJV headings; visible in both modes
- Search across every translation at once
- Library side panel — **the library only**; auto-opens >1000px, closes on a pick at phone width

### My Stuff
- Index of counts, each opening its own page: highlights, notes, sermon notes, bookmarks, journal entries, favourites, meditations, chapters visited, moods
- Every item jumps to the **exact** word or verse and flashes it
- Remove from the page
- **Backup and restore** to a `.json` the reader keeps, with a "last backup" nudge
- Asks the browser for persistent storage

### Journal
- Month calendar; markers for reading due and days written on
- Six reading plans, computed from the corpus rather than hard-coded
- Daily reflection, and **sermon notes on their own page** with a formatting bar

### Hymns
- 1,323 hymns, indexed by first line, searchable across text, author, theme and metre
- Previous/next follow the search, not the hymnal

### Options
- Reading size and font (reading surfaces only), About, The Texts, Sources & Licences

### Responsive
- <1000px: bottom nav (five tabs, ends on Journal), stacked layout, options mark top-right in the header, library panel above the text and capped at 58vh


## Planned / stubbed *(rewritten 2026-08-04)*

| Feature | Status |
|---|---|
| Listen / TTS | Button rendered, **inert** |
| Share | Button rendered, **inert** |
| Home button | Button rendered, **inert** |
| Cross-references | Built, `SHOW_CROSSREF = false`. The full-NT blocker is gone; needs retuning against full-corpus frequency |
| Study Notes (`ref.02`) | Card exists; `section.notes` is present on every section and empty everywhere |
| Antique facsimiles | Cards exist, nothing behind them |
| Play listing screenshots | Still show the retired Flutter app |

Everything else this table used to list — mood filtering, Prayer, Journal, My
Stuff, Search, favourites, history, the missing 20 books — is **built**. See
*Everything once listed here as unbuilt is now built* above.

---

# Current Priorities *(rewritten 2026-08-04)*

**The translation work is done.** Every priority this section used to list —
audit Matthew and Mark, finish Luke, John, Acts 1–12, mood filtering, favourites
and history — is complete. The placement audit closed on 2026-07-31 across all
27 books, and the four Romans Greek discrepancies closed on 2026-07-30.

What is worth doing next, in rough order:

### 1. A second prose reading

One full pass has been made. README's *Honest limitations* says plainly that a
second reading would find more, and that is still true. This is the highest-value
work on the text itself — but it is polish now, not repair.

### 2. Retire the dead buttons

Listen, Share and Home are rendered and do nothing. Either build them or remove
them; a control that does nothing teaches a reader not to trust the others.

### 3. Cross-references

Built and switched off. The blocker was "wait for the full NT", and the full NT
is here.

### 4. Replace the Play listing screenshots

They show the Flutter app that no longer exists. A store-listing edit, no build.

### 5. Nothing about the Illumination's textual basis

Listed here so a future session does not "discover" it and try to fix it. The
Illumination descends from the 1769 AV and follows a different Greek text than
Mak. That is disclosed to readers and is **deliberate**.

---

# Known Issues

## 🔴 THE CRITICAL BUG — gloss drift

**This is the most important thing in this document.**

When you reorder units **and** rewrite glosses in the same operation, the English comes out reading perfectly while the label under the Greek drifts onto the wrong word.

Real case, Luke 2:1. Produced this — which reads flawlessly:

> "Now it happened in those days that a decree from Caesar Augustus went out that all the inhabited world should be registered."

But underneath:

| Greek | was labelled | should be |
|---|---|---|
| `ἐξῆλθεν` (went out) | **"that"** | "went out" |
| `ἀπογράφεσθαι` (to be registered) | **"went out that"** | "should be registered" |
| `οἰκουμένην` (inhabited world) | **"inhabited world should be registered"** | "inhabited world" |

**Click `ἐξῆλθεν` on the site → the popup says "that."** The product's entire promise is broken, silently.

### Why every existing check misses it

| Check | Why it fails |
|---|---|
| Prose read-back | The prose *reads fine* — that's the whole problem |
| Greek multiset vs SBLGNT | **Passes.** No Greek was lost or added. |
| `splice()` assertion | **Passes.** It only guards the Greek. |
| Token count (137,554) | **Passes.** |

**Only printing each Greek → English pair catches it.**

### The rule

> ## Reorder units, OR rewrite glosses — never both in one step. Then print every pair you touched and read them.

### ⚠️ Matthew and Mark were never checked this way

Pair-checking started partway through Luke. **Matthew (28 ch) and Mark (16 ch) were done reading prose only.** Assume drift is present until audited.

### What this looks like when it lands on something that matters

**Luke 3:23 — a missing generation.** The English read:

> "being a son— as it was supposed— of Joseph, **of Matthat**, of Levi..."

**Heli was gone.** `τοῦ Ἠλὶ` was sitting right there in the Greek — but labelled "of Joseph," with every gloss from `υἱός` onward shifted one place. Luke's genealogy runs *through Heli*; it's what distinguishes Luke's account from Matthew's. Prose: fine. Greek count: clean. Only pair-checking found it.

All 76 names were then verified. Heli was the only one dropped.

## 🟠 Remaining data errors

| Issue | Detail |
|---|---|
| **Romans — 4 Greek words** | ch3 `ὁ`→`ὄν`, ch8 `τὸν`→`τὸ`, ch13 `τὸν`→`τὸ`, ch15 `οὖν`→`οὐ`. Each word occurs 8–15× per chapter; no verse numbers exist to disambiguate. Needs verse-level alignment. |
| **Matthew 7:12 — last Greek leak** | English: *"for this and you also sums up the Law and the Prophets. Οὗτος γάρ"*. `οὕτως` ("so/thus") and `οὗτος` ("this") are **crossed** — near-identical words. Also an `ἐστιν` sits in the 7:12 region that SBLGNT places at **7:9**. Needs re-authoring by hand. |
| **5 lowercase sentence-starts** | 3 Mark, 2 Luke. Cosmetic. |
| **37 arity mismatches** | Greek token count ≠ tag count. **All pre-existing.** Mostly Matthew 1 genealogy where a folded `τὸν` has no matching tag. |

## 🟢 2026-08-12 — Hebrews text review, four items

Chris read through Hebrews and flagged four spots. Three were fixed and pushed;
the fourth was investigated and deliberately left alone. Full detail — the
Greek, the reasoning, the options offered — is in CHANGELOG.md under each
date-matching entry.

| Passage | What changed |
|---|---|
| **Hebrews 3:9**, Illumination + Commentary | "made Me sick at heart" → **"I grieved over that generation"** — matches the Illumination's own Psalm 95:8–11, which Hebrews 3:9 is quoting. προσώχθισα (G4360) is an anger/indignation word, not a sickness word. |
| **Hebrews 2:5–8**, Commentary only | Cut *"or claim it by faith"* — the line set faith up as a contrast to honesty, read as a swipe at faith language. The section's actual point (the writer says "not yet," not "look harder") is unchanged. |
| **Hebrews 2:1–4**, Illumination + Commentary | "So we owe" → **"So we must give"** — δεῖ (G1163-family, impersonal necessity) was rendered as if it were ὀφείλω (debt/owe), which isn't in this verse. Also updated the commentary's Greek gloss, which had never actually named δεῖ. |
| **Romans 7:5**, Mak — **left unchanged** | See the "Open translation decisions" table below. |

## 🟡 Open translation decisions — Chris's call, not the AI's

| Passage | Question |
|---|---|
| **Mark 1:41 — `ὀργισθεὶς`** | Currently "moved with indignation." SBLGNT prints the harder reading (angry) vs. `σπλαγχνισθεὶς` (compassion). **Long-standing open question. Never decided. Do not change it.** |
| **Romans 16:25–27 doxology** | Textual placement question. Unresolved. |
| **`—` placeholders** | 342 across Luke (77) + John (265). Romans already solved this by folding the article. **Chris chose chapter-by-chapter (Option B) over a bulk sweep — but the option stands.** |
| **Romans 7:5 — "stirred up by" over `τὰ διὰ`** | The Mak's unit `['stirred up by', 'τὰ διὰ', 'G3588 ART · G1223 PREP']` glosses an article + preposition ("the [ones] through") with a verb of arousal that isn't in the Greek — no word for "stir/arouse/incite" exists here in **any** Greek text tradition. Checked directly: Textus Receptus (Stephanus 1550), Byzantine Majority Text, and the critical text (NA27/UBS4) all print the identical `τὰ διὰ τοῦ νόμου ἐνηργεῖτο`, word for word — this is not a textual variant. The KJV, which the Illumination is built from, doesn't have it either: *"the motions of sins, which were by the law, did work in our members"* — plain and literal. "Aroused by" is the NASB's own interpretive addition (confirmed by direct lookup), not a translation of a Greek word; it likely borrows forward from Paul's explicit "sin, taking opportunity by the commandment, wrought in me" two verses later (7:8), where a real verb of that kind (`κατειργάσατο`) does exist and is correctly glossed there as "stirred up." **Chris's decision, 2026-08-12, after the investigation above: leave the Mak's wording exactly as it stands. Do not change it, and do not follow the NASB's move here either.** Recorded so a future pass doesn't rediscover this and "fix" it without knowing it was already decided. |

## 🟡 Technical debt *(rewritten 2026-08-04)*

| Item | Detail |
|---|---|
| **No verse numbers in Mak** | `CHAPTERS` has sections, not verses. Blocks precise error location and cross-refs to standard references. The Illumination and KJV *do* carry verse refs. |
| **`section.notes` unused** | Present on all 1,190 Mak sections, empty everywhere. |
| **Dead buttons** | Home, Listen, Share. Rendered, inert. |
| **Fake library cards** | Study Notes, Gutenberg, Luther have no backing. |
| **`innerHTML` everywhere** | Lists and modals are built by string concatenation. **This stopped being theoretical when restore landed:** a backup file is user-supplied input, so saved-item labels are escaped with `ilEsc()` and sermon-note markup goes through `rtSanitize()`. Anything new that renders stored text must do the same. |
| **`execCommand` in the sermon editor** | Deprecated, with no dependency-free replacement. Works everywhere that matters; degrades to plain typing if a command is refused. |
| **Full re-render on mutation** | `loadChapter()` / `loadIllum()` after a bookmark or note change. Fine at current size; the Illumination reader does targeted class toggles instead so the reader does not lose their place. |
| **Google Fonts dependency** | The only network call. Offline → fallback fonts. |
| **27 MB of data** | Split across twelve files and cached by the service worker. First visit pulls ~21 MB; Thayer's (5 MB) waits for the first word tap. |

### Resolved, kept here so nobody re-reports them

| Was | Now |
|---|---|
| Positional highlight keys | `stableKey(chapterIdx, sectionIdx, grk, nth)` — content-addressed. Migrated on load. |
| Positional bookmark/note keys | `translation\|reference\|section`. Migrated on load. |
| `moods` populated but unused | Live, 17 moods. |
| In-memory favourites | Persisted, keyed on the verse reference. |
| Single 7.5 MB file | Split into `index.html` + `data/*.js`. |


## Recurring wooden patterns (measured across the corpus)

| Pattern | Matthew | Mark | **Luke** | **John** |
|---|---|---|---|---|
| Postposed genitive ("of his", "of mine") | 16 | 10 | **214** | **284** |
| `—` placeholder for the article | 0 | 0 | **77** | **265** |
| Doubled article ("the calf the fattened one") | 4 | 1 | **44** | **65** |
| Postposed δέ as "now" | 0 | 0 | **31** | **18** |
| "a X certain" | 0 | 0 | **12** | 0 |

Matthew/Mark are near zero **because they were fixed**. Luke/John are untouched.

---

# Design Guidelines

> **This section describes an existing, deliberate design. Do not redesign. Do not "modernize." Do not add a dark mode, gradients, shadows, or animation. Change nothing here unless Chris asks.**

> Night mode was built on 2026-08-04 and REMOVED the same day: Chris looked at
> it and did not want it. Do not re-add it speculatively.

## Colors

```css
--white:  #ffffff    /* page background */
--paper:  #fbfaf8    /* side panel, accordion bodies, dividers */
--ink:    #111111    /* primary text, primary buttons, borders on emphasis */
--gray:   #9a9a95    /* secondary text, labels, inactive nav */
--line:   #eceae3    /* all borders and rules */

--orange: #FF5A1F    /* THE accent. Active states, highlights, Strong's dot */
--blue:   #3B6FE0    /* Abbott-Smith dot, sense numbers, custom meditation dots */
--yellow: #F0B90B    /* library swatch */
--green:  #3FA66A    /* library swatch */
--pink:   #E8558C    /* library swatch, destructive hover */
```

Other literals in use: `#fdf0b8` highlight fill · `#fbe79a` highlight hover · `#f4f3ef` unit hover · `#6b5f4a` section headings · `#9c9488` tag text · `#2b2b2b` filler italic · `#fff8f4` active library card.

**Orange is the accent. Not blue. Not purple.** It marks the active tool, the active tab, the active dot, the switch when on.

### The 36-color palette

`PALETTE` at line 377. Muted, desaturated, mid-dark — legible on white at 0.85em. Cycles per section, resets each section, skips fillers.

```js
"#b5461a","#1a6fa8","#7a8c1a","#a3247a","#1a8c6f","#c47a00","#5a3fa8",
"#0f7a3f","#a81a3f","#2f6ba8","#8c5a1a","#1a9c9c","#8c1a8c","#4f7a1a",
"#c4321a","#1a4fa8","#a87a1a","#2f8c5a","#7a1a5a","#1a7ac4","#a84f1a",
"#5a7a1a","#c41a6f","#1a8caf","#8c3f1a","#3f1a8c","#a89c1a","#1a5a7a",
"#7a4f1a","#c41a3f","#1a7a4f","#6f1a8c","#af7a1a","#1a3fa8","#8c1a3f",
"#4f8c1a"
```

**Never reorder, resaturate, or shorten this array.** Adjacent colors are deliberately distinct.

## Fonts

```css
--sans: 'Space Grotesk', sans-serif     /* UI + English */
--mono: 'JetBrains Mono', monospace     /* refs, tags, labels, metadata */
--grk:  'Gentium Plus', serif           /* Greek + user-written text */
```

**Gentium Plus is used for Greek AND for user input** (note textarea, meditation input) — user writing gets the same serif dignity as the Greek. Deliberate.

Weights: Space Grotesk 400/500/600/700 · JetBrains Mono 500/700 · Gentium Plus regular + italic.

## Style

- **Lowercase UI.** Buttons, labels, headings: `text-transform:lowercase`. "meditate", "share", "my stuff". Chapter refs lowercase too.
- **Mono for metadata.** Anything data-ish — refs, Strong's numbers, counters, tab labels — is JetBrains Mono, small, gray, often lowercase.
- **Pill buttons.** `border-radius:999px` for actions. `8px` for tools. `50%` for icons.
- **Hairline borders.** 1px or 1.5px `--line`. Never heavy.
- **Almost no shadow.** Only the modal (`0 20px 60px rgba(0,0,0,0.25)`) and the switch knob.
- **Big display type.** Verse of the day 2.6em/700. Meditation 2.3em/700. Negative letter-spacing (-0.01em).
- **Generous whitespace.** Sections 2.6em apart. Modals padded 26px.
- **Italic section headings** in muted brown `#6b5f4a` — editorial, not scriptural.

## UI philosophy

1. **The text is the interface.** Chrome recedes. No sidebars of buttons.
2. **Study and Read are equals.** Not a hidden toggle — a labeled switch.
3. **Nothing between reader and word.** One tap = definition. No hover cards, no popovers, no tooltips.
4. **The Greek is always honest.** Filler is italic black. Folded particles show Greek with blank English. The reader always knows what came from Greek.
5. **Devotional, not academic.** Lowercase, warm, spacious. Not a seminary tool.
6. **Local-first.** No accounts, no sync, no telemetry. localStorage only.

## Never change unless Chris asks

- The **36-color palette** — contents or order
- **Orange `#FF5A1F`** as the accent
- The three fonts
- **Lowercase UI convention**
- The **three-line word stack** (English / Greek / tag)
- **Black italic for supplied filler**
- **Single-file, no-build** architecture
- **Section headings** as the subdivision (vs. verse numbers)
- **"Mak Translation"** and the `tx.01` / `ref.01` / `an.01` code scheme
- The **Study/Read** switch
- **Mark 1:41** rendering
- The **grace-centered** theological frame

---

# Coding Standards

## Naming

| Thing | Convention | Example |
|---|---|---|
| JS functions | `camelCase`, verb-first | `loadChapter`, `toggleHighlight`, `renderNotesTab` |
| The router | `sv(name)` | terse "set view" — established |
| JS constants | `SCREAMING_SNAKE` | `PALETTE`, `CHAPTERS`, `OCCURRENCE_INDEX`, `SHOW_CROSSREF` |
| Mutable globals | `camelCase`, `let` at top of section | `currentIdx`, `readMode`, `currentChapterIdx` |
| CSS classes | lowercase, hyphenated | `.word-row`, `.def-source-block`, `.as-sense-head` |
| CSS abbrevs | established prefixes | `.def-*` lexicon · `.as-*` Abbott-Smith · `.med-*` meditate · `.si-*` saved item · `.lib-*` library |
| DOM ids | `camelCase` | `chapterSelect`, `defOverlay`, `noteTextarea` |
| View ids | `view-{name}` | `view-bible` — **`sv()` depends on this** |
| Tab ids | `tab-{name}` | `tab-bookmarks` — **`showTab()` depends on this** |
| localStorage | `everypromise_{name}` | `everypromise_bookmarks` |

## Formatting

- **2-space indent**
- CSS is **dense** — related props on one line. Match it.
- Semicolons in JS.
- Single quotes in JS; double in HTML attributes.
- Template literals for HTML strings.
- Comment blocks: `/* ---- Bookmarks ---- */`

## Implementation rules

1. **NEVER pretty-print the data blobs.** Lines 378–381 (0-indexed 377–380) stay one line each. Rewrite via:
   ```python
   lines[377] = 'const CHAPTERS = ' + json.dumps(ch, ensure_ascii=False) + ';'
   ```
2. **`ensure_ascii=False`** always. The file is UTF-8 Greek.
3. **No build step. No dependencies. No framework.**
4. **`onclick=` in markup is the established pattern** for static elements; `addEventListener` for generated ones (see `buildSection`). Both are correct in their place.
5. **Modes are body classes.** Don't re-render for a mode change.
6. **Follow the bookmarks pattern** for any new persistence: `loadStore` → mutate → `saveStore` → re-render.
7. **Never edit by content search.** `[k for k,w in enumerate(ws) if w[1]=='καὶ'][0]` hits the **wrong instance** — `καὶ` appears dozens of times per section. This broke Matthew 8 and Luke 2. **Use explicit indices.**
8. **Author the whole plan; assert every unit consumed exactly once.** Index shift after `pop()` broke Matthew 8 and Romans 2.
9. **Folds first, capitalization LAST.** Running capitalization first capitalized leaked Greek ("Νηστεύοντες"); removing those units then exposed lowercase sentences underneath.
10. **Never `sed` a plan file.** It produced a plan mapping `γάρ` ("For") onto "happened?".
11. **Verify after every session:** 137,554 Greek tokens · 117,353 units · 0 SBLGNT discrepancies · all 12 files in `data/` parse.

## The `splice` helper

The workhorse. Reorders units within a span while proving no Greek moved.

```python
from collections import Counter

def splice(ws, a, b, plan):
    """Replace ws[a:b] with units reordered per plan=[(old_abs_index, new_en|None), ...]
       new_en=None keeps existing English."""
    seg = [list(w) for w in ws[a:b]]
    assert sorted(i for i, _ in plan) == list(range(a, b)), \
        f'plan must cover exactly [{a},{b})'
    new = []
    for i, en in plan:
        u = list(ws[i])
        if en is not None: u[0] = en
        new.append(u)
    assert Counter(t for w in seg for t in w[1].split()) == \
           Counter(t for w in new for t in w[1].split()), 'splice changed Greek'
    ws[a:b] = new
```

Its assertions **blocked real bad writes** — span errors, and the `sed`/`γάρ` case. **They cannot catch gloss drift.**

## Per-section workflow

1. Dump units as `{index}|{english}|{greek}`
2. Read the prose; find Greek-order sentences
3. Author a `splice` plan with **explicit indices**
4. Run — assertions guard the Greek
5. **Print Greek→English pairs for every unit touched**
6. Read the prose back
7. Verify token count + SBLGNT; save

## Verification snippets

```python
# --- SBLGNT check. Needs github.com/morphgnt/sblgnt (codeload tarball works).
# CRITICAL: authoritative surface form is column index 4. Index 5 is NORMALIZED
# (elision resolved: δι'→διά, οὐκ→οὐ) and will produce ~2000 false positives.
p = line.split()
book_chapter = int(p[0][2:4]); surface = p[4]

# --- Greek leaking onto the English line
GREEK = re.compile(r'[\u0370-\u03ff\u1f00-\u1fff]')
[(c['ref'], e) for c in ch for s in c['sections'] for e,g,t in s['words'] if GREEK.search(e)]

# --- lowercase sentence-starts
prev[0].strip().endswith(('.','?','!')) and cur[0].strip()[:1].islower()

# --- arity check (Greek tokens vs tags)
len(g.split()) != len([x for x in t.split('·') if x.strip()])
```

Book file map: `61-Mt 62-Mk 63-Lk 64-Jn 65-Ac 66-Ro 67-1Co`.

---

# Things the next AI should know

## 1. The standard is Chris's words, not your taste

> **"I want it to be easy to read and make sense."**

That is the test. Not "faithful to Greek syntax." Not "matches the register of Romans 1." When these conflict, **readability wins** — *provided the gloss stays honest.*

This was learned the hard way. An earlier attempt chased "the voice of Romans 1" and produced *"God's verdict lands on the truth of things"* — replacing the clearer *"God's judgment is based on truth."* Punchier, worse. Chris's correction reframed everything.

## 2. Gloss drift is the failure mode that matters — read the Known Issues section

If you read nothing else, read that. It produces perfect English with the wrong word in the popup, and **every automated check passes.**

## 3. Matthew and Mark are unaudited

44 chapters done before pair-checking. Drift may be sitting there. **This is the most valuable work available.**

## 4. Metrics lie. You must read.

Three separate proxies were tried and **all three were wrong**:

| Metric | Verdict | Reality |
|---|---|---|
| % multi-word English units | "Matthew 1–28 all fine" | Matthew 8 was unreadable |
| Filler-ratio (supplied English %) | "1 Corinthians 13 is wooden" | It's beautiful |
| Chapter-opening samples | "Matthew 9–28 wooden" | 9–22, 25–27 were fine |

Wooden text has multi-word units too ("the Son of Man"). Non-Romans books were built without the filler convention but still read fine. Openings aren't representative.

**There is no proxy for reading it.**

## 5. The insight that makes this tractable

The wooden chapters have **good English glosses sitting in Greek word order**.

`ἠκολούθησαν αὐτῷ ὄχλοι πολλοί` glossed in place gives *"there followed him crowds large."* Reorder those same four units → *"large crowds followed him."* **The Greek rides along for free.**

So most of the work is **reordering units**, not rewriting English. That's why `splice` exists.

## 6. Not every inversion is an error

- *"was healed the servant"* → **wrong.** Greek order leaked.
- *"there were sitting Pharisees"* → **correct.** English existential inversion.

Over-triggering on this broke a working section of Luke 5 that had to be restored from the original upload. **Read the sentence. Ask whether an English speaker would say it.**

## 7. Errors are rarely simple substitutions

The 11 Greek errors resisted pinning for a long time because they weren't typos-in-place. Each was a word **absent at one site and spurious at another**:

- Matthew 7:9 — `ὃν` and `ἢ` missing entirely; **7:28** had a duplicate `ὁ` and spurious `ἦν`
- Matthew 4:17 — `λέγειν` missing from "began to preach **and say**"; a stray `λέγει` sat in 4:22 where SBLGNT has none
- Matthew 7:14's `ὅτι` — stranded at the **end of a different section, four sections downstream**

Count the form corpus-wide, list every occurrence in both texts, map them. Don't assume locality.

## 8. Doctrinal errors hide inside "clunky"

**John 1:1** read *"and God was the Word."* It looked like ordinary wooden word order. It isn't — `ὁ λόγος` is articular (subject), `θεὸς` anarthrous (predicate). Reversing them makes the terms convertible: modalism. Fixed to *"and the Word was God."*

**Given that one, John's remaining 20 chapters need a doctrinal read, not just a style pass.**

Same class: **Romans 16:4** read *"all but the churches of the Gentiles are too"* — the opposite of Paul's meaning. `πᾶσαι` ("all") and `ἀλλὰ` ("but") in Greek order inverted the sense.

## 9. Chris's working style

- **Casual and direct.** Types fast, doesn't punctuate.
- **Prefers targeted fixes over rebuilds.** Don't propose rewrites when a splice will do.
- **Values honest assessment.** He asked *"do you think it's easy to read"* repeatedly. The right answer was *"I haven't read it yet, let me read it"* — not agreement.
- **Wants pace, and will say so.** He'll ask you to do more per turn. **Do not trade the pair-check for speed.** That check is the only thing standing between him and a broken product.
- **Report honestly, including your own bugs.** A bug was introduced in nearly every section — doubled "and", dropped quotation marks, duplicated verbs, gloss drift. Every one surfaced only from reading output back. Say so.

## 10. Track and report the count

He lost track of scope once because a "Matthew is now perfect" headline (about *Greek*) buried a one-line note that only 8 of 28 chapters were *readable*. **Keep those two things separate and state both every time.**

**As of 2026-08-04 this is finished: 260 of 260 chapters readable, 0 to go.** The two counts this section warns about keeping separate — Greek accuracy and readability — are both complete. Keep stating them separately anyway when reporting future work.

## 11. History of what went wrong (so you don't repeat it)

| Incident | Cause |
|---|---|
| Matthew 8 → *"with behold, they cried out"* | Content-search targeting hit the wrong `καὶ`. **Restored from original upload.** |
| Romans 2 §1 → *"chase glory and honor a life that never rots: a life that never rots"* | Index shift after a unit move. **Restored from original upload.** |
| Luke 5 §2 → *"he was there were sitting Pharisees"* | Over-triggered on a correct existential inversion. **Restored from original upload.** |
| Mark 6 → *"But others said, he is 'Elijah;'"* | Bad swap in a splice plan |
| Mark 13 → *"and will rise up children will rise up against parents"* | Plan kept the original English *and* assigned it elsewhere |
| Matthew 5:22 → *"'you fool!' **Will** be in danger"* | Capitalization pass fired after `!` inside a quotation |
| Luke 2:1, 2:22, 3:1, 5:1, 5:33, 6:9 | Gloss drift |

**The original upload is the safety net.** When a section is mangled, restore it from `/mnt/user-data/uploads/` (or Chris's original) and redo with explicit indices. Don't try to un-mangle in place.

## 12. Invariants — check all four after every session

```
Greek tokens ......... 137,554    (if this moves, something broke)
Word units ........... 117,353
SBLGNT discrepancies . 0          (was 4, all Romans; closed 2026-07-30)
Data files ........... all 12 in data/ parse
Gloss honesty ........ every English describes the Greek beneath it
```

The token figure in earlier copies of this file was **96,778**, from before the
last twenty books were added. If you are reading a number near that, the document
is stale, not the corpus.

## 13. Tone in reports

Show before/after tables. State the token count and discrepancy count every time. **Name your own bugs out loud** — they're the most useful thing you can report, because they're the ones nobody else will find.
