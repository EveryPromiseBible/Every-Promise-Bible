# tools/ — Every Promise translation utilities

Reusable helpers for the interlinear translation work. **Local authoring tools
only** — they are not part of the app. `index.html` stays the single, authoritative,
build-free source; these scripts just read and rewrite its inline data blobs
in place, preserving the exact single-line, UTF-8 layout.

Requires Python 3 (stdlib only — no packages, no build step).

## Files

| File | What it does |
|---|---|
| `epcore.py` | Core: load/edit/save the 4 blobs; `splice()`; counts; invariants. |
| `baseline.py` | Verify global invariants (98,006 units / 114,218 tokens); show a chapter's sections. |
| `dump_section.py` | Dump a section's units as `{index}|{english}|{greek}` to author a plan. |
| `pair_print.py` | Print every Greek→English pair + joined prose (the gloss-honesty check). |
| `apply_plan.py` | Apply a section plan; dry-run pair-print by default, `--write` to save + re-verify. |
| `plans/` | Per-section reorder/gloss plans (data). One file per section worked. |

### Building a new book (used for 2 Corinthians, then Galatians — now book-parametric)

The `nt_*` tools take a book key from the `BOOKS` registry in `nt_tags.py`
(e.g. `Ga`); add a book by adding one registry entry. The older `co2_*` tools
are the 2 Corinthians-specific originals kept for reference.

| File | What it does |
|---|---|
| `nt_tags.py` | Resolve every SBLGNT word of `<book> <ch>` to `G#### MORPH` (form-match → app LEXICON → verified overrides → Strong's dict). |
| `nt_words.py` | List a chapter's numbered source words (index · Greek · tag · gloss hint). |
| `nt_assemble.py` | Assemble from `plans/<slug>_<ch>.py`; assert multiset == SBLGNT; `--check` / `--write`. |
| `nt_lex.py` | Emit + merge new-vocabulary LEXICON/ABBOTT entries for a book. |

| File | What it does |
|---|---|
| `lex_build.py` | Parse the public-domain sources (Strong's Greek Dict XML; Abbott-Smith TEI) into the app's LEXICON/ABBOTT format; `validate` reproduces existing entries exactly before minting new ones. |
| `co2_tags.py` | Resolve every SBLGNT word of a 2 Cor chapter to `G#### MORPH` — corpus form-match → app LEXICON lemma → verified `data/co2_lemma_overrides.json` → Strong's dict. Nothing invented. |
| `co2_words.py` | List a chapter's numbered source words (index · Greek · tag · gloss hint) — the backbone the paraphrase is authored against. |
| `co2_assemble.py` | Assemble a chapter from `plans/co2_<ch>.py`; assert Greek multiset == SBLGNT; `--check` prints prose, `--write` inserts into CHAPTERS. |
| `co2_lex_emit.py` / `co2_insert_lex.py` | Emit and merge the new-vocabulary LEXICON/ABBOTT entries. |
| `plans/co2_<ch>.py` | Per-chapter authoring plan: reading-order English anchored to source-word indices. |

Raw sources under `tools/data/` (Strong's/Abbott-Smith/MorphGNT) are gitignored;
re-download via the URLs in the script headers.

## Per-section workflow

```
python tools/dump_section.py "Luke 7"          # list sections
python tools/dump_section.py "Luke 7" 0        # dump units -> read the prose
# author tools/plans/luke07_0.py  (CHAPTER, SECTION, BLOCKS)
python tools/apply_plan.py tools/plans/luke07_0.py            # dry run: read every pair
python tools/apply_plan.py tools/plans/luke07_0.py --write    # save + verify invariant
```

## The rules (from PROJECT.md / HANDOFF.md)

- Reorder units OR rewrite glosses — if you do both, **print every touched pair and read them.**
- `splice()` guards the Greek multiset; it **cannot** catch gloss drift. Only reading pairs can.
- Never pretty-print the blobs. Never edit `index.html` by hand for data changes.
- Invariants after every write: 98,006 units · 114,218 tokens · 4 blobs parse · every gloss honest.
