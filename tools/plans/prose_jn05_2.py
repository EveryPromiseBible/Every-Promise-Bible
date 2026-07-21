# -*- coding: utf-8 -*-
# Two sentences in John 5 §2 keep Greek order in English.
#
# BLOCK 1 — John 5:39 read "because you think in them to have eternal life".
#   Now "because you think to have eternal life in them". Pure reorder; the only
#   gloss edits are the em-dash moving from ζωὴν ("life") to αὐταῖς ("them"),
#   since "them" now ends the clause.
#
# BLOCK 2 — John 5:42 read "that the love of God you do not have in yourselves".
#   Now "that you do not have the love of God in yourselves". This is a pure
#   reorder: not one gloss changes, and ἑαυτοῖς still ends the sentence so it
#   keeps its full stop.
CHAPTER = "John 5"
SECTION = 2
BLOCKS = [
    (133, 141, [
        (133, None),        # ὅτι      — because
        (134, None),        # ὑμεῖς    — you
        (135, None),        # δοκεῖτε  — think
        (138, None),        # ἔχειν    — to have
        (139, None),        # αἰώνιον  — eternal
        (140, "life"),      # ζωὴν     — life
        (136, None),        # ἐν       — in
        (137, "them—"),     # αὐταῖς   — them
    ]),
    (166, 174, [
        (170, None),        # οὐκ      — you do not
        (171, None),        # ἔχετε    — have
        (166, None),        # τὴν      — the
        (167, None),        # ἀγάπην   — love
        (168, None),        # τοῦ      — of
        (169, None),        # θεοῦ     — God
        (172, None),        # ἐν       — in
        (173, None),        # ἑαυτοῖς  — yourselves.
    ]),
]
