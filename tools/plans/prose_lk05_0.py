# -*- coding: utf-8 -*-
# Luke 5 §0 — three Greek-order defects. All pure reorders; the only gloss
# edits move punctuation onto whichever unit now ends the phrase.
#
# 1. (37-42) "he asked him from the land to put out a little" — the
#    prepositional phrase sits between the verb and its infinitive.
#    -> "he asked him to put out a little from the land".
# 2. (43-47) "and sitting down, from the boat he was teaching the crowds"
#    -> "and sitting down, he was teaching the crowds from the boat".
# 3. (69-72) "Master, through the whole night having worked hard, we took
#    nothing" -> "Master, having worked hard through the whole night, we took
#    nothing".
CHAPTER = "Luke 5"
SECTION = 0
BLOCKS = [
    (37, 43, [
        (37, None),                  # ἠρώτησεν     he asked
        (38, None),                  # αὐτὸν        him
        (41, None),                  # ἐπαναγαγεῖν  to put out
        (42, "a little"),            # ὀλίγον
        (39, None),                  # ἀπὸ          from
        (40, "the land;"),           # τῆς γῆς
    ]),
    (43, 48, [
        (43, None),                  # καθίσας δὲ   and sitting down,
        (46, None),                  # ἐδίδασκεν    he was teaching
        (47, "the crowds"),          # τοὺς ὄχλους
        (44, None),                  # ἐκ           from
        (45, "the boat."),           # τοῦ πλοίου
    ]),
    (69, 73, [
        (72, "having worked hard"),  # κοπιάσαντες
        (69, None),                  # δι’          through
        (70, None),                  # ὅλης         the whole
        (71, "night,"),              # νυκτὸς
    ]),
]
