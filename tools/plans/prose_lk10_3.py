# -*- coding: utf-8 -*-
# Luke 10 §3 — one defect.
# "but of few things there is need— or of one." — the fronted genitive leaves
# an awkward existential. Recast in place with no reordering at all, so every
# gloss stays on its own word: "but few things are needed— or one."
# ὀλίγων δέ -> "but few things", ἐστιν -> "are", χρεία -> "needed—",
# ἑνός -> "one." (the genitives are what the recast absorbs).
CHAPTER = "Luke 10"
SECTION = 3
BLOCKS = [
    (67, 72, [
        (67, "but few things"),      # ὀλίγων δέ
        (68, "are"),                 # ἐστιν
        (69, "needed—"),             # χρεία
        (70, None),                  # ἢ      or
        (71, "one."),                # ἑνός
    ]),
]
