# -*- coding: utf-8 -*-
# Romans 15 §2 read: "...because of the grace God gave me from to be a minister
# of Christ Jesus..." — "gave me from to be" is not English. The cause is Greek
# order: διὰ τὴν χάριν τὴν δοθεῖσάν μοι ὑπὸ τοῦ θεοῦ. τοῦ θεοῦ was pulled
# forward to sit next to "the grace", which stranded its own preposition ὑπὸ
# ("from") behind the verb, right in front of the infinitive.
#
# Reordered within [24,31) to the English shape "the grace given to me by God":
#   τὴν δοθεῖσάν  "gave" -> "given"  (it is a passive participle, not a finite
#                                     active verb — this is strictly more honest)
#   μοι           "me"   -> "to me"  (dative)
#   ὑπὸ           "from" -> "by"     (ὑπό + genitive marks the agent)
#   τοῦ θεοῦ      "God"  -> "God,"   (comma only, closing the phrase)
# Nothing is added or dropped, and every word keeps its own sense.
CHAPTER = "Romans 15"
SECTION = 2
BLOCKS = [
    (24, 31, [
        (24, None),      # διὰ — "because of"
        (25, None),      # τὴν χάριν — "the grace"
        (27, "given"),   # τὴν δοθεῖσάν
        (28, "to me"),   # μοι
        (29, "by"),      # ὑπὸ
        (26, "God,"),    # τοῦ θεοῦ
        (30, None),      # εἰς τὸ εἶναί με — "to be"
    ]),
]
