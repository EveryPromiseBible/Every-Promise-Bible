# -*- coding: utf-8 -*-
# Luke 15 §3 read "but I with famine here am perishing!" — Greek order
# (ἐγὼ δὲ λιμῷ ὧδε ἀπόλλυμαι), verb stranded at the end behind two adverbials.
# Reordered to "but I am perishing here from hunger!"
#   106 ἐγὼ δὲ    "but I"          unchanged
#   109 ἀπόλλυμαι "am perishing!"  -> "am perishing"  (exclamation mark moves
#       to the new final unit; the verb itself is unchanged)
#   108 ὧδε       "here"           unchanged
#   107 λιμῷ      "with famine"    -> "from hunger!"  λιμός is both "famine"
#       and "hunger"; here it is the dative of cause describing the son's own
#       state, not the regional famine of unit 55, and "perishing from hunger"
#       is how English says it. Same word, its personal sense.
CHAPTER = "Luke 15"
SECTION = 3
BLOCKS = [
    (106, 110, [
        (106, None),            # ἐγὼ δὲ     but I
        (109, "am perishing"),  # ἀπόλλυμαι
        (108, None),            # ὧδε        here
        (107, "from hunger!"),  # λιμῷ
    ]),
]
