# -*- coding: utf-8 -*-
# Mark 10:38 read "or the baptism that I am baptized with to be baptized with?" —
# Greek order leaves the infinitive stranded at the end after its own object
# clause, so the reader meets "baptized with ... to be baptized with".
# This gives "or to be baptized with the baptism that I am baptized with?"
# Pure reorder; the only gloss edits move the question mark and closing quote
# to the new final unit.
CHAPTER = "Mark 10"
SECTION = 3
BLOCKS = [
    (121, 127, [
        (121, None),                     # ἢ — or
        (126, "to be baptized with"),    # βαπτισθῆναι — loses "?”"
        (122, None),                     # τὸ βάπτισμα — the baptism
        (123, None),                     # ὃ — that
        (124, None),                     # ἐγὼ — I
        (125, "am baptized with?”"),     # βαπτίζομαι — takes "?”"
    ]),
]
