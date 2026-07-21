# -*- coding: utf-8 -*-
# Two defects in Mark 6 §3.
#
# 1) Mark 6:39 read "he directed them to have recline everyone group by group" —
#    "to have recline" is not English. ἀνακλῖναι here is the causative aorist
#    infinitive of ἀνακλίνω, "to make recline / to seat"; glossing it "to seat"
#    is the honest sense and needs no reordering.
#    -> "he directed them to seat everyone group by group on the green grass."
#
# 2) Mark 6:43 read "they took up of broken pieces twelve baskets full" — Greek
#    order, the partitive stranded ahead of its head noun.
#    -> "they took up twelve baskets full of broken pieces".
#    Pure reorder; the only gloss edits move the comma from "full," to the new
#    end of the phrase.
CHAPTER = "Mark 6"
SECTION = 3
BLOCKS = [
    (153, 154, [
        (153, "to seat"),   # ἀνακλῖναι
    ]),
    (202, 207, [
        (202, None),                    # ἦραν — they took up
        (204, None),                    # δώδεκα — twelve
        (205, None),                    # κοφίνων — baskets
        (206, "full"),                  # πληρώματα — loses the comma
        (203, "of broken pieces,"),     # κλάσματα — takes the comma
    ]),
]
