# -*- coding: utf-8 -*-
# John 4:24 -- gloss drift, not a prose defect. The English is correct and
# doctrinally right ("God is spirit", already repaired once from the modalist
# "Spirit is God"), but the labels underneath are wrong:
#
#     134  ὁ  "is"
#
# ὁ is the article belonging to θεός. It is not a copula. πνεῦμα ὁ θεός is
# VERBLESS in Greek, so English's "is" is supplied and has no Greek word to sit
# on -- it had been parked on the article, so clicking ὁ reports "is".
#
# The corpus convention for both halves of this is already settled elsewhere:
#   1 John 4:8/16  ὁ θεὸς='God'  ἐστίν='is'  ἀγάπη='love'
#   1 John 1:5     ὁ θεὸς='God'  ἐστιν='is'  φῶς='light'
# -- the article folds into the noun, and "is" rides on the copula. Here there
# is no copula to ride on, so the supplied "is" attaches to the subject noun and
# the article folds, which is what the ὁ θεὸς unit does in 1 John anyway.
#
#   133 θεός   "God"   -> "God is"   (subject + the supplied copula)
#   134 ὁ      "is"    -> ""         (folded; it is θεός's article)
#   135 πνεῦμα "spirit," unchanged
#
# Subject and predicate are untouched: θεός keeps the articular subject and
# πνεῦμα keeps the anarthrous predicate, so the terms stay non-convertible.
# The visible prose is BYTE-IDENTICAL before and after.
CHAPTER = "John 4"
SECTION = 1
BLOCKS = [
    (133, 136, [
        (133, "God is"),   # θεός + its supplied copula
        (134, ""),         # ὁ — folded article
        (135, None),       # πνεῦμα -> "spirit,"
    ]),
]
