# -*- coding: utf-8 -*-
# Luke 15 §1.
#
# BLOCK 1 (1,3): read "“What person of you, having a hundred sheep…".
#   1 ἄνθρωπος "person" -> "man"   (same word; "what person of you" is not
#     English, "what man among you" is the natural form of the idiom)
#   2 ἐξ "of" -> "among"           (partitive ἐκ after an interrogative; still
#     the preposition ἐκ, just the English partitive that goes with "what man")
#   No reordering.
#
# BLOCK 2 (63,64): read "there will be joy in heaven over one sinner who
#   repents THAN over ninety nine righteous ones" — "than" with no comparative
#   in front of it, which is ungrammatical and stops the reader dead. Greek
#   expresses the comparison with ἤ plus a positive noun (χαρὰ … ἢ …), so the
#   comparative degree belongs to the noun phrase in English.
#   63 χαρὰ "joy" -> "more joy".  ἢ (unit 71) keeps "than" untouched.
#   Gives "there will be more joy in heaven over one sinner who repents than
#   over ninety nine righteous ones…". Gloss-only; nothing reordered.
CHAPTER = "Luke 15"
SECTION = 1
BLOCKS = [
    (1, 3, [
        (1, "man"),      # ἄνθρωπος
        (2, "among"),    # ἐξ
    ]),
    (63, 64, [
        (63, "more joy"),   # χαρὰ
    ]),
]
