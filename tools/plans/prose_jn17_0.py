# -*- coding: utf-8 -*-
# John 17:5 read "And now glorify me, you, Father, alongside yourself" — the
# emphatic σύ and the vocative πάτερ were left trailing after the verb and its
# object, so the reader hits three commas in a row and has to reassemble it.
# Now: "And now you, Father, glorify me alongside yourself".
# One gloss edit, punctuation only:
#   74 με "me," -> "me"  (it is no longer followed by the vocative)
CHAPTER = "John 17"
SECTION = 0
BLOCKS = [
    (71, 79, [
        (71, None),        # καὶ      — And
        (72, None),        # νῦν      — now
        (75, None),        # σύ       — you,
        (76, None),        # πάτερ    — Father,
        (73, None),        # δόξασόν  — glorify
        (74, "me"),        # με
        (77, None),        # παρὰ     — alongside
        (78, None),        # σεαυτῷ   — yourself,
    ]),
]
