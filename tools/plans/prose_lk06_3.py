# -*- coding: utf-8 -*-
# Luke 6 §3 — two Greek-order defects. Both pure reorders.
#
# 1. (36-40) "even do not withhold the tunic" — the ascensive καί belongs with
#    "the tunic", not with the verb. -> "do not withhold even the tunic".
# 2. (105-108) "Even sinners to sinners lend," — object and verb inverted.
#    -> "Even sinners lend to sinners,". The comma moves from δανίζουσιν onto
#    ἁμαρτωλοῖς, which now ends the clause.
CHAPTER = "Luke 6"
SECTION = 3
BLOCKS = [
    (36, 41, [
        (37, None),                  # μὴ         do not
        (38, None),                  # κωλύσῃς    withhold
        (36, None),                  # καὶ        even
        (39, None),                  # τὸν        the
        (40, None),                  # χιτῶνα     tunic.
    ]),
    (105, 109, [
        (105, None),                 # καὶ          Even
        (106, None),                 # ἁμαρτωλοὶ    sinners
        (108, "lend"),               # δανίζουσιν
        (107, "to sinners,"),        # ἁμαρτωλοῖς
    ]),
]
