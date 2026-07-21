# -*- coding: utf-8 -*-
# Mark 6 §2 — four drifts, all adjacent swaps. Prose is unchanged throughout.
#
# 1) #7-8:   φανερὸν (φανερός = manifest/well known) carried "had become";
#            ἐγένετο (γίνομαι = become) carried "well known,". Swapped.
# 2) #25-26: Ἠλίας carried "“He is"; ἐστίν carried "Elijah;”". Swapped.
#            (This is the "But others said, he is 'Elijah;'" incident in
#            PROJECT.md §11 — the bad splice is still in the data.)
# 3) #35-36: Ὃν (relative pronoun "whom") carried "“John,";
#            Ἰωάννην carried "whom". Swapped.
# 4) #87-90: ἄνδρα ("man") carried only the article "a", while its noun "man,"
#            had slid onto ἅγιον ("holy"). Reordered so ἄνδρα ends the phrase
#            with "man,": "a righteous and holy man,".
CHAPTER = "Mark 6"
SECTION = 2
BLOCKS = [
    (7, 9, [
        (8, "had become"),      # ἐγένετο
        (7, "well known,"),     # φανερὸν
    ]),
    (25, 27, [
        (26, "“He is"),         # ἐστίν
        (25, "Elijah;”"),       # Ἠλίας
    ]),
    (35, 37, [
        (36, "“John,"),         # Ἰωάννην
        (35, "whom"),           # Ὃν
    ]),
    (87, 91, [
        (88, "a righteous"),    # δίκαιον
        (89, None),             # καὶ — "and"
        (90, "holy"),           # ἅγιον
        (87, "man,"),           # ἄνδρα
    ]),
]
