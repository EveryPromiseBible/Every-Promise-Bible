# -*- coding: utf-8 -*-
# Romans 10 §1, three defects.
#
# (1)+(2) Capitalisation broken mid-sentence. Both τοῦτ’ ἔστιν parentheses read
#     "— That is,". The capital fired off the question mark inside the preceding
#     quotation ("...into heaven?”'"), which is exactly the Matthew 5:22 failure.
#     Lowercased to "— that is,". Gloss unchanged otherwise.
#
# (3) "'The word is near you — is in your mouth and in your heart.'" The stray
#     "— is" is ἐστιν stranded in Greek position (Ἐγγύς σου τὸ ῥῆμά ἐστιν),
#     after Ἐγγύς had already absorbed the copula as "is near". Reordered so the
#     copula sits where English wants it and each word carries its own sense:
#     ἐστιν = "is", Ἐγγύς = "near", σου = "you,". Nothing is added or dropped;
#     the em dash that was doing duty as a stopgap becomes the comma the
#     apposition actually needs.
CHAPTER = "Romans 10"
SECTION = 1
BLOCKS = [
    (23, 24, [
        (23, "— that is,"),   # τοῦτ’ ἔστιν
    ]),
    (31, 32, [
        (31, "— that is,"),   # τοῦτ’ ἔστιν
    ]),
    (40, 44, [
        (40, None),      # τὸ ῥῆμά — "'The word"
        (43, "is"),      # ἐστιν
        (41, "near"),    # Ἐγγύς
        (42, "you,"),    # σου
    ]),
]
