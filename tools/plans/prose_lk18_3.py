# -*- coding: utf-8 -*-
# Luke 18 §3 read "The commandments you know: ‘Do not commit adultery…" —
# Greek order (τὰς ἐντολὰς οἶδας), object before verb. Pure reorder to
# "You know the commandments: ‘Do not commit adultery…". No gloss is
# re-anchored: οἶδας keeps "know", ἐντολὰς keeps "commandments", τὰς keeps
# "the". Only the sentence capital and the colon migrate with them.
CHAPTER = "Luke 18"
SECTION = 3
BLOCKS = [
    (28, 31, [
        (30, "You know"),        # οἶδας
        (28, "the"),             # τὰς
        (29, "commandments:"),   # ἐντολὰς
    ]),
]
