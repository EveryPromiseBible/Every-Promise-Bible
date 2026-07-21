# -*- coding: utf-8 -*-
# Acts 23:13-14 read "...more than forty who made this plot. Who went to the
# chief priests..." -- a full stop strands the relative pronoun οἵτινες as a
# sentence fragment. Comma, not full stop.
# 21 τὴν συνωμοσίαν "plot." -> "plot,"  (noun unchanged, punctuation only)
# 22 οἵτινες        "Who"   -> "who"    (same relative pronoun, decapitalised)
CHAPTER = "Acts 23"
SECTION = 3
BLOCKS = [
    (21, 23, [
        (21, "plot,"),   # τὴν συνωμοσίαν
        (22, "who"),     # οἵτινες
    ]),
]
