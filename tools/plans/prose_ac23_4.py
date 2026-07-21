# -*- coding: utf-8 -*-
# Acts 23:29 read "...I brought him down to their council. Whom I found accused
# about questions of their law..." -- a full stop strands the relative pronoun
# ὃν as a fragment. Here a comma would misread (the nearest antecedent is
# "council"), so the connective relative is taken as what it is: ὃν is
# accusative masculine singular pointing back at Paul, the standard connective
# use, honestly rendered "him". Swapping it behind the verb gives a complete
# sentence with no word added.
#   72 εὗρον "I found" moves first (gloss unchanged)
#   71 ὃν    "Whom" -> "him"
CHAPTER = "Acts 23"
SECTION = 4
BLOCKS = [
    (71, 73, [
        (72, "I found"),   # εὗρον
        (71, "him"),       # ὃν
    ]),
]
