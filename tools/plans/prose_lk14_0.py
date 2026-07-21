# -*- coding: utf-8 -*-
# Luke 14 §0.
#
# BLOCK 1 (54,57): read "And to them he said," — Greek order (πρὸς αὐτοὺς
#   εἶπεν). Pure reorder to "And he said to them,". The comma moves from εἶπεν
#   onto the new final unit αὐτούς so the speech is still introduced.
#
# BLOCK 2 (65,66): read "…falls into a well, and will he not immediately pull
#   him out…". This καί is apodotic — it introduces the apodosis of a condition
#   and has no English word; left as "and" it makes the question read as a
#   dangling second clause. Folded (Greek still displayed, English blank), which
#   is the project's convention for untranslatable particles. Result:
#   "…falls into a well, will he not immediately pull him out on a Sabbath day?"
CHAPTER = "Luke 14"
SECTION = 0
BLOCKS = [
    (54, 57, [
        (56, "he said"),   # εἶπεν
        (54, None),        # πρὸς    to
        (55, "them,"),     # αὐτοὺς
    ]),
    (65, 66, [
        (65, ""),          # καὶ  apodotic — folded
    ]),
]
