# -*- coding: utf-8 -*-
# Two Greek-order defects in Mark 14 §0.
#
# 1) Mark 14:7 read "For always the poor you have with you," — adverb and object
#    both ahead of the verb. -> "For you have the poor with you always,"
# 2) Mark 14:11 read "and promised him money to give." — the infinitive stranded
#    at the end. -> "and promised to give him money."
#
# Both are pure reorders; the only gloss edits move the comma / full stop onto
# whichever unit now ends the clause.
CHAPTER = "Mark 14"
SECTION = 0
BLOCKS = [
    (90, 95, [
        (92, None),        # ἔχετε — you have
        (91, None),        # τοὺς πτωχοὺς — the poor
        (93, None),        # μεθ’ — with
        (94, "you"),       # ἑαυτῶν — loses the comma
        (90, "always,"),   # πάντοτε — takes the comma
    ]),
    (149, 153, [
        (149, None),        # ἐπηγγείλαντο — promised
        (152, "to give"),   # δοῦναι — loses the full stop
        (150, None),        # αὐτῷ — him
        (151, "money."),    # ἀργύριον — takes the full stop
    ]),
]
