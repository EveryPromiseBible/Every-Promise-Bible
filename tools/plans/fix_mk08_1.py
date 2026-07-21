# -*- coding: utf-8 -*-
# Mark 8 §1 — #46-47: the negation of οὐκ εἶχον was stripped from its own unit
# ("they had") and parked on the preposition μεθ’ ("nothing with"). Re-glossed in
# place so the negative verb keeps its negative and μετά reads simply "with".
# Prose "they had nothing with them in the boat" is unchanged.
CHAPTER = "Mark 8"
SECTION = 1
BLOCKS = [
    (46, 49, [
        (46, "they had nothing"),  # οὐκ εἶχον
        (47, "with"),              # μεθ’
        (48, None),                # ἑαυτῶν — "them"
    ]),
]
