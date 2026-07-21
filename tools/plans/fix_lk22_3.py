# -*- coding: utf-8 -*-
# Luke 22:47 — the genitive absolute was mislabelled.
# WAS: Ἔτι = "While"  |  αὐτοῦ = "he was still"  |  λαλοῦντος = "speaking—"
# ἔτι is the word that means "still"; αὐτοῦ is just the pronoun.
# FIX: αὐτοῦ = "While he was" (pronoun + supplied conjunction/copula),
#      Ἔτι = "still", λαλοῦντος = "speaking—". Prose unchanged.
CHAPTER = "Luke 22"
SECTION = 3
BLOCKS = [
    (0, 3, [
        (1, "While he was"),
        (0, "still"),
        (2, None),           # λαλοῦντος = "speaking—"
    ]),
]
