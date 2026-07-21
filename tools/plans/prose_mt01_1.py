# -*- coding: utf-8 -*-
# Matthew 1 §1: "they will call him the name Immanuel" is ungrammatical English —
# αὐτοῦ is genitive ("his"), not accusative. No reorder needed: relabel αὐτοῦ
# "his" and τὸ ὄνομα "name", giving "they will call his name Immanuel".
CHAPTER = "Matthew 1"
SECTION = 1
BLOCKS = [
    (92, 96, [
        (92, None),      # καλέσουσιν  — they will call
        (93, "his"),     # αὐτοῦ       — his  (was "him")
        (94, "name"),    # τὸ ὄνομα    — name (was "the name")
        (95, None),      # Ἐμμανουήλ   — Immanuel'
    ]),
]
