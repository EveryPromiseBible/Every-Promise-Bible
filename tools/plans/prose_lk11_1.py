# -*- coding: utf-8 -*-
# Luke 11 §1 — two defects.
#
# 1. (60-64) "how his kingdom will stand?" — a question with statement word
#    order. English forms this question by subject-auxiliary inversion, and the
#    auxiliary attaches to the interrogative: πῶς -> "how will", σταθήσεται ->
#    "stand?". -> "how will his kingdom stand?"
# 2. (73-77) "But if I by Beelzebul cast out the demons" — the subject sits
#    between "if" and the fronted prepositional phrase. Reordered to "But if by
#    Beelzebul I cast out the demons", which also matches the parallel clause
#    three sentences later ("But if by the finger of God I cast out the
#    demons"). Pure reorder.
CHAPTER = "Luke 11"
SECTION = 1
BLOCKS = [
    (60, 65, [
        (60, "how will"),            # πῶς
        (61, None),                  # αὐτοῦ        his
        (62, None),                  # βασιλεία     kingdom
        (63, None),                  # ἡ            (folded)
        (64, "stand?"),              # σταθήσεται
    ]),
    (73, 78, [
        (73, None),                  # εἰ δὲ        But if
        (75, None),                  # ἐν           by
        (76, None),                  # Βεελζεβοὺλ   Beelzebul
        (74, None),                  # ἐγὼ          I
        (77, None),                  # ἐκβάλλω      cast out
    ]),
]
