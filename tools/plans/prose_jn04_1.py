# -*- coding: utf-8 -*-
# John 4:24 read "and those worshiping him in spirit and truth must worship."
# That is Greek order standing in English — the reader hits "must worship" with
# nothing after it. Reordered to "and those worshiping him must worship in
# spirit and truth."
# Only two glosses change, both punctuation-only:
#   143 ἀληθείᾳ "truth" now ends the sentence, so it takes the "." and the close-quote
#   145 προσκυνεῖν "worship" no longer ends it, so it gives them up
# Every English word stays on the Greek word it was already anchored to.
CHAPTER = "John 4"
SECTION = 1
BLOCKS = [
    (136, 146, [
        (136, None),          # καὶ          — and
        (137, None),          # τοὺς         — those
        (138, None),          # προσκυνοῦντας— worshiping
        (139, None),          # αὐτὸν        — him
        (144, None),          # δεῖ          — must
        (145, "worship"),     # προσκυνεῖν   — worship
        (140, None),          # ἐν           — in
        (141, None),          # πνεύματι     — spirit
        (142, None),          # καὶ          — and
        (143, "truth.”"),     # ἀληθείᾳ      — truth
    ]),
]
