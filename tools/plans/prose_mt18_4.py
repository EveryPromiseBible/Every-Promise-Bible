# -*- coding: utf-8 -*-
# Matthew 18 §4 — four fixes:
#  (a) "Then his fellow servants saw what had happened, they were greatly
#      grieved" — comma splice. Reordered to "Then, seeing what had happened,
#      his fellow servants were greatly grieved"; ἰδόντες keeps a participial
#      gloss ("seeing").
#  (b) "Then the master of him called him in" — postposed genitive. Reordered
#      to "Then his master called him in". Pure reorder.
#  (c) "Should you not you also have had mercy" — "you" doubled across οὐκ ἔδει
#      and καὶ σὲ. οὐκ ἔδει reglossed "Should not", leaving
#      "Should not you also have had mercy on your fellow servant".
#  (d) "unless you forgive each of you your brother" — Greek order. Reordered
#      to "unless each of you forgive your brother". Pure reorder.
CHAPTER = "Matthew 18"
SECTION = 4
BLOCKS = [
    (135, 142, [
        (135, "Then,"),              # οὖν
        (138, "seeing"),             # ἰδόντες
        (139, None),                 # τὰ γενόμενα — "what had happened,"
        (136, None),                 # αὐτοῦ — "his"
        (137, None),                 # οἱ σύνδουλοι — "fellow servants"
        (140, "were"),               # (supplied filler)
        (141, None),                 # ἐλυπήθησαν σφόδρα — "greatly grieved,"
    ]),
    (150, 152, [
        (151, "his"),                # αὐτοῦ
        (150, "master"),             # ὁ κύριος
    ]),
    (165, 166, [
        (165, "Should not"),         # οὐκ ἔδει
    ]),
    (192, 197, [
        (192, None),                 # ἐὰν μὴ — "unless"
        (194, None),                 # ἕκαστος — "each of you"
        (193, "forgive"),            # ἀφῆτε
        (195, None),                 # αὐτοῦ — "your"
        (196, None),                 # τῷ ἀδελφῷ — "brother"
    ]),
]
