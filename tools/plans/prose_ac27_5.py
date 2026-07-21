# -*- coding: utf-8 -*-
# Acts 27:41 read "they ran aground the vessel" -- "run aground" is intransitive
# in English, so it cannot take "the vessel" as an object; the reader stumbles.
# ἐπικέλλω is transitive, "to drive/ground a ship", and "grounded" carries it
# exactly in one word, keeping the whole verb on its own Greek unit rather than
# splitting a phrasal verb across ἐπέκειλαν and τὴν ναῦν.
# 40 ἐπέκειλαν "they ran aground" -> "they grounded"
CHAPTER = "Acts 27"
SECTION = 5
BLOCKS = [
    (40, 41, [
        (40, "they grounded"),   # ἐπέκειλαν
    ]),
]
