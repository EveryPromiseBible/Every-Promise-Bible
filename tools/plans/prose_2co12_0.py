# -*- coding: utf-8 -*-
# 2 Corinthians 12:3-4 read "And I know THAT such a man — ... — THAT he was caught
# up into paradise": a doubled "that" with no main clause between them, so the
# sentence loses its footing. The real ὅτι is unit 52, already glossed "that".
# Fix: trim unit 40 (τὸν τοιοῦτον) from "that such" back to "such".
# Anchoring: τὸν τοιοῦτον = "such (one)" — the stray "that" never belonged to it;
# it duplicated ὅτι. No reorder, no other change.
CHAPTER = "2 Corinthians 12"
SECTION = 0
BLOCKS = [
    (40, 41, [
        (40, "such"),   # τὸν τοιοῦτον
    ]),
]
