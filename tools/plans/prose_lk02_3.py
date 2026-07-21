# -*- coding: utf-8 -*-
# Luke 2 §3 — one defect.
# "Jesus the boy stayed behind in Jerusalem" is Greek order (Ἰησοῦς ὁ παῖς) and
# reads as two subjects jammed together. Swap the two units so it reads
# "the boy Jesus stayed behind in Jerusalem". Pure reorder, no gloss change:
# ὁ παῖς still says "the boy", Ἰησοῦς still says "Jesus".
CHAPTER = "Luke 2"
SECTION = 3
BLOCKS = [
    (51, 53, [
        (52, None),                 # ὁ παῖς   the boy
        (51, None),                 # Ἰησοῦς   Jesus
    ]),
]
