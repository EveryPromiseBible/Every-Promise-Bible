# Every Promise — Project Handoff

**File:** `every_promise_site.html` (7.5 MB, single file, no dependencies)
**As of:** end of this session

---

## 1. What this project is

A Greek–English interlinear New Testament where **every English word is anchored to a specific SBLGNT Greek word**. Clicking a Greek word opens Strong's/Thayer's and Abbott–Smith definitions. The English is a grace-centered, thought-for-thought paraphrase — readable prose, not a gloss — but the anchoring must stay honest, because the whole promise of the site is: *click this Greek word, learn what **this word** means.*

Two goals in tension, both required:
1. **Easy to read and makes sense** (the stated standard)
2. **Every gloss honestly describes the Greek word beneath it**

---

## 2. File structure

Single HTML file. Four JSON blobs on lines 378–381 (0-indexed 377–380):

| Line | Blob | Size |
|---|---|---|
| 378 | `CHAPTERS` | 260 chapters, 117,353 word units |
| 379 | `LEXICON` (Strong's/Thayer's) | 5,357 entries |
| 380 | `PROMISES` | 329 verses + meditations |
| 381 | `ABBOTT` (Abbott–Smith) | 5,339 entries |

**Word unit shape:** `[english, greek, tags]`
- `greek` may hold multiple tokens (folded articles/particles)
- `tags` is ` · `-separated Strong's + morphology, one per Greek token
- Empty `greek` = supplied English (black italic filler)
- Empty `english` + present `greek` = folded particle (renders Greek with no English above)

**Units are stored in ENGLISH reading order**, not Greek order. Greek order within the data already differs from SBLGNT — this is by design. The invariant is the **multiset** (nothing lost/added), not the sequence.

---

## 3. Current state

### Greek accuracy vs. SBLGNT (authoritative check)

| Book | Discrepant words |
|---|---|
| Matthew | **0** |
| Mark | **0** |
| Luke | **0** |
| John | **0** |
| Acts | **0** |
| **Romans** | **4** |
| 1 Corinthians | **0** |

The 4 in Romans: ch3 `ὁ`→`ὄν`, ch8 `τὸν`→`τὸ`, ch13 `τὸν`→`τὸ`, ch15 `οὖν`→`οὐ`. All single-letter article/pronoun slips; none change meaning. They need verse-level alignment to pin the exact occurrence, and the data has no verse numbers — only section headings.

### Readability

| | Chapters | Units | State |
|---|---|---|---|
| **Matthew** | 1–28 | 14,699 | **done** |
| **Mark** | 1–16 | 9,566 | **done** |
| **Luke** | 1–5 + most of 6 | ~4,100 of 17,904 | **in progress** |
| Romans | 1–16 | 5,334 | good (was already) |
| 1 Corinthians | 1–16 | 5,664 | good (was already) |
| Acts | 13–28 | ~8,000 | good (was already) |
| **Luke** | 6 (last sec) – 24 | ~13,800 | **wooden** |
| **John** | 1–21 | 15,094 | **wooden** |
| **Acts** | 1–12 | ~8,000 | **wooden** |

**Roughly 57 chapters / ~37,000 units remain.**

---

## 4. THE CRITICAL BUG — read this first

### Gloss drift

When you reorder units **and** rewrite glosses in the same step, the English comes out reading perfectly while the label under the Greek drifts onto the wrong word.

Real example from Luke 2:1. Produced this, which reads fine:

> "Now it happened in those days that a decree from Caesar Augustus went out that all the inhabited world should be registered."

But underneath:

| Greek | was labelled | should be |
|---|---|---|
| `ἐξῆλθεν` (went out) | **"that"** | "went out" |
| `ἀπογράφεσθαι` (to be registered) | **"went out that"** | "should be registered" |
| `οἰκουμένην` (inhabited world) | **"inhabited world should be registered"** | "inhabited world" |

Click `ἐξῆλθεν` → popup says "that".

**Why nothing catches it:**
- The prose read-back doesn't catch it — the prose *reads fine*
- The Greek multiset check doesn't catch it — no Greek was lost
- Only printing each **Greek → English pair** catches it

### The rule that works

> **Reorder units, OR rewrite glosses — never both in one step. Then print every pair you touched and read them.**

### ⚠️ Matthew and Mark were NOT checked this way

I only started printing pairs partway through Luke. **Matthew (28 ch) and Mark (16 ch) were done while reading prose only.** Drifted glosses may be sitting in those 44 chapters right now, invisible.

**Recommended next action:** audit Matthew and Mark for gloss drift before continuing forward.

### How this surfaced a real content error

Luke 3:23 — the genealogy. The English read:

> "being a son— as it was supposed— of Joseph, **of Matthat**, of Levi..."

**Heli was missing.** `τοῦ Ἠλὶ` was present in the Greek but labelled "of Joseph," and every gloss from `υἱός` onward had shifted one place. Luke's genealogy runs *through Heli* — it's what distinguishes Luke's account from Matthew's. The prose read fine. The Greek count was clean. Only pair-checking found it.

---

## 5. Method — how to do this work

### The core insight

The wooden chapters have **good English glosses in Greek word order**. `ἠκολούθησαν αὐτῷ ὄχλοι πολλοί` glossed in place gives "there followed him crowds large." Reorder the same four units → "large crowds followed him." **The Greek rides along for free.**

So most of the fix is *reordering units*, not rewriting.

### The `splice` helper (in `mk.py`)

```python
def splice(ws, a, b, plan):
    """replace ws[a:b] with units reordered per plan=[(old_abs_index, new_en|None),...]"""
    seg = [list(w) for w in ws[a:b]]
    assert sorted(i for i,_ in plan) == list(range(a,b)), 'plan must cover exactly that span'
    new = []
    for i, en in plan:
        u = list(ws[i])
        if en is not None: u[0] = en
        new.append(u)
    assert Counter(t for w in seg for t in w[1].split()) == \
           Counter(t for w in new for t in w[1].split()), 'splice changed Greek'
    ws[a:b] = new
```

The assertions block bad writes. They caught span errors and a case where a `sed` patch mapped `γάρ` ("For") onto "happened?". **They cannot catch gloss drift.**

### Per-section workflow

1. Dump units: `{index}|{english}|{greek}`
2. Read the prose to find Greek-order sentences
3. Author a `splice` plan with **explicit indices**
4. Run — assertions guard the Greek
5. **Print the Greek→English pairs for every unit touched**
6. Read the prose back
7. Verify SBLGNT count unchanged; save

### Verification commands

```python
# SBLGNT multiset check (needs sblgnt-master/ from morphgnt/sblgnt)
# authoritative surface form is MorphGNT column index 4 (NOT 5 — that's normalized)

# Greek leaking into English line
GREEK = re.compile(r'[\u0370-\u03ff\u1f00-\u1fff]')
[... for e,g,t in s['words'] if GREEK.search(e)]

# lowercase sentence-starts
prev.endswith(('.','?','!')) and cur[:1].islower()
```

---

## 6. Traps and lessons learned

| Trap | Detail |
|---|---|
| **Editing by content search** | `[k for k,w in enumerate(ws) if w[1]=='καὶ'][0]` hits the wrong instance — `καὶ` appears dozens of times per section. Broke Matthew 8 ("with behold, they cried out") and Luke 2. **Use explicit indices.** |
| **Index shift after delete/move** | Every index after a `pop` shifts. Broke Matthew 8 and Romans 2. Author the whole plan; assert every unit consumed exactly once. |
| **Order of operations** | Folds first, capitalization **last**. My capitalization pass ran first and helpfully capitalized leaked Greek ("Νηστεύοντες"); removing those units then exposed lowercase sentences underneath. Had to re-run. |
| **Not every inversion is an error** | "there were sitting Pharisees" is correct English (existential inversion). "was healed the servant" is not. I over-triggered on this in Luke 5 and broke a working section. |
| **Chapter-opening samples are unreliable** | They made Matthew 9–28 look wooden (it mostly wasn't) and my "multi-word unit %" metric made it look fine (it wasn't). **A filler-ratio metric flagged 1 Cor 13 as wooden — it's beautiful.** There is no proxy. You must read. |
| **`sed` on plan files** | Produced a plan mapping `γάρ` onto "happened?". Rewrite the plan by hand instead. |

---

## 7. Recurring wooden patterns — RE-MEASURED 2026-07-19

**The numbers in the previous version of this section were badly out of date and
were sending sessions hunting problems that no longer exist.** Current, verified:

| Pattern | Total | Worst books | Status |
|---|---|---|---|
| Postposed δέ rendered "now" | **386** | Luke 172, John 86, Acts 51 | **the one large pattern left** |
| Postposed genitive ("of his", "of them") | **124** | Luke 27, Matthew 17, Mark 12, Acts 12 | modest, spread thin |
| `—` placeholder for the article | **2** | Mark 1, Romans 1 | effectively done (was 342) |
| Doubled article | **0** | — | **done** (was 65) |
| "a X certain" | **0** | — | **done** |
| Lowercase sentence-start | **1** | 2 Peter 2 ("deeds. then") | effectively done |
| Arity mismatches | **0** | — | **done** (was 37) |
| Greek leaking into English | **0** | — | **done** |
| Unbalanced quotations | **2 sections** | Luke 15 §3–§4 | **done** — those 2 are a legitimate cross-section speech |

The em-dash sweep, the doubled-article sweep and the "a X certain" sweep are all
**finished**. Do not plan work around them.

⚠️ **Careful measuring lowercase sentence-starts.** A naive check counts a
lowercase word after any `.`/`?`/`!` — but since the quotation pass, sentences
frequently end `…,” he said`, where lowercase is *correct*. Excluding a preceding
`”` takes the count from a spurious 64 to the true 1.

### What is actually left of readability

Not a pattern problem. The remaining defects are prose judgement — Greek word
order standing in English where every label is honest and every word present:

> "over all his possessions he will put in charge him."
> "Let the little children and do not hinder them come to me"
> "which is translated, 'Of a Skull Place.'"

**There is no detector for this.** It has no signature: the glosses are correct,
the multiset is correct, nothing is missing. The only way through is reading. See
§9 for the recommended approach.

---

## 8. Known open items — updated 2026-07-19

### Closed since the last handoff
- ~~Matthew 7:12, the last Greek leak~~ — **closed.** It was gloss drift underneath: `οὕτως` glossed "for this" (that's `οὗτος`), `αὐτοῖς` glossed "also". The surplus `ἐστιν` was returned to its 7:9 clause. **Corpus-wide Greek-in-English leaks: 0.**
- ~~37 arity mismatches~~ — **closed.** All 37 were an untagged Greek article; `tools/fix_arity.py` inserted `G3588 ART` at each. 24 were in Matthew 1's genealogy, so those words were unclickable on the first page a reader opens.
- ~~5 lowercase sentence-starts~~ — **1 remains** (2 Peter 2, "deeds. then").
- ~~Matthew + Mark gloss-drift audit~~ — **closed.** Both books fully pair-read; ~53 real drifts fixed.

### Still open
1. **Romans — 4 Greek words** (ch3, 8, 13, 15). Needs verse-level alignment against MorphGNT. Note MorphGNT for all 27 books is now in `tools/data/` (gitignored), so this is unblocked.
2. **Mark 1:41 — `ὀργισθεὶς`.** Currently "moved with indignation." SBLGNT prints the harder reading (angry) vs `σπλαγχνισθεὶς` (compassion). **A long-standing decision for Chris, never made.** Left untouched.
3. **Cross-references** — `SHOW_CROSSREF = false`. The full NT corpus now exists, so the blocker is gone; this can be re-enabled and tested.
4. **Quote convention inconsistency.** Sections are now self-contained (each closes its own quotation). But some long speeches used a competing habit — first section opens, intermediate sections carry no quotes at all, last section closes (Acts 7 §1–§4, Acts 13 §3–§7, Acts 26 §1–§2, Mark 13 §2–§3). Those middle sections are internally balanced so nothing flags them, but a long speech now reads quoted / unquoted / unquoted / quoted. **A taste decision, not a bug.**
5. **Strong's tag tail.** `tools/tag_sense.py --min 3` lists ~60 low-frequency forms whose gloss never matches their tag. Every one checked so far was a false positive (English morphology, spelling tradition, translation choice), but the tail is not exhausted. `G687` and `G3391` are absent from LEXICON — nothing points at them, but a future tag would dangle.
6. **Luke 1–6 never sampled.** The Luke drift sample used chapters 4/11/18/22, which are in the *unreordered* band — and text that was never reordered cannot drift. Luke 1–6 *were* reworked, and that is where Luke 1:5 broke. The low measured rate (1.5/1k) does not cover them.

---

## 9. Recommended next steps

The accuracy work is in good shape. Verified against the pre-audit baseline
(commit `71ca43e`) after ~150 edits: **0 of 260 chapters had their Greek multiset
change**, 0 leaks, 0 unresolvable tags, 0 arity mismatches, units 117,353 /
tokens 137,554 unchanged throughout.

**The remaining work is prose quality, and it cannot be automated.** See §7.

**Recommended: a book-by-book prose read, starting with Matthew as a pilot.**
Read the joined prose (not the pairs — this pass is about how it *reads*), mark
every sentence that makes a reader stop, and fix by reordering units. Measure how
many real defects one book yields before committing to all 27.

**Two cautions from this session's experience:**

- **Precision over recall.** A reorder that improves prose can move a gloss onto
  the wrong Greek word — that is exactly the drift bug, re-introduced. Every
  prose fix must still be pair-checked before it lands. Use `apply_plan.py`,
  never hand-edit.
- **Do not batch the writing.** One subagent read all 38 Matthew sections and
  then died to an API error before writing a single plan file; the entire run was
  lost. Author and validate incrementally.

**What NOT to do:** do not plan an em-dash sweep, a doubled-article sweep, or an
"a X certain" sweep. They are finished. The stale counts in the previous version
of §7 would have sent you after all three.

If pushing forward, the order that makes sense is **Luke → John → Acts 1–12**. John is the roughest (265 placeholders, heaviest postposed genitives) and had a **doctrinal error already fixed**: John 1:1 read *"and God was the Word"* — subject and predicate inverted, which is a different doctrine (modalism). It now reads *"and the Word was God."* **Given that one, John's wooden chapters likely need a doctrinal read, not just a style pass.**

---

## 10. Invariants to hold

- **Greek tokens: 137,554.** If this number moves (outside a deliberate book addition), something broke.
- **SBLGNT discrepancies: 4** (all Romans). If this rises, Greek was damaged.
- **All four JSON blobs must parse.**
- Every gloss must honestly describe the Greek beneath it.

Verify all four after every session.
