# -*- coding: utf-8 -*-
# Matthew 19 §0:
#  (a) "…came to him to test him, and asking, “Is it lawful…" — dangling
#      participle. λέγοντες reglossed "asked," to match the finite main verb.
#  (b) "Moses because of your hardness of heart permitted you to divorce your
#      wives" — Greek order, subject split from its verb. Reordered to
#      "Because of your hardness of heart Moses permitted you to divorce your
#      wives". Pure reorder; the opening quotation mark travels to the new
#      first unit so the speech still opens.
CHAPTER = "Matthew 19"
SECTION = 0
BLOCKS = [
    (32, 33, [
        (32, "asked,"),               # λέγοντες
    ]),
    (99, 108, [
        (100, "“Because of"),         # πρὸς
        (101, None),                  # ὑμῶν — "your"
        (102, None),                  # τὴν σκληροκαρδίαν — "hardness of heart"
        (99, "Moses"),                # ὅτι Μωϋσῆς
        (103, None),                  # ἐπέτρεψεν — "permitted"
        (104, None),                  # ὑμῖν — "you"
        (105, None),                  # ἀπολῦσαι — "to divorce"
        (106, None),                  # ὑμῶν — "your"
        (107, None),                  # τὰς γυναῖκας — "wives,"
    ]),
]
