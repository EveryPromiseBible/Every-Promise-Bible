# -*- coding: utf-8 -*-
# Luke 17 §1 — two defects.
#
# BLOCK 1 (40,41): read "he said to them, “Going, show yourselves to the
#   priests.”" — a bare aorist participle where English needs a coordinate
#   imperative. Πορευθέντες is attendant-circumstance to the imperative
#   ἐπιδείξατε, so "Go and" is the same verb (πορεύομαι) in the form English
#   uses. Gloss-only; the opening quotation mark stays on it.
#
# BLOCK 2 (51,53): read "One now of them, seeing that he was healed…" —
#   postposed δέ left sitting inside the noun phrase. Pure reorder to
#   "Now one of them…"; the two glosses simply swap places and the sentence
#   capital moves with them (δέ takes "Now", εἷς takes "one").
CHAPTER = "Luke 17"
SECTION = 1
BLOCKS = [
    (40, 41, [
        (40, "“Go and"),   # Πορευθέντες
    ]),
    (51, 53, [
        (52, "Now"),   # δὲ
        (51, "one"),   # εἷς
    ]),
]
