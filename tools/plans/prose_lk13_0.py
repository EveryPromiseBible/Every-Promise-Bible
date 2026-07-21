# -*- coding: utf-8 -*-
# Luke 13 §0.
#
# BLOCK 1 (42,45): read "all likewise you will perish." — Greek order (πάντες
#   ὁμοίως ἀπολεῖσθε). Reordered to "you all will perish likewise."
#   42 πάντες "all" -> "you all"  (πάντες IS the nominative-plural subject of
#      ἀπολεῖσθε, so carrying the "you" on it is honest; the 2pl person is
#      still also in the verb.)
#   44 ἀπολεῖσθε "you will perish." -> "will perish"  (period moves to the
#      new final unit; the "you" moved to πάντες.)
#   43 ὁμοίως "likewise" -> "likewise."  (now sentence-final, takes the stop.)
#
# BLOCK 2 (78,81): the parallel clause, same defect with ὡσαύτως.
#   "all in the same way you will perish.”" -> "you all will perish in the
#   same way.”"  Same treatment; the closing quotation mark travels with the
#   period onto the new final unit so no punctuation is lost.
#
# BLOCK 3 (134,140): read "leave it also this year," — καὶ stranded before the
#   noun phrase. Pure reorder to "leave it this year also,": the adverbial καὶ
#   ("also") moves after the phrase it modifies. Only the comma moves from
#   ἔτος to καί; no gloss is re-anchored.
CHAPTER = "Luke 13"
SECTION = 0
BLOCKS = [
    (42, 45, [
        (42, "you all"),        # πάντες
        (44, "will perish"),    # ἀπολεῖσθε
        (43, "likewise."),      # ὁμοίως
    ]),
    (78, 81, [
        (78, "you all"),                # πάντες
        (80, "will perish"),            # ἀπολεῖσθε
        (79, "in the same way.”"),      # ὡσαύτως
    ]),
    (134, 140, [
        (134, None),      # ἄφες   leave
        (135, None),      # αὐτὴν  it
        (137, None),      # τοῦτο  this
        (138, None),      # τὸ     (folded)
        (139, "year"),    # ἔτος   year   (comma moves off)
        (136, "also,"),   # καὶ    also,
    ]),
]
