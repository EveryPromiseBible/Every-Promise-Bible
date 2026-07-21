# -*- coding: utf-8 -*-
# Luke 24 §2 — two defects.
#
# BLOCK 1 (91,94): read "and taking it, before them he ate." — Greek order
#   (ἐνώπιον αὐτῶν ἔφαγεν), the prepositional phrase in front of the verb.
#   Pure reorder to "and taking it, he ate before them." Only the full stop
#   moves, from ἔφαγεν onto αὐτῶν.
#
# BLOCK 2 (137,139): read "And he said to them that “Thus it is written:…" —
#   recitative ὅτι in front of an opening quotation mark. It marks a DIRECT
#   quotation and has no English word of its own; folded, and the comma that
#   introduces the speech moves onto αὐτοῖς.
CHAPTER = "Luke 24"
SECTION = 2
BLOCKS = [
    (91, 94, [
        (93, "he ate"),   # ἔφαγεν
        (91, None),       # ἐνώπιον  before
        (92, "them."),    # αὐτῶν
    ]),
    (137, 139, [
        (137, "to them,"),   # αὐτοῖς
        (138, ""),           # ὅτι  recitative — folded
    ]),
]
