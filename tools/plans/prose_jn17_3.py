# -*- coding: utf-8 -*-
# John 17:20 read "“Not about these now do I ask only, but also about those…"
# — negation, postposed δέ and "only" are all stranded away from the verb, and
# the reader has to hold the whole clause open. Now:
# "“Now I ask not about these only, but also about those believing in me…"
# Gloss edits — each word ends up on the Greek word that actually carries it:
#   3 δὲ    "now"      -> "“Now"    (postposed δέ, now leading; takes the open-quote)
#   4 ἐρωτῶ "do I ask" -> "I ask"   (same verb, plain word order)
#   0 Οὐ    "“Not"     -> "not"     (still the negative; gives up the open-quote)
CHAPTER = "John 17"
SECTION = 3
BLOCKS = [
    (0, 6, [
        (3, "“Now"),      # δὲ
        (4, "I ask"),     # ἐρωτῶ
        (0, "not"),       # Οὐ
        (1, None),        # περὶ    — about
        (2, None),        # τούτων  — these
        (5, None),        # μόνον   — only,
    ]),
]
