# -*- coding: utf-8 -*-
# Two fixes in Luke 1 §1.
#
# 1) Luke 1:5 - SEVERE pre-existing gloss drift (found while triaging the blank
#    at #91). Glosses belonging to the 1:12 sentence had been pasted onto the
#    1:5 units, and the prose was broken too:
#      "a certain priest And Zechariah was troubled when he saw him, of Abijah;"
#    ONOMATI="And", EX="was troubled", EPHEMERIAS="when he saw him,".
#    Re-glossed to "named / of / the division". Pure re-gloss, no reorder.
#
# 2) Luke 1:12 - "was troubled" had drifted onto the participle IDWN ("seeing");
#    ETARACHTHE (the actual verb "was troubled") was left blank.
CHAPTER = "Luke 1"
SECTION = 1
BLOCKS = [
    (8, 13, [(8, "named"), (9, "Zechariah,"), (10, "of"),
             (11, "the division"), (12, None)]),
    (90, 92, [(90, "seeing him,"), (91, "was troubled")]),
]
