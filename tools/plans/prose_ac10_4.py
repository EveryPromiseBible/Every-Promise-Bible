# -*- coding: utf-8 -*-
# Acts 10 §4 — two defects.
#
# 1) "And the believers of the circumcision were amazed as many as had come with
#    Peter—" — the verb sat between the subject and its own appositive clause.
#    This gives "And the believers of the circumcision, as many as had come with
#    Peter, were amazed—". Pure reorder; only the commas/dash shift to the words
#    that now open and close the appositive.
#
# 2) "“Can anyone forbid the water from being baptized— these, who received the
#    Holy Spirit just as we did?”" — as it stood, the water was the thing being
#    baptized. τοῦ μὴ βαπτισθῆναι τούτους is the articular infinitive with its
#    own accusative subject τούτους, so this gives "“Can anyone forbid the water,
#    that these should not be baptized— who received the Holy Spirit just as we
#    did?”"
#    Anchoring: τοῦ, the article that makes the infinitive a purpose/result
#    clause, is unfolded to carry "that"; μή carries "should not" (the modal is
#    what English needs for the infinitive under a verb of hindering); τούτους is
#    plain "these", now the subject it actually is; βαπτισθῆναι is "be baptized".
CHAPTER = "Acts 10"
SECTION = 4
BLOCKS = [
    (19, 28, [
        (19, None),                 # οἱ — "the"
        (20, None),                 # πιστοὶ — "believers"
        (21, None),                 # ἐκ — "of"
        (22, "the circumcision,"),  # περιτομῆς — opens the appositive
        (24, None),                 # ὅσοι — "as many as"
        (25, None),                 # συνῆλθαν — "had come with"
        (26, None),                 # τῷ — folded
        (27, "Peter,"),             # Πέτρῳ — closes the appositive
        (23, "were amazed—"),       # ἐξέστησαν
    ]),
    (50, 69, [
        (50, None),               # δύναται — "“Can"
        (51, None),               # τις — "anyone"
        (52, None),               # κωλῦσαί — "forbid"
        (53, None),               # τὸ — "the"
        (54, "water,"),           # ὕδωρ
        (55, None),               # Μήτι — folded
        (56, "that"),             # τοῦ — article of the articular infinitive
        (59, "these"),            # τούτους — subject of the infinitive
        (57, "should not"),       # μὴ
        (58, "be baptized—"),     # βαπτισθῆναι
        (60, None),               # οἵτινες — "who"
        (61, None),               # ἔλαβον — "received"
        (62, None),               # τὸ — "the"
        (63, None),               # ἅγιον — "Holy"
        (64, None),               # πνεῦμα — "Spirit"
        (65, None),               # τὸ — folded
        (66, None),               # ὡς — "just as"
        (67, None),               # καὶ — folded
        (68, None),               # ἡμεῖς — "we did?”"
    ]),
]
