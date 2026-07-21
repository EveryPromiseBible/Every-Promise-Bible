# -*- coding: utf-8 -*-
# Two drifts in Mark 9 §4:
#  (1) 9:42 — the labels slid one slot: μύλος ("millstone") was labelled
#      "a donkey’s", ὀνικὸς ("of a donkey") was blank, and the preposition περὶ
#      ("around") carried "millstone" while αὐτοῦ carried "around his".
#      Reordered so each gloss sits on its own word.
#  (2) 9:50 — καλὸν ("good") was labelled "is", and the supplied filler unit
#      carried "good;". Swapped so the adjective reads "good;" and the filler
#      supplies "is".
CHAPTER = "Mark 9"
SECTION = 4
BLOCKS = [
    (14, 20, [
        (15, "a donkey’s"),
        (14, "millstone"),
        (17, "were hung"),
        (16, "around"),
        (18, "his"),
        (19, None),
    ]),
    (106, 109, [
        (106, None),
        (108, "is"),
        (107, "good;"),
    ]),
]
