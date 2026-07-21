# -*- coding: utf-8 -*-
# 1 Corinthians 9:7 read "Who serves as a soldier at his own expense ever?"
# ποτέ is left in Greek final position, where English strands it after the
# prepositional phrase and the question lands wrong. Pure reorder to the normal
# English adverb slot, with the question mark moving to the new final unit:
#   4 ποτέ     "ever?"   -> "ever"
#   3 ὀψωνίοις "expense" -> "expense?"
# Gives: "Who ever serves as a soldier at his own expense?"
CHAPTER = "1 Corinthians 9"
SECTION = 1
BLOCKS = [
    (0, 5, [
        (0, None),          # τίς — "Who"
        (4, "ever"),        # ποτέ
        (1, None),          # στρατεύεται — "serves as a soldier"
        (2, None),          # ἰδίοις — "at his own"
        (3, "expense?"),    # ὀψωνίοις
    ]),
]
