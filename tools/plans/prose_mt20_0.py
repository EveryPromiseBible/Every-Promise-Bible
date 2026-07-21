# -*- coding: utf-8 -*-
# Matthew 20 §0
#  - "received each a denarius" (x2) read in Greek order; reordered to
#    "each received a denarius". Pure reorder.
#  - "But he answered one of them, said, 'Friend..." was ungrammatical
#    (ἀποκριθεὶς + εἶπεν stacked). Reordered so εἶπεν governs the dative
#    ἑνὶ αὐτῶν: "But he in reply said to one of them, 'Friend..." —
#    ἀποκριθεὶς is a participle, so "in reply" is the honest label.
CHAPTER = "Matthew 20"
SECTION = 0
BLOCKS = [
    (111, 113, [(112, None), (111, None)]),
    (123, 125, [(124, None), (123, None)]),
    (147, 152, [(147, None), (148, "in reply"), (151, "said"),
                (149, "to one"), (150, None)]),
]
