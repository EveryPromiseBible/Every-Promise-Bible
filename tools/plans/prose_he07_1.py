# -*- coding: utf-8 -*-
# Hebrews 7:8 read "And here, mortal men receive tithes, but there, by one of whom it
# is testified that he lives."  The first half was turned into an active clause
# ("mortal men receive tithes") but the second half was left in the Greek's elliptical
# passive parallel ("but there, by one of whom..."), so the two halves no longer agree
# and the reader stalls on a clause with no verb and no subject.
#
# Fix uses ONLY the supplied-English filler unit 58 (greek == "", so nothing is
# anchored to Greek there) plus dropping a comma on 57. No unit is moved, no
# Greek-bearing gloss is rewritten, so anchoring is untouched:
#   57  ἐκεῖ            "there," -> "there"   (same word, comma moved)
#   58  (filler)        "by one" -> "they are received by one"
# Result: "And here, mortal men receive tithes, but there they are received by one
# of whom it is testified that he lives."
CHAPTER = "Hebrews 7"
SECTION = 1
BLOCKS = [
    (57, 59, [
        (57, "there"),                          # ἐκεῖ
        (58, "they are received by one"),       # supplied filler, no Greek
    ]),
]
