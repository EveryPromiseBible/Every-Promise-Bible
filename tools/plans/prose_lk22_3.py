# -*- coding: utf-8 -*-
# Luke 22 §3 read "“Judas— with a kiss the Son of Man do you hand over?”" —
# Greek order (φιλήματι τὸν υἱὸν τοῦ ἀνθρώπου παραδίδως), instrument and
# object both in front of the verb. Pure reorder to
# "“Judas— do you hand over the Son of Man with a kiss?”"
# No gloss is re-anchored; the question mark and the closing quotation mark
# travel together from παραδίδως onto φιλήματι, which is now clause-final,
# so the speech still closes.
CHAPTER = "Luke 22"
SECTION = 3
BLOCKS = [
    (24, 30, [
        (29, "do you hand over"),   # παραδίδως
        (25, None),                 # τὸν        the
        (26, None),                 # υἱὸν       Son
        (27, None),                 # τοῦ        of
        (28, None),                 # ἀνθρώπου   Man
        (24, "with a kiss?”"),      # φιλήματι
    ]),
]
