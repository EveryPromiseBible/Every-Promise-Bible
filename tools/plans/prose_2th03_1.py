# -*- coding: utf-8 -*-
# 2 Thessalonians 3:4 read "...that you are doing and will do both what we command."
# The correlative καί ("both") was left standing in Greek position, stranded at the
# end of the clause where an English reader parses it as a quantifier over two
# things that never arrive. Greek: ὅτι ἃ παραγγέλλομεν καὶ ποιεῖτε καὶ ποιήσετε.
#
# This is a PURE REORDER — no gloss is rewritten, so no gloss can drift. Unit 21
# (καί, "both") is moved to the front of the pair it correlates, giving:
#   "...that both you are doing and will do what we command."
# Anchoring: 21 καί = "both" and 19 καί = "and" together render the καί…καί
# correlative, which is precisely "both … and". 18 ποιεῖτε keeps "you are doing",
# 20 ποιήσετε keeps "will do", 22 ἃ keeps "what", 23 παραγγέλλομεν keeps
# "we command." with its full stop intact.
CHAPTER = "2 Thessalonians 3"
SECTION = 1
BLOCKS = [
    (17, 24, [
        (17, None),   # ὅτι          — "that"
        (21, None),   # καί          — "both"
        (18, None),   # ποιεῖτε      — "you are doing"
        (19, None),   # καί          — "and"
        (20, None),   # ποιήσετε     — "will do"
        (22, None),   # ἃ            — "what"
        (23, None),   # παραγγέλλομεν— "we command."
    ]),
]
