# PROJECT.md — Every Promise

> Complete developer handoff. Written for an AI agent with no access to prior conversations.
> **File:** `every_promise_site.html` — 7.5 MB, single file, zero build step, zero dependencies. Open it in a browser and it runs.

---

# Project Overview

## What this project is

**Every Promise** is a single-file web application containing a **Greek–English interlinear New Testament**. It is not a conventional Bible app. Its defining feature is that **every English word is anchored to a specific Greek word from the SBLGNT** (SBL Greek New Testament), and clicking any word opens its Strong's/Thayer's and Abbott–Smith lexicon entries.

The English is an **original paraphrase** called the **"Mak Translation"** (`tx.01` in the UI). It is grace-centered and thought-for-thought — readable modern prose, not a wooden gloss. But it is simultaneously a *strict interlinear*: no English word floats free of its Greek.

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
| Strong's/Thayer's entries | **5,357** |
| Abbott–Smith entries | **5,339** |
| Promise verses | **329** (15 meditations each) |

Books present: **the complete New Testament — Matthew (28), Mark (16), Luke (24), John (21), Acts (28), Romans (16), 1 Corinthians (16), 2 Corinthians (13), Galatians (6), Ephesians (6), Philippians (4), Colossians (4), 1 Thessalonians (5), 2 Thessalonians (3), 1 Timothy (6), 2 Timothy (4), Titus (3), Philemon (1), Hebrews (13), James (5), 1 Peter (5), 2 Peter (3), 1 John (5), 2 John (1), 3 John (1), Jude (1), Revelation (22).** All 27 books, in canonical order. The corpus is complete.

### Greek accuracy — verified against SBLGNT

Every chapter was checked word-by-word against **MorphGNT/SBLGNT** (`github.com/morphgnt/sblgnt`).

| Book | Discrepant words |
|---|---|
| Matthew | **0** |
| Mark | **0** |
| Luke | **0** |
| John | **0** |
| Acts | **0** |
| **Romans** | **4** |
| 1 Corinthians | **0** |

The 4 in Romans: ch3 `ὁ`→`ὄν`, ch8 `τὸν`→`τὸ`, ch13 `τὸν`→`τὸ`, ch15 `οὖν`→`οὐ`. All single-letter article/pronoun slips; none change meaning.

**This started at 11 and is now 4.** The fixes were not simple substitutions — in each case a word was *absent* at one site and *spurious* at another (e.g. Matthew 7:9 was missing `ὃν` and `ἢ` entirely, while 7:28 had a duplicate `ὁ` and a spurious `ἦν`).

### Readability — which books read as English

| Book | Chapters | Units | State |
|---|---|---|---|
| **Matthew** | 1–28 | 14,699 | **done** |
| **Mark** | 1–16 | 9,566 | **done** |
| **Luke** | 1–5, most of 6 | ~4,100 / 17,904 | **in progress** |
| Romans | 1–16 | 5,334 | good — was already |
| 1 Corinthians | 1–16 | 5,664 | good — was already |
| Acts | 13–28 | ~8,000 | good — was already |
| **Luke** | 6 (last sec) – 24 | ~13,800 | **wooden** |
| **John** | 1–21 | 15,094 | **wooden** |
| **Acts** | 1–12 | ~8,000 | **wooden** |

### Other completed work

- **Capitalization pass** — Romans, 1 Cor, Acts, Matthew. Was 56%/97%/87%/21% lowercase sentence-starts; now ~0.
- **Greek leaks cleared** — raw Greek was rendering *on the English line* in Matthew 6–7 (11 instances). 10 fixed; 1 remains (see Known Issues).
- **Romans prose repair** — 16 broken sentences, including Romans 6:3–4 (baptism passage, was two fragments) and Romans 16:4 (**meaning was inverted**: "all but the churches" → "but all the churches").
- **Romans 2 §1 voice rewrite** — 144 units re-authored.
- **John 1:1 doctrinal fix** — read **"and God was the Word."** The Greek `καὶ θεὸς ἦν ὁ λόγος` has `ὁ λόγος` articular (subject), `θεὸς` anarthrous (predicate). The reversal makes the terms convertible = modalism. Now reads **"and the Word was God."**
- **Luke 3:23 — restored a missing generation.** See "The Critical Bug" below.

## What is currently being worked on

**Luke, chapter by chapter, in canonical order.** Chapters 1–5 done; chapter 6 done through section 3 of 5. Next up: Luke 6 §4 ("The Tree and Its Fruit, the House and Its Foundation", 234 units).

## What still needs to be built

1. **Luke 6 §4 → Luke 24** (~13,800 units)
2. **John 1–21** (15,094 units) — roughest book remaining
3. **Acts 1–12** (~8,000 units)
4. **Matthew + Mark gloss audit** (see Known Issues — this may be more urgent than #1)
5. Prayer view — placeholder only
6. Journal view — placeholder only
7. My Stuff view — placeholder only
8. Search, Listen/TTS, Home buttons — rendered but inert
9. Favorites + History tabs — hardcoded empty states, no logic
10. Share button — inert
11. Cross-references — built, disabled behind `SHOW_CROSSREF = false`

---

# Architecture

## Top-level shape

One file. No bundler, no framework, no npm, no server. **Vanilla HTML + CSS + ES6.** Data is inlined as JavaScript object literals. Open the file → it works. Any build step would be a regression.

```
every_promise_site.html   (873 lines, 7.5 MB)
├── <head>
│   ├── Google Fonts <link>          (the ONLY external request)
│   └── <style>                       lines ~9–228
├── <body>
│   ├── <header>                      brand, top nav, bible toolbar
│   ├── <main>                        #view-promises, #view-meditate
│   ├── #view-bible                   (OUTSIDE <main> — full-width layout)
│   ├── #view-mystuff / #view-prayer / #view-journal   (placeholders)
│   ├── .bnav                         mobile bottom nav
│   ├── #defOverlay                   lexicon modal
│   ├── #noteOverlay                  note modal
│   └── <script>                      lines ~377–871
│       ├── PALETTE                   line 377
│       ├── const CHAPTERS = [...]    LINE 378  ← 4 MB
│       ├── const LEXICON  = {...}    LINE 379  ← 1 MB
│       ├── const PROMISES = [...]    LINE 380  ← 270 KB
│       ├── const ABBOTT   = {...}    LINE 381  ← 2.2 MB
│       └── application code          lines 382–871
```

> ⚠️ **The four data blobs are each exactly ONE LINE.** Line numbers are 1-indexed 378–381 = **0-indexed 377–380**. Every tool in this project depends on that. **Never pretty-print them.** A formatter would explode the file to millions of lines and break every script.

## Data schemas

### `CHAPTERS` — array of 149

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

### `PROMISES` — array of 329

```js
{
  reference: "Psalm 46:1",
  verse: "God is our refuge and strength...",
  meditations: [ "God is your refuge.", ... ],   // EXACTLY 15, always
  moods: ["Anxious", "Broken", ...]
}
```

**16 moods, hand-tagged:** Anxious (87), Overwhelmed (35), Stressed (30), Lonely (36), Waiting (51), Peaceful (78), Encouraged (132), Broken (67), Hopeful (112), Confused (61), Tired (31), Sick (30), Grateful (113), Joyful (32), Tempted (29), Angry (22).

> **`moods` is fully populated but NOT USED by any code.** It's built and waiting. Mood-based filtering is the obvious next feature and the data is ready.

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

## Currently working

### Promises (landing view)
- Verse of the day — random from 329 on load
- **Shuffle** — new random verse (guards against repeat)
- **Meditate** — opens the meditation stepper
- **Favorite** — heart toggle, **in-memory only, resets on reload**
- Share button — **inert**

### Meditate
- 15 meditations per verse, one at a time, large type
- Prev/Next with disabled states at bounds
- Dot indicator — click to jump; active dot elongates; **blue dot = user-added**
- **Add your own** — appends to session list. **Not persisted.**
- Back to promises

### Bible (the core)
- Chapter `<select>` — all 149, grouped by `<optgroup>` per book
- Three-line word stacks, 36-color cycling per section
- **Click any word → lexicon modal** with Strong's + Abbott–Smith
- Multi-token units show all entries stacked
- Abbott–Smith senses as recursive collapsible accordion
- **Study/Read toggle** — Read hides Greek+tags, gives clean prose
- **Highlight mode** — toolbar pencil; click words to highlight (yellow `#fdf0b8`); persists
- **Section bookmark** — icon per section heading; persists
- **Section notes** — modal textarea; persists; delete supported
- Library side panel — six tabs; auto-opens >1000px
- Esc closes lexicon modal
- Click-outside closes modals

### Library tabs
| Tab | State |
|---|---|
| Library | Static cards: Mak Translation (tx.01), Strong's+Thayer's (ref.01), Study Notes (ref.02), Gutenberg (an.01), Luther (an.02). **Only tx.01 + ref.01 are real.** |
| Bookmarks | **Working** — list, jump, remove |
| Notes | **Working** — list, jump, remove |
| Favorites | **Empty state only — no logic** |
| Highlights | **Working** — list, jump, remove |
| History | **Empty state only — no logic** |

### Responsive
- <1000px: bottom nav, stacked layout, smaller type

## Planned / stubbed

| Feature | Status |
|---|---|
| Mood filtering | **`moods` data is complete and unused. Lowest-hanging fruit in the codebase.** |
| Cross-references | Built, `SHOW_CROSSREF = false`, awaiting full NT |
| Prayer view | Placeholder |
| Journal view | Placeholder — "yearly themes and reflection" |
| My Stuff view | Placeholder |
| Search | Button rendered, inert |
| Listen / TTS | Button rendered, inert |
| Home button | Button rendered, inert |
| Favorites persistence | Tab exists, no code |
| History tracking | Tab exists, no code |
| Share | Button rendered, inert |
| Study Notes (ref.02) | Card exists; `section.notes` array exists and is empty everywhere |
| Antique facsimiles | Cards exist, nothing behind them |
| Rest of NT | 20 books not yet present |

---

# Current Priorities

**In order:**

### 1. Audit Matthew + Mark for gloss drift — DO THIS FIRST

44 chapters were completed **before** pair-checking was adopted. Drifted glosses may be sitting there right now, invisible, because **the English reads fine**. See the next section. This is the highest-value work available and it is not optional if the product's core promise is to hold.

### 2. Finish Luke
Luke 6 §4, then 7–24. Chapter by chapter, section by section.

### 3. John
Roughest book. **265 em-dash placeholders**, heaviest postposed genitives (284). John 1:1 already had a doctrinal inversion — **John's wooden chapters need a doctrinal read, not just a style pass.**

### 4. Acts 1–12

### 5. Mood filtering
Data is done. Pure UI work. Very high value-to-effort.

### 6. Favorites + History persistence
`loadStore`/`saveStore` already exist. Follow the bookmarks pattern exactly.

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
| Token count (96,778) | **Passes.** |

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

## 🟡 Open translation decisions — Chris's call, not the AI's

| Passage | Question |
|---|---|
| **Mark 1:41 — `ὀργισθεὶς`** | Currently "moved with indignation." SBLGNT prints the harder reading (angry) vs. `σπλαγχνισθεὶς` (compassion). **Long-standing open question. Never decided. Do not change it.** |
| **Romans 16:25–27 doxology** | Textual placement question. Unresolved. |
| **`—` placeholders** | 342 across Luke (77) + John (265). Romans already solved this by folding the article. **Chris chose chapter-by-chapter (Option B) over a bulk sweep — but the option stands.** |

## 🟡 Technical debt

| Item | Detail |
|---|---|
| **Positional keys** | Highlights key on `chapter:section:word`. **Any insert/delete/reorder silently re-points saved highlights.** Bookmarks/notes key on `chapter:section` — safer but still positional. |
| **No verse numbers** | Blocks precise error location, verse linking, cross-refs to standard refs. |
| **`section.notes` unused** | Present on all 149×N sections, empty everywhere. |
| **`moods` unused** | 329 verses tagged across 16 moods. Zero code touches it. |
| **In-memory favorites** | `let fav = false` — resets on reload. |
| **Dead buttons** | Home, search, listen, share. |
| **Fake library cards** | Study Notes, Gutenberg, Luther have no backing. |
| **`innerHTML` everywhere** | Lexicon/notes/lists built by string concat. Note text is user input rendered via `innerHTML` — **XSS is theoretical (local file, single user) but real.** |
| **Full re-render on every mutation** | `loadChapter()` after each bookmark/note/highlight change. Fine at current size. |
| **Google Fonts dependency** | The only network call. Offline → fallback fonts. |
| **7.5 MB single file** | ~2–4s parse on mobile. |

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
11. **Verify after every session:** 96,778 tokens · 4 SBLGNT discrepancies · all four blobs parse.

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

Current: **~92 of 149 chapters readable. ~57 to go.**

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
Greek tokens ......... 96,778     (if this moves, something broke)
SBLGNT discrepancies . 4          (all Romans; if this rises, Greek was damaged)
JSON blobs ........... all 4 parse
Gloss honesty ........ every English describes the Greek beneath it
```

## 13. Tone in reports

Show before/after tables. State the token count and discrepancy count every time. **Name your own bugs out loud** — they're the most useful thing you can report, because they're the ones nobody else will find.
