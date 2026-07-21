# TODO.md — Every Promise

> Working task list. See `PROJECT.md` for architecture, standards, and the full context.
> **Last updated:** end of Claude.ai session, before migration to Claude Code.

---

## What we're trying to achieve

Build a Bible that is **two things at once**, both required:

1. **Easy to read and makes sense.** Chris's words, verbatim. Not "faithful to Greek syntax," not "matches a style." The test is: *can a reader follow this without stopping?*
2. **Every English word honestly anchored to its Greek word.** Click a Greek word → the popup tells you what **that word** means. A beautiful sentence with a wrong label is a **broken product**.

**The work right now:** the corpus was built from a pipeline that produced good English glosses sitting in **Greek word order** — "there followed him crowds large." We're going book by book, section by section, reordering units into English order so the prose reads, while proving no Greek moves and every gloss stays honest.

**Progress: 260 chapters — THE ENTIRE NEW TESTAMENT IS COMPLETE. All 27 books (Matthew through Revelation) read as English, every English word anchored to its SBLGNT Greek word.** This session newly built 2 Corinthians (13 ch), Galatians (6 ch), Ephesians (6 ch), Philippians (4 ch), Colossians (4 ch), 1 Thessalonians (5 ch), 2 Thessalonians (3 ch), 1 Timothy (6 ch), 2 Timothy (4 ch), Titus (3 ch), Philemon (1 ch), Hebrews (13 ch), James (5 ch), 1 Peter (5 ch), 2 Peter (3 ch), 1 John (5 ch), 2 John (1 ch), 3 John (1 ch), Jude (1 ch), and Revelation (22 ch) — 20 whole books, authored fresh from the SBLGNT in the Mak voice, with new Strong's/Thayer's + Abbott–Smith lexicon entries for their vocabulary. Every chapter's Greek multiset verified equal to SBLGNT. The build pipeline is book-parametric (`tools/nt_*.py`, `BOOKS` registry). **No books remain to add.** The remaining work is the readability/gloss-drift audit of the older wooden chapters (the Matthew/Mark P0 below), not new books.**

**Note:** Matthew + Mark still carry the P0 gloss-drift audit (they were reordered before the pair-checking discipline existed). Luke, John, and Acts were each pair-read section-by-section as they were reordered.

---

## 🔴 P0 — Do this first

### [~] Audit Matthew + Mark for gloss drift — **Matthew DONE, Mark next**

**44 chapters were completed before pair-checking existed.** Drift may be sitting in them right now, invisible, because the English reads fine.

Gloss drift = reordering units *and* rewriting glosses in one step, which silently moves the English label onto the wrong Greek word. Every automated check passes on it: prose reads fine, Greek count is right, `splice` assertion passes. Only printing Greek→English pairs catches it.

- [x] Write a heuristic flagger — `tools/gloss_scan.py`. The useful signal is **DRIFT** (English matches a *neighbour's* definition, not its own), which is the reorder+regloss fingerprint: 712 flags corpus-wide vs 10,137 for a naive "no overlap with own def" test.
- [x] Expect false positives — confirmed, heavily. Matthew ran ~1 real per 12 flags. It is a triage list, not a verdict.
- [x] **Manually review the flagged set in Matthew 1–28** — all 93 flags read in context; **13 real drifts fixed** (8:8, 27:46, 27:50, 22:24, 26:39, 6:2, 6:14, 9:13, 13:21, 21:33, 4:23, 19:24, 7:12). Plans in `tools/plans/fix_mtNN_S.py`. See CHANGELOG 2026-07-19.
- [x] **Manually review the flagged set in Mark 1–16** — all 16 chapters pair-read in full; **~40 real drifts fixed** across 27 sections. Mark was in considerably worse shape than Matthew. Includes the `Ἠλίας`/`ἐστίν` "he is 'Elijah;'" swap that PROJECT.md lists as a *known past bug* — it had never actually been repaired in the data.
- [x] Pay special attention to units touched during reorders — genealogies, name lists, particle-heavy passages

### 🔴 [~] Readability pass — book by book — **Matthew DONE, 26 books to go**

Separate from the drift audit. Drift asks *"is this English label on the right
Greek word?"*; this asks *"would a reader stumble here?"* A section can be
perfectly anchored and still read as Greek word order.

**The finding that matters for planning: the defect rate is wildly uneven within
a single book.**

| Matthew | sections with a real prose defect |
|---|---|
| chapters 1–24 | 26 of 109 — **24%** |
| chapters 25–28 | 21 of 23 — **91%** |

The earlier "~2 defects per chapter" estimate came from chapters 1–19 and was far
too optimistic. **Sampling early chapters understates a book badly.**

Representative Matthew fixes:
- "over many things you I will put in charge" → "I will set you over many things"
- "And will be gathered before him all the nations" → "And all the nations will be gathered before him"
- "took off him the robe and put on him his clothes" → "stripped him of the robe and dressed him in his clothes"
- "'Of God I am the Son.'" → "'I am the Son of God.'"

Residue that **no earlier audit caught**, because prose reading is the only lens
that sees it: "there **there** will be weeping" (Mt 22:13, 24:51, 25:30 — `ἐκεῖ`
"there" plus `ἔσται` *also* glossed "there will be"), "it was all it was all
leavened", "collapse on on the way", "Peter answered him, said," (×3).

- [x] Matthew (158 sections)
- [x] **All 26 remaining books — 1,032 sections — DONE 2026-07-20**

### The defect rate is not uniform. It tracks how a book was BUILT.

| Band | Sections | Fixed | Rate |
|---|---|---|---|
| Luke 13–24 | 52 | 36 | **69%** |
| Luke 1–12 | 51 | 36 | **71%** |
| Acts 1–14 | 71 | 24 | 34% |
| Mark | 77 | 25 | 32% |
| John | 72 | 22 | 31% |
| Acts 15–28 | 69 | 19 | 28% |
| Matthew 25–28 | 23 | 21 | 91% |
| Matthew 1–24 | 109 | 26 | 24% |
| Romans | 74 | 9 | 12% |
| 1 Corinthians | 69 | 9 | 13% |
| Revelation | 59 | 9 | 15% |
| Galatians · 2 Cor · Hebrews · 2 Peter · Titus · 1 Pet · 2 Tim · 2 Th | 300 | 22 | 7% |
| **Eph · Col · Php · 1 Tim · 1 Th · 1 Jn · Jas · Jude · Phm · 2 Jn · 3 Jn** | **194** | **0** | **0%** |

The five hand-reordered books (Matthew, Mark, Luke, John, Acts) carry almost all
of it. The 20 books authored fresh by the `tools/nt_*.py` pipeline in the Mak
voice were already in English order and needed almost nothing — 194 sections
across eleven books needed **zero**.

**Lesson for any future corpus work:** sampling a book understates it badly, and
which band you sample decides your answer. The old "~2 defects per chapter"
estimate came from Matthew 1–19 and was wrong by a factor of three.

### ✅ [x] `tools/prose_scan.py` — the mechanical layer, exhausted 2026-07-20

Four checks with a real signature: duplicated adjacent words, doubled speech
verbs, fragment after a sentence end, capital continuing a sentence after a
closing quote. **Calibration mattered more than authoring** — the first
`quotecap` regex produced 524 hits that were essentially all correct English;
narrowed to words that rarely open a sentence, the whole tool went from 570
flags to 24.

Corpus-wide it now reports **20 flags, and reading them all: zero defects.**
Every `dup` ("had had the legion", "those who sleep sleep at night", "that that
deceiver") and every `frag` ("Which is easier…" after a question mark) is correct
English. Three `quotecap` hits are mild stylistic awkwardness, not errors.

It earned its keep first time out — it found 5 real defects **outside** Matthew
that a full read of Matthew 1–24 had already missed: 1 Cor 9:22 "I became to the
weak weak" → "To the weak I became weak", plus four identical fragments (Mk 10:8,
Ac 11:30, Ac 27:17, 1 Cor 2:13) where a full stop sat where a comma belonged and
stranded a relative pronoun.

**What this means:** the mechanical layer is done. Everything left needs reading.

### ✅ [x] Wrong Strong's numbers — 224 fixed (2026-07-19)

**The build gate could not catch this class.** "Every tag resolves to a LEXICON entry" (0 MISS) passes happily when a tag resolves to the *wrong* entry. Five ambiguous forms carried valid-but-wrong numbers:

| form | was | meaning shown | now | n |
|---|---|---|---|---|
| `δεῖ`/`ἔδει` | G1210 δέω | "bind" | **G1163** δεῖ | 89 |
| `ἱερῷ`/`ἱεροῦ` | G2413 ἱερός | "holy" *(adj)* | **G2411** ἱερόν | 70 |
| `μιᾷ`/`μίαν` | G1519 εἰς | *(preposition)* | **G1520** εἷς | 26 |
| `εἰδὼς` | G3708 ὁράω | "see" | **G1492** εἴδω | 22 |
| `μῆνας` | G3375 μήν | "+ surely" | **G3376** μήν | 17 |

Clicking "must" anywhere in the NT showed the definition of *bind*.

**Why it took two tools.** `tools/tag_audit.py` compares each tag's Strong's headword to the MorphGNT lemma — and found nothing, because **MorphGNT itself lemmatises `δεῖ` to `δέω`** (all 92 occurrences; `δεῖ` is morphologically 3sg of `δέω`). The tag agreed with the lemma source and was still wrong for the reader. A lemma check is structurally blind to this. `tools/tag_sense.py` instead asks whether the English we chose for a form *ever* shares a root with its tag's definition, aggregated over every occurrence — 89 consecutive misses is not a paraphrase. That found all five.

`tag_audit.py` remains useful as a second lens: it confirms the 20 pipeline-built books have **no** genuine head/lemma disagreements — all 503 of its classes are spelling traditions, voice lemmatisation, suppletive stems, or the documented textual-variant parallels.

- [x] **Remaining tail — exhausted 2026-07-20.** `tag_sense --min 3` read in full: every remaining flag is the tool string-matching a modern gloss against a KJV-era definition ("he wept" vs "bewail, weep"). Spot-checked the suspicious ones (φυλακή→"a haunt" Rev 18:2, αἴτιον→"guilt" Lk 23:4, λοιπόν→"Beyond that") — all correct senses. This lens is done.
- [x] **`tag_audit` run over all 27 books for the first time** (it had only ever covered the 20 pipeline-built ones). Found **one genuine mistag**: Romans 16:14 "Hermas" carried **G2061 = Ἑρμογένης**, a different person from 2 Tim 1:15. Correct entry **G2057 Ἑρμᾶς was absent from LEXICON entirely**, so the tagger took the nearest neighbour and nothing complained. Entry added, unit retagged.
- [x] The other 333 flagged (form, tag) pairs are benign: suppletive stems (φαγεῖν/ἐσθίω, ἐροῦμεν/λέγω), deponent listing conventions (πυρόω/πυρόομαι), spelling traditions (Μωσεύς/Μωϋσῆς, Καπερναούμ/Καφαρναούμ), and places where SBLGNT reads a different word than the text Strong's indexed — there the tag is the nearest true entry.
- [ ] **Admin and Arni (Luke 3:33) stay on G689 (Ἀράμ)** — a knowing compromise. They have no Strong's number at all, the tag regex is `/^G(\d+)/` so no synthetic key can resolve, and the genealogy-slot mapping is what standard SBLGNT interlinears use. Clicking them shows "Aram".
- [ ] `G687` and `G3391` are still absent from LEXICON. Neither is referenced by any tag, so nothing dangles today.

### ✅ [x] The defects a prose read CANNOT see — found by pair-reading, 2026-07-20

The most important finds of the whole audit. In every one of these the **English
already read correctly**, so no prose pass, no scanner, and no assertion could
see them. Only reading the Greek→English pairs could.

| Where | The label said | It should say |
|---|---|---|
| **1 Cor 10:22** | `ἰσχυρότεροι` → "are we provoking" | "stronger" — **a whole sentence was gone** |
| **Luke 1:35** | `τὸ γεννώμενον` → "the holy one" | "the one to be born" — swapped with `ἅγιον` |
| **Luke 1:64** | `ἀνεῴχθη` → "And immediately" | "was opened" — swapped with `παραχρῆμα` |
| **Luke 1:65** | `τὰ ῥήματα` → "these" | "the words" — swapped with `ταῦτα` |
| **Luke 3:23** | `ὤν` → "old," | "being" — glosses shifted one place left |
| **John 4:12** | `εἶ` → "than" | "are" — Greek has NO word for "than" |
| **John 4:24** | `ὁ` → "is" | (folded) — the clause is verbless; "is" is supplied |
| **Rom 16:14** | `Ἑρμᾶν` → G2061 *Hermogenes* | G2057 *Hermas* — **a different person** |

**Luke 3:23 is the same verse and the same one-place shift as the Heli
incident** — a second, separate residue that the original repair missed. That is
the strongest evidence that this class does not come in ones.

**1 Cor 10:22 was caused by a spent plan being re-applied.** `1cor10_2fix.py`
targeted indices 94/95 believing they were `παραζηλοῦμεν`/`τὸν κύριον`; by then
they were `ἰσχυρότεροι`/`αὐτοῦ`. Every assertion passed, because an overwrite
changes neither the Greek multiset nor the unit count. The file is deleted, and
`apply_plan.py` now **refuses any plan it has already applied** (ledger at
`tools/plans/APPLIED.log`, `--force` to override). A plan is a one-shot
instrument and the tool now enforces it.

### ✅ [x] Recitative ὅτι — 55 → 0 (2026-07-20)

`ὅτι` before DIRECT speech is a quotation marker with no English equivalent, not
the word "that". It was producing *he said that "I am…"*, which mixes indirect
and direct speech. Matthew had 0; the rest of the corpus had 55. Cleared by
`tools/fold_recitative.py`, whose rule is deliberately narrow so that `ὅτι`
before *indirect* speech — a real "that" — is never touched.

### ✅ [x] Luke, John and Acts — now genuinely read (was: NOT as verified as claimed)

The note above ("Luke, John, and Acts were each pair-read section-by-section as they were reordered") **cannot be relied on.** While triaging blank content words, **Luke 1:5** turned out to have glosses from the 1:12 sentence pasted onto it, with the prose itself broken:

> *"…a certain priest **And Zechariah was troubled when he saw him,** of Abijah;"*

That is the same failure class as Luke 3:23 (the missing Heli generation), sitting in **chapter 1** of a book recorded as done. Separately, **John 12:1** had the name `Ἰησοῦς` folded to blank and replaced by a pronoun, so the English never said who raised Lazarus.

- [x] Full read of Luke 1–24 — **103 sections, 72 fixed.** The never-audited 1–6 band did hold real drift: three crossed-gloss pairs and the second Heli-class shift.
- [x] Full read of John 1–21 — 72 sections, 22 fixed, plus the two anchoring repairs at 4:12 and 4:24.
- [x] Full read of Acts 1–28 — 140 sections, 43 fixed.

**Why this matters more than the flag counts:** both finds were invisible to `gloss_scan`'s DRIFT heuristic and surfaced only because a human-equivalent read the pairs. Automated triage narrows where to look; it does not certify anything.

### ✅ [x] Blank content-word sweep — 42 → 10 (2026-07-19)

`gloss_scan.py --blank` reports content words (V/N/A-) carrying no English of their own. Folding is sanctioned for particles and articles; folding a word that *has a dictionary meaning* is not. 32 of 42 were real drift. The 10 that remain are benign: copulas and pleonastic `λέγων` "saying".

**Compound numerals — resolved.** Nine numerals sat blank while the preceding word carried the whole value (clicking `τριάκοντα` "thirty" reported "thirty-eight"). No value was missing from any prose — **no Heli-class loss** — but the labels lied. All nine now split across their two Greek words, matching the convention already in Acts 1 ("a hundred twenty"), Acts 27, 1 Cor 10, Rev 14. Cost: a hyphen ("ninety-nine" → "ninety nine"). A proper multi-token merge would be better but `apply_plan.py` cannot express it (it asserts unit count is unchanged) — needs a new tool.

**⚠️ Known limit of the scanner:** it only inspects content-word (V/N/A) units, so it **cannot see a content word's label landing *on* a function word**. Matthew 9:13 (οὐ carrying "I did") and 13:21 (δέ carrying "comes") were invisible to it and surfaced only by full pair-reading. Flags are where to start, not the whole audit.

**Why P0:** Luke 3 had a whole generation missing (Heli) from exactly this bug, and it was found by luck. Matthew and Mark have never been checked.

---

## ✅ P1 — Finish Luke — DONE

**Luke 1–24 all readable.** Luke 6 §4 through Luke 24 §3 completed 2026-07-16
using the reusable `tools/` utilities; per-section plan modules live in
`tools/plans/lukeNN_S.py`. Every section verified by pair-reading; global
token count held at 96,778 throughout; **0 standalone `—` placeholders
remain in Luke** (all folded into adjacent units).

---

## 🟠 P2 — John (15,094 units)

**The roughest book remaining.** 284 postposed genitives, **265 `—` placeholders** (more than the rest of the corpus combined), 65 doubled articles.

### ⚠️ John needs a DOCTRINAL read, not just a style pass

John 1:1 read **"and God was the Word."** That's not clunky word order — `ὁ λόγος` is articular (the subject), `θεὸς` is anarthrous (the predicate). Reversing them makes the terms convertible, which is modalism. **Already fixed** to "and the Word was God." Given that one slipped through, assume there are others.

**Confirmed: there was another.** John 4:24 read **"Spirit is God"** — same trap: `ὁ θεός` is the articular subject, `πνεῦμα` the anarthrous predicate. **Fixed** to "God is spirit" (2026-07-17). Watch for every `X is Y` where Y carries the article.

Chapters done keep 1:1, 1:14 ("the Word became flesh"), 1:18 / 3:18 ("the only-begotten [Son of] God"), 3:16-17, and "the Son of Man" sayings with subject/predicate intact.

| | Ch | Sections | Units |
|---|---|---|---|
| [x] | John 1 | 4 | 817 | ✅ 2026-07-17 |
| [x] | John 2 | 2 | 420 | ✅ 2026-07-17 |
| [x] | John 3 | 2 | 630 | ✅ 2026-07-17 |
| [x] | John 4 | 4 | 911 | ✅ 2026-07-17 (4:24 doctrinal fix) |
| [x] | John 5 | 3 | 764 | ✅ 2026-07-17 |
| [x] | John 6 | 5 | 1,217 | ✅ 2026-07-17 |
| [x] | John 7 | 3 | 830 | ✅ 2026-07-17 |
| [x] | John 8 | 3 | 878 | ✅ 2026-07-17 (egō eimi / 8:58) |
| [x] | John 9 | 3 | 676 | ✅ 2026-07-17 |
| [x] | John 10 | 3 | 681 | ✅ 2026-07-17 (10:30) |
| [x] | John 11 | 5 | 929 | ✅ 2026-07-17 (11:25) |
| [x] | John 12 | 4 | 881 | ✅ 2026-07-17 |
| [x] | John 13 | 4 | 641 | ✅ 2026-07-17 |
| [x] | John 14 | 3 | 562 | ✅ 2026-07-17 (14:6) |
| [x] | John 15 | 3 | 485 | ✅ 2026-07-17 (15:1) |
| [x] | John 16 | 3 | 565 | ✅ 2026-07-17 |
| [x] | John 17 | 4 | 489 | ✅ 2026-07-17 |
| [x] | John 18 | 3 | 777 | ✅ 2026-07-17 |
| [x] | John 19 | 4 | 806 | ✅ 2026-07-17 (19:7,30) |
| [x] | John 20 | 4 | 599 | ✅ 2026-07-17 (20:28,31) |
| [x] | John 21 | 3 | 536 | ✅ 2026-07-17 (agapaō/phileō kept) |

**John COMPLETE (1–21).** All doctrinally-loaded sayings preserved through the reorder — see per-chapter commit messages.

**Known samples:** "Do not let be troubled your the heart" (14:1) · "In the house of the Father of mine dwelling places many there are" (14:2) · "I am the vine the true one, and the Father of mine the vinedresser is" (15:1) · "Was following now him a crowd large" (6:2)

---

## ✅ P3 — Acts 1–12 — DONE

Acts 13–28 already read well; chapters 1–12 (the original wooden block) were
reordered this session. **All of Acts now reads as English.**

| | Ch | Sections | Units |
|---|---|---|---|
| [x] | Acts 1 | 4 | 498 | ✅ 2026-07-17 (1:8 commission) |
| [x] | Acts 2 | 5 | 820 | ✅ 2026-07-17 (Lord and Christ) |
| [x] | Acts 3 | 3 | 487 | ✅ 2026-07-17 |
| [x] | Acts 4 | 4 | 666 | ✅ 2026-07-17 (no other name) |
| [x] | Acts 5 | 4 | 756 | ✅ 2026-07-17 |
| [x] | Acts 6 | 2 | 274 | ✅ 2026-07-17 |
| [x] | Acts 7 | 6 | 1,102 | ✅ 2026-07-17 (Stephen) |
| [x] | Acts 8 | 3 | 673 | ✅ 2026-07-17 |
| [x] | Acts 9 | 4 | 772 | ✅ 2026-07-17 (conversion) |
| [x] | Acts 10 | 5 | 825 | ✅ 2026-07-17 (no partiality) |
| [x] | Acts 11 | 9 | 527 | ✅ 2026-07-17 |
| [x] | Acts 12 | 7 | 492 | ✅ 2026-07-17 |

Every doctrinally-loaded verse preserved through the reorder — see per-chapter
commit messages. Greek multiset unchanged; 0 standalone `—` placeholders.

---

## 🟡 Data fixes — small, precise

### [ ] Romans — 4 Greek words vs SBLGNT — **DIAGNOSED 2026-07-20, not yet repaired**

**No longer blocked.** All 27 MorphGNT files are local, and the comparison has
been run. First, the scope is confirmed smaller than it looked: comparing all 16
Romans chapters throws up dozens of deltas, but **every one except these four is
an accent position (`πολλοὶ`/`πολλοί`, grave vs acute before a following word) or
a sentence-initial capital (`Καὶ`/`καὶ`)**. Those are not textual differences.
Stripping accents and case leaves exactly four:

| | We have | SBLGNT has |
|---|---|---|
| Romans 3 | `ὁ` | `ὃν` |
| Romans 8 | `τὸν` | `τὸ` |
| Romans 13 | `τὸν` | `τὸ` |
| Romans 15 | `οὖν` | `οὐ` |

**The important finding: each is a PAIR of errors, not one.** A duplicated token
in one verse masks an omitted token in another, which is why the chapter counts
matched and why nothing ever flagged them:

- **Romans 3** — `ὁ` is **duplicated at 3:30** (ours reads `εἷς ὁ` + `ὁ θεός`;
  SBLGNT 3:30 is `εἷς ὁ θεὸς`), and `ὃν` is **missing at 3:25** (`ὃν προέθετο ὁ
  θεὸς ἱλαστήριον`). Our unit S2 #45 `προέθετο` carries "presented him publicly"
  — the "him" is the absent `ὃν`.
- **Romans 15** — `οὖν` is **duplicated at 15:28** (ours has both S3 #70 `οὖν`
  and S3 #72 `τοῦτο οὖν`; SBLGNT has one `τοῦτο οὖν`), and `οὐ` is **missing at
  15:18** (`οὐ γὰρ τολμήσω`). The English negation is present and correct
  ("I wouldn't dare speak"), so **no meaning is affected** — only the Greek line
  is short a word.
- **Romans 8 and 13** — same shape, exact sites not yet pinned. Both chapters
  have units that bundle non-adjacent Greek (`τὸ τέλος φόρον` at 13 S0 #94),
  so the instance must be identified by context, not position.

**How to repair safely.** Unit count and token count both stay constant if you
do it as a swap: delete the duplicate token from its unit (if English remains on
that unit it simply becomes supplied filler, `["So", "", ""]`, which is legal),
and add the missing token plus its tag to the unit whose English already
supplies its sense. **Gate the write on a stronger invariant than usual: assert
the chapter's Greek multiset EQUALS SBLGNT afterwards**, not merely that it is
unchanged. That check makes the repair self-verifying.

**Do this in a fresh session, not at the end of a long one.** It is token-level
surgery on data stored out of order, and a careless version of exactly this is
what produced the 1 Corinthians 10:22 corruption.

### [x] Matthew 7:12 — the last Greek leak — **DONE 2026-07-19**
Was: *"for this and you also sums up the Law and the Prophets. Οὗτος γάρ"*

It turned out to be **gloss drift underneath**, not just a leak: `οὕτως` ("so")
was labelled "for this" (that's `οὗτος`), `αὐτοῖς` was labelled "also", and
`οἱ ἄνθρωποι` was labelled "to others". Re-authored in honest order; the surplus
`ἐστιν` returned to its own 7:9 clause (same section, multiset untouched).

**Corpus-wide Greek-in-English leaks: 0.**

### [ ] 1 lowercase sentence-start
2 Peter 2, "deeds. then". The "5" this file used to claim was miscounted: a naive
count gives 64, but since the quotation pass most of those are `…," he said`,
where lowercase is *correct*. Excluding a preceding `”` leaves exactly one.

### [x] 37 arity mismatches (Greek token count ≠ tag count) — **DONE 2026-07-19**
All 37 were the same defect: a Greek **article** carrying no tag, which silently
shifted every later tag onto the wrong word and left the last word unclickable.
24 were in Matthew 1's genealogy — the first chapter a reader opens.
Repaired by `tools/fix_arity.py`, which inserts `G3588 ART` **only** where the
token really is an article form and doing so makes the counts match exactly.
**Corpus-wide arity mismatches: 0.**

---

## 🔵 Decisions for Chris — NOT the AI's call

### [ ] Mark 1:41 — `ὀργισθεὶς`
Currently rendered **"moved with indignation."** SBLGNT prints the harder reading (angry) against `σπλαγχνισθεὶς` (moved with compassion) in other manuscripts. **Open since before this work started. Left untouched deliberately.**

### [ ] Romans 16:25–27 — the doxology
Textual placement question. Unresolved.

### [ ] The `—` placeholder convention
**Luke's 77 are now cleared** (folded into adjacent units during the chapter passes). **265 remain in John**, rendering the Greek article as a literal em-dash on the English line:
> "I have sinned against **—** heaven and before you"
> "said **—** Peter to **—** Jesus"

**Romans already solved this** by folding the article into the adjacent noun's unit. Applying that to Luke + John is a single mechanical pass.

Chris chose **Option B** (chapter-by-chapter, fix as you go) over the bulk sweep. **The option stands if he changes his mind** — it would clear a whole category fast.

---

## 🟢 Features — the app around the text

### ✅ [x] Mood filtering — **DONE 2026-07-20**
All 329 promise verses were **already tagged** across 16 moods and nothing read
them. Now wired up.

**Corpus grown 329 → 1,007 promises / 15,105 meditations (2026-07-20).** Every
added verse copied verbatim from a local public-domain KJV via `tools/kjv.py`;
nothing merged until it passed `tools/add_promises.py`. See CHANGELOG.

Counts at the time the picker was built (all 329 carried at least one mood):
Encouraged 132 · Grateful 113 · Hopeful 112 · Anxious 87 · Peaceful 78 · Broken 67 · Confused 61 · Waiting 51 · Lonely 36 · Overwhelmed 35 · Joyful 32 · Tired 31 · Sick 30 · Stressed 30 · Tempted 29 · Angry 22

- [x] Mood picker UI on the Promises view — top row, centred, across from the
      "verse of the day" kicker
- [x] Filter `PROMISES` by selected mood(s)
- [x] "How are you feeling today?" entry point (the prompt above the pills)

**Design decisions worth knowing:**
- **The mood list is derived from `PROMISES`, not hardcoded.** A mood added to
  the data appears automatically; one removed cannot leave a dead button behind.
  Ordered by how many promises carry it.
- **Multiple moods take the UNION, not the intersection.** Someone both anxious
  and tired wants either verse, and intersecting 16 moods empties out fast.
- **`shuffleVerse` had to be fixed, not just extended.** Its fallback was
  `(n+1) % PROMISES.length`, which steps to the next promise in the whole
  corpus — with a filter on, that hands back a verse the chosen mood does not
  carry. It now steps within the filtered pool.
- Selection persists via the existing `loadStore`/`saveStore` pattern
  (`everypromise_moods`), so a mood survives reload.
- `moodPool()` falls back to the full list if a filter ever matches nothing, so
  the page cannot go blank.

Verified: all 4 data blobs parse; the full 8.7 MB script parses cleanly under
esprima; mood counts and union semantics checked against the real data.
**Not verified: the visual layout** — that needs a human to open the page.

### [ ] Favorites — persist
Tab exists with a hardcoded empty state. `let fav = false` resets on reload.
- [ ] Follow the bookmarks pattern exactly: `loadStore('favorites')` → mutate → `saveStore` → re-render
- [ ] Wire `toggleFav()` to storage
- [ ] Render `#tab-favorites`

### [ ] History — track and persist
Tab exists with a hardcoded empty state, no logic.
- [ ] Record chapter views in `loadChapter()`
- [ ] Cap the list (last 50?)
- [ ] Render `#tab-history`

### [ ] Meditations — persist custom entries
`addCustomMeditation()` appends to a session array. Lost on reload.

### [ ] Search
Toolbar button `🔍` rendered, inert.
- [ ] English text search across `CHAPTERS`
- [ ] Greek search
- [ ] Strong's number search (`OCCURRENCE_INDEX` already exists and is built at load)

### [ ] Cross-references — re-enable
`SHOW_CROSSREF = false`. Code is written and working. The comment says: *"re-enable once the full NT is translated and this can be retuned against full-corpus word frequency."*
- [ ] Blocked on: full NT corpus
- [ ] Then retune `CROSSREF_MAX` (currently 12) against real frequency

### [ ] Prayer view
Placeholder — "your prayer space"

### [ ] Journal view
Placeholder — "yearly themes and reflection"

### [ ] My Stuff view
Placeholder — "favorites, notes, highlights, library"

### [ ] Share button
Inert.

### [ ] Listen / TTS
Toolbar button `🔊` rendered, inert.

### [ ] Home button
Toolbar button `⌂` rendered, inert.

### [ ] Study Notes (ref.02)
Library card exists. `section.notes` array exists on all 149×N sections and is **empty everywhere**. The plumbing is there.

---

## ⚪ Technical debt

### [ ] Positional keys break on edit
Highlights key on `chapterIdx:sectionIdx:wordIdx`. **Every splice silently re-points saved highlights after the edit point.** Bookmarks/notes key on `chapterIdx:sectionIdx` — safer but still positional.

Options: content hash, stable unit IDs, or accept it and document that highlights may drift during translation work.

### [ ] No verse numbers
Blocks: precise error location, verse linking, standard cross-refs, sharing a verse. Adding them means re-aligning against MorphGNT's `BBCCVV` column — real work, real payoff.

### [ ] `innerHTML` for user input
Note text renders via `innerHTML`. XSS is theoretical (local file, single user) but real.

### [ ] Full re-render on every mutation
`loadChapter()` fires after each bookmark/note/highlight change. Fine at current size.

### [ ] 7.5 MB single file
~2–4s parse on mobile. The single-file architecture is deliberate and worth keeping — but worth knowing.

### [ ] Google Fonts is the only network call
Offline → fallback fonts. Consider embedding if offline matters.

### [ ] Fake library cards
Study Notes, Gutenberg, Luther have nothing behind them.

---

## 📋 Future — beyond the current corpus

- [ ] The remaining 20 NT books (currently: Matthew, Mark, Luke, John, Acts, Romans, 1 Corinthians)
- [ ] Then re-enable cross-references and retune
- [ ] Then the promises dataset can expand past 329

---

## ✅ Done

- [x] **Matthew 1–28** — readable (14,699 units)
- [x] **Mark 1–16** — readable (9,566 units)
- [x] **Luke 1–24 — readable (complete)** — Luke 6 §4 → Luke 24 done 2026-07-16; 0 `—` placeholders remain in Luke
- [x] **Greek accuracy: 11 → 4 discrepancies** vs SBLGNT. Matthew, Mark, Luke, John, Acts, 1 Cor all **perfect**.
- [x] **Capitalization** — Romans, 1 Cor, Acts, Matthew (was 56%/97%/87%/21% lowercase sentence-starts → ~0)
- [x] **Greek leaks** — 11 in Matthew 6–7 → **0 corpus-wide** (last one, 7:12, closed 2026-07-19)
- [x] **Matthew gloss-drift audit** — all 28 chapters pair-read; 13 real drifts fixed
- [x] **Romans prose** — 16 broken sentences repaired, incl. Romans 6:3–4 (baptism, was fragments) and **Romans 16:4 (meaning was inverted)**
- [x] **Romans 2 §1** — 144 units re-authored
- [x] **John 1:1** — "and God was the Word" → **"and the Word was God"** (doctrinal)
- [x] **Luke 3:23** — restored **Heli**, a missing generation in the genealogy
- [x] `PROJECT.md` written

---

## The workflow (per section)

1. Dump units: `{index}|{english}|{greek}`
2. Read the prose — find Greek-order sentences
3. Author a `splice` plan with **explicit indices**
4. Run — assertions guard the Greek
5. **Print Greek→English pairs for every unit touched** ← the step that catches drift
6. Read the prose back
7. Verify: 96,778 tokens · 4 SBLGNT discrepancies · 4 blobs parse
8. Save

## The rules that matter

> **Reorder units, OR rewrite glosses — never both in one step.**
>
> **Never edit by content search.** `[k for k,w in enumerate(ws) if w[1]=='καὶ'][0]` hits the wrong instance.
>
> **Not every inversion is an error.** "was healed the servant" is wrong. "there were sitting Pharisees" is correct English.
>
> **Metrics lie. You must read.** Three proxies were tried; all three were wrong.
>
> **Folds first, capitalization last.**
>
> **Restore from the original upload when a section is mangled.** Don't un-mangle in place.

## Invariants — check every session

```
Units ................ 117,353
Greek tokens ......... 137,554
SBLGNT discrepancies . 4  (all Romans)
JSON blobs ........... all 4 parse
Arity mismatches ..... 0   (Greek token count == tag count, every unit)
Unresolvable tags .... 0   (every G-number present in LEXICON)
Greek-in-English ..... 0   leaks
Gloss honesty ........ every English describes the Greek beneath it
```

The 96,778 figure this file carried until 2026-07-20 predated the 20 books added
in the final build session. Anything quoting it is stale.
