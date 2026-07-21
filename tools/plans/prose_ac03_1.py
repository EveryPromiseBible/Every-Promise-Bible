# -*- coding: utf-8 -*-
# Acts 3 §1 read "but the Author of life you killed;" — object-first Greek order
# (τὸν δὲ ἀρχηγὸν τῆς ζωῆς ἀπεκτείνατε) standing in English. This gives
# "but you killed the Author of life;".
#
# Anchoring: the unit τὸν δὲ keeps δέ's "but" and its article folds into the noun
# unit (the convention already used elsewhere in this corpus for a bare article),
# so ἀρχηγὸν now reads "the Author"; ἀπεκτείνατε keeps exactly "you killed" and
# hands its semicolon to ζωῆς, which now ends the clause.
CHAPTER = "Acts 3"
SECTION = 1
BLOCKS = [
    (89, 94, [
        (89, "but"),          # τὸν δὲ — δέ = "but"; τὸν folds into ἀρχηγὸν below
        (93, "you killed"),   # ἀπεκτείνατε — semicolon moves off
        (90, "the Author"),   # ἀρχηγὸν — carries the folded article
        (91, None),           # τῆς — "of"
        (92, "life;"),        # ζωῆς — now ends the clause
    ]),
]
