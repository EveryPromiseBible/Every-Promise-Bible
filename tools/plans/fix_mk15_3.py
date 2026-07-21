# -*- coding: utf-8 -*-
# Mark 15:33 — two hour-phrases with the noun ὥρα labelled "the" and the
# ordinal carrying "<n>th hour". Block 1 also had γενομένης ("came") labelled
# merely "when". Block 2 is the same shift on ἐνάτης. Prose unchanged.
# (The third hour-phrase at #13-14, τῇ ἐνάτῃ / ὥρᾳ, is already correct.)
CHAPTER = "Mark 15"
SECTION = 3
BLOCKS = [
    (1, 4, [
        (3, "when the sixth"),   # ἕκτης
        (2, "hour"),             # ὥρας
        (1, "came,"),            # γενομένης
    ]),
    (9, 12, [
        (9, None),               # ἕως — until
        (11, "the ninth"),       # ἐνάτης
        (10, "hour."),           # ὥρας
    ]),
]
