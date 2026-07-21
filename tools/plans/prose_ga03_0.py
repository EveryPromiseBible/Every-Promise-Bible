# -*- coding: utf-8 -*-
# Galatians 3:4 renders "Did you suffer so many things in vain —if indeed it really
# was in vain?" The em dash is carried as a prefix on unit 37 (εἴ), so the joiner
# puts a space BEFORE the dash and none after — " —if" — which reads as a typo.
# Everywhere else in Galatians the convention is a spaced em dash ("Paul, an apostle
# — not from men", "privately, though, before those recognized as leaders —").
#
# Pure gloss rewrite, no reordering. The dash moves from the front of εἴ to the end
# of εἰκῇ; it is punctuation, not a gloss, so nothing about the anchoring changes:
#   36 εἰκῇ "in vain" -> "in vain —"   (still glosses εἰκῇ, "in vain")
#   37 εἴ   "—if"     -> "if"          (still glosses εἴ, "if")
CHAPTER = "Galatians 3"
SECTION = 0
BLOCKS = [
    (36, 38, [
        (36, "in vain —"),   # εἰκῇ
        (37, "if"),          # εἴ
    ]),
]
