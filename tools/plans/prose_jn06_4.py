# -*- coding: utf-8 -*-
# John 6:66 read "many of his disciples went away to the things behind" — a
# word-for-word rendering of the idiom ἀπῆλθον εἰς τὰ ὀπίσω, which stops the
# reader cold. English for that idiom is "went back".
# No units move. Three glosses change:
#   118 ἀπῆλθον "went away" -> "went"  (still the verb of departure)
#   119 εἰς     -> folded            (the preposition has no separate English
#   120 τὰ      -> folded             inside the idiom; folding an article or
#                                     preposition is the established convention)
#   121 ὀπίσω   "behind," -> "back,"  (ὀπίσω is exactly "back/behind")
# The Greek multiset is untouched and every remaining English word sits on the
# Greek word that carries it.
CHAPTER = "John 6"
SECTION = 4
BLOCKS = [
    (118, 122, [
        (118, "went"),      # ἀπῆλθον
        (119, ""),          # εἰς
        (120, ""),          # τὰ
        (121, "back,"),     # ὀπίσω
    ]),
]
