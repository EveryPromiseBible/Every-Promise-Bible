# -*- coding: utf-8 -*-
# Luke 3 §2 — three defects.
#
# 1. (40-45) "Whose the winnowing fork is in his hand" — the previous sentence
#    ends with a full stop, so the relative οὗ is stranded and "Whose the" is
#    ungrammatical. οὗ is the genitive pronoun; render it possessively at the
#    head of the new sentence and fold the bare article τὸ, which the
#    possessive now carries. -> "His winnowing fork is in his hand".
# 2. (61-67) "Therefore with many also other exhortations he was preaching" —
#    καὶ was sitting between "many" and "other". Moved after "exhortations".
#    Pure reorder plus dropping the capital: "also" still glosses καί.
# 3. (92-93) καὶ was labelled "he" — the pronoun belongs to the 3rd-singular
#    verb κατέκλεισεν, not to the conjunction. Fold καί and let the verb carry
#    "he shut up". (Small gloss drift: clicking καί said "he".)
CHAPTER = "Luke 3"
SECTION = 2
BLOCKS = [
    (40, 46, [
        (40, "His"),                 # οὗ  (genitive pronoun)
        (41, ""),                    # τὸ  — article folded under "His"
        (42, None),                  # πτύον       winnowing fork
        (43, None),                  # ἐν          is in
        (44, None),                  # αὐτοῦ       his
        (45, None),                  # τῇ χειρὶ    hand
    ]),
    (61, 68, [
        (61, None),                  # οὖν         Therefore
        (62, None),                  # Πολλὰ μὲν   with many
        (64, None),                  # ἕτερα       other
        (65, None),                  # παρακαλῶν   exhortations
        (63, "also"),                # καὶ
        (66, None),                  # εὐηγγελίζετο he was preaching the good news to
        (67, None),                  # τὸν λαόν    the people.
    ]),
    (92, 94, [
        (92, ""),                    # καὶ — folded (was wrongly glossed "he")
        (93, "he shut up"),          # κατέκλεισεν
    ]),
]
