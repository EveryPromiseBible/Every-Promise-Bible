# -*- coding: utf-8 -*-
# John 7:37 read "Now on the last day, the great one, of the feast, Jesus stood"
# — the appositive is wedged between "day" and "of the feast", so the reader
# loses the head noun. Reordered to "Now on the last day of the feast— the
# great one— Jesus stood", which keeps the same apposition but lets the noun
# phrase finish first.
# The only gloss edits are punctuation moving with the words:
#   98  ἡμέρᾳ  "day,"       -> "day"        (no longer before a break)
#   102 ἑορτῆς "feast,"     -> "feast—"     (now opens the apposition)
#   100 μεγάλῃ "great one," -> "great one—" (now closes it)
CHAPTER = "John 7"
SECTION = 2
BLOCKS = [
    (95, 103, [
        (95, None),             # Ἐν      — on
        (96, None),             # τῇ      — the
        (97, None),             # ἐσχάτῃ  — last
        (98, "day"),            # ἡμέρᾳ   — day
        (101, None),            # τῆς     — of the
        (102, "feast—"),        # ἑορτῆς  — feast
        (99, None),             # τῇ      — the
        (100, "great one—"),    # μεγάλῃ  — great one
    ]),
]
