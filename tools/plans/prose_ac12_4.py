# -*- coding: utf-8 -*-
# Acts 12 §4 read "…interrogating the guards he ordered them led away." — with no
# comma the reader parses "the guards he ordered" as a relative clause and has to
# back up. Gloss-only change, no reorder: φύλακας -> "guards," closes the
# participial phrase.
CHAPTER = "Acts 12"
SECTION = 4
BLOCKS = [
    (24, 25, [
        (24, "guards,"),   # φύλακας
    ]),
]
