# -*- coding: utf-8 -*-
# Mark 15:4 read "Look how many things against you they accuse!" — Greek order,
# verb last.
# This gives "Look how many things they accuse you of!"
# Reorder plus one gloss change: σου "against you" -> "you of". σου is the
# genitive of the person accused that κατηγορέω governs; "you of" renders that
# same genitive in the English construction, and no other word moves onto it.
CHAPTER = "Mark 15"
SECTION = 0
BLOCKS = [
    (48, 51, [
        (48, None),             # πόσα — how many things
        (50, "they accuse"),    # κατηγοροῦσιν — loses the "!”"
        (49, "you of!”"),       # σου — takes the "!”"
    ]),
]
