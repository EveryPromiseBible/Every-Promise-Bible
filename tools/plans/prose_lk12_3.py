# -*- coding: utf-8 -*-
# Luke 12 §3 — three Greek-order defects. All pure reorders; the only gloss
# edits move punctuation (and the closing quotation mark) onto whichever unit
# now ends the clause.
#
# 1. (182-183) "to eat both and to drink and to get drunk" — the correlative τε
#    landed after the first item. -> "both to eat and to drink and to get
#    drunk".
# 2. (246-248) "to everyone to whom was given much, much will be required from
#    him" — with "much" behind the verb the two "much"es collide and the clause
#    reads as gibberish. -> "to everyone to whom much was given, much will be
#    required from him".
# 3. (257-259) "more abundantly they will ask of him." -> "they will ask of him
#    more abundantly." The closing quotation mark moves onto περισσότερον.
CHAPTER = "Luke 12"
SECTION = 3
BLOCKS = [
    (182, 184, [
        (183, None),                 # τε          both
        (182, None),                 # ἐσθίειν     to eat
    ]),
    (246, 249, [
        (246, None),                 # ᾧ           to whom
        (248, "much"),               # πολύ
        (247, "was given,"),         # ἐδόθη
    ]),
    (257, 260, [
        (258, None),                 # αἰτήσουσιν    they will ask
        (259, "of him"),             # αὐτόν
        (257, "more abundantly.”"),  # περισσότερον
    ]),
]
