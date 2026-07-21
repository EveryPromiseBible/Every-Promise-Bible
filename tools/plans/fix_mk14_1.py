# -*- coding: utf-8 -*-
# Mark 14:15 — three-way gloss shift. ἀνάγαιον (the upper room) was labelled
# "a large", μέγα ("large") was blank, ἐστρωμένον ("furnished") was labelled
# "upper room," and ἕτοιμον ("ready") carried "furnished, ready;".
# Reorder so every label sits on its own word. Prose unchanged.
CHAPTER = "Mark 14"
SECTION = 1
BLOCKS = [
    (60, 64, [
        (61, "a large"),        # μέγα
        (60, "upper room,"),    # ἀνάγαιον
        (62, "furnished,"),     # ἐστρωμένον
        (63, "ready;"),         # ἕτοιμον
    ]),
]
