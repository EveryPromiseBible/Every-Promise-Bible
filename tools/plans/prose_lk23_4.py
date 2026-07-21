# -*- coding: utf-8 -*-
# Luke 23 §4 — two defects in the opening description of Joseph.
#
# BLOCK 1 (3,4): "a man by name Joseph" -> "a man named Joseph".
#   ὀνόματι is the dative of respect, "by name / named"; "named" is the same
#   word in the form English actually uses. Gloss-only. (Luke 16 §2 already
#   renders the identical construction "a certain poor man, named Lazarus".)
#
# BLOCK 2 (7,11): read "being a council member, a man good and righteous—" —
#   Greek order (ἀνὴρ ἀγαθὸς καὶ δίκαιος), adjectives trailing their noun.
#   Pure reorder to "a good and righteous man—". No gloss is re-anchored;
#   only the article and the dash migrate:
#     8  ἀγαθὸς  "good"        -> "a good"
#     10 δίκαιος "righteous—"  -> "righteous"
#     7  ἀνὴρ    "a man"       -> "man—"
CHAPTER = "Luke 23"
SECTION = 4
BLOCKS = [
    (3, 4, [
        (3, "named"),   # ὀνόματι
    ]),
    (7, 11, [
        (8, "a good"),      # ἀγαθὸς
        (9, None),          # καὶ        and
        (10, "righteous"),  # δίκαιος
        (7, "man—"),        # ἀνὴρ
    ]),
]
