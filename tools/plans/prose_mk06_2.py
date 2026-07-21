# -*- coding: utf-8 -*-
# Mark 6:25 read "I want that at once you give me on a platter the head of John
# the Baptist" — Greek order throughout: the adverb and the prepositional
# phrase both sit ahead of the object.
# This gives "I want that you give me at once the head of John the Baptist on a
# platter."
# Pure reorder; the only gloss edits move the closing full stop and quotation
# mark from the old last unit to the new last unit.
CHAPTER = "Mark 6"
SECTION = 2
BLOCKS = [
    (173, 183, [
        (173, None),            # Θέλω — “I want
        (174, None),            # ἵνα — that
        (176, None),            # δῷς — you give
        (177, None),            # μοι — me
        (175, None),            # ἐξαυτῆς — at once
        (180, None),            # τὴν κεφαλὴν — the head
        (181, None),            # Ἰωάννου — of John
        (182, "the Baptist"),   # τοῦ βαπτιστοῦ — loses the full stop/quote
        (178, None),            # ἐπὶ — on
        (179, "a platter.”"),   # πίνακι — takes the full stop and closing quote
    ]),
]
