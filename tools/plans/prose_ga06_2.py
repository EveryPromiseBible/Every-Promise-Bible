# -*- coding: utf-8 -*-
# Galatians 6:8 read "the one who sows to his own flesh from the flesh will reap
# corruption, but the one who sows to the Spirit from the Spirit will reap eternal
# life." That is Greek order (εἰς τὴν σάρκα ... ἐκ τῆς σαρκὸς θερίσει) left standing
# in English: the reader hits "flesh from the flesh" / "Spirit from the Spirit" back
# to back and has to stop and work out which phrase attaches to which verb.
#
# This moves the ἐκ-phrase to after the verb it modifies, which is where English
# puts it: "...sows to his own flesh will reap corruption from the flesh."
#
# Pure reorder. No gloss changes except the punctuation, which follows the phrase
# that now ends the clause:
#   17 φθοράν  "corruption," -> "corruption"   (comma moves off, no longer clause-final)
#   15 τῆς σαρκὸς "the flesh" -> "the flesh,"  (now clause-final, takes the comma)
#   26 ζωὴν   "life."        -> "life"         (period moves off)
#   23 τοῦ πνεύματος "the Spirit" -> "the Spirit."  (now sentence-final)
# Every gloss stays on its own Greek word: ἐκ is still "from", τῆς σαρκὸς is still
# "the flesh", θερίσει is still "will reap", φθοράν is still "corruption".
CHAPTER = "Galatians 6"
SECTION = 2
BLOCKS = [
    (14, 18, [
        (16, None),            # θερίσει     "will reap"
        (17, "corruption"),    # φθοράν      drop the comma
        (14, None),            # ἐκ          "from"
        (15, "the flesh,"),    # τῆς σαρκὸς  take the comma
    ]),
    (22, 27, [
        (24, None),            # θερίσει       "will reap"
        (25, None),            # αἰώνιον       "eternal"
        (26, "life"),          # ζωὴν          drop the period
        (22, None),            # ἐκ            "from"
        (23, "the Spirit."),   # τοῦ πνεύματος take the period
    ]),
]
