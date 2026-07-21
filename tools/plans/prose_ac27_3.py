# -*- coding: utf-8 -*-
# Acts 27:23 read "an angel of the God whose I am and whom I serve" -- "whose I
# am" is not modern English and stops the reader dead.
#   45 οὗ   "whose" -> "to whom"   (οὗ is the genitive of possession; English
#                                   expresses it with "belong to")
#   46 εἰμι "I am"  -> "I belong"  (εἰμί + possessive genitive = "belong to")
# 48 ᾧ "whom" is left alone -- it is the dative governed by λατρεύω and already
# reads correctly.
CHAPTER = "Acts 27"
SECTION = 3
BLOCKS = [
    (45, 47, [
        (45, "to whom"),    # οὗ
        (46, "I belong"),   # εἰμι
    ]),
]
