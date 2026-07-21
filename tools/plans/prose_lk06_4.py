# -*- coding: utf-8 -*-
# Luke 6 §4 — one defect.
# "“A blind man is able to guide a blind man?" reads as a statement with a
# question mark bolted on. The unit Μήτι δύναται already carries the
# interrogative particle (μήτι, expecting the answer "no"), so it can front the
# clause as "Can": -> "“Can a blind man guide a blind man? Will not both fall
# into a pit?" Reorder only; ὁδηγεῖν drops its infinitive "to" because the
# fronted modal now supplies it.
CHAPTER = "Luke 6"
SECTION = 4
BLOCKS = [
    (5, 9, [
        (6, "“Can"),                 # Μήτι δύναται
        (5, "a blind man"),          # τυφλὸς
        (7, "guide"),                # ὁδηγεῖν
        (8, None),                   # τυφλὸν      a blind man?
    ]),
]
