# -*- coding: utf-8 -*-
# 1 Corinthians 9:22 read "I became to the weak weak," -- Greek order, and the
# stutter is what a duplicated-adjacent-word scan flagged. The parallel clause
# five units later already has the right shape ("To all I have become all
# things"), so this matches it:
#     "To the weak I became weak, so that I might win the weak."
# Pure reorder -- the only gloss change is capitalising "to" as the sentence now
# opens on that unit.
CHAPTER = "1 Corinthians 9"
SECTION = 3
BLOCKS = [
    (45, 48, [
        (46, "To the weak"),   # τοῖς ἀσθενέσιν
        (45, None),            # ἐγενόμην -> "I became"
        (47, None),            # ἀσθενής  -> "weak,"
    ]),
]
