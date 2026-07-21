# -*- coding: utf-8 -*-
# Acts 5 §0 read "Now Ananias, hearing these words, falling, he breathed his
# last" — the subject "Ananias" is already stated, so the resumptive "he" after
# two participles breaks the sentence. Dropping it gives
# "Now Ananias, hearing these words, falling, breathed his last;".
#
# No reorder; only the supplied pronoun is removed from ἐξέψυξεν, whose own sense
# ("breathed his last") is untouched.
CHAPTER = "Acts 5"
SECTION = 0
BLOCKS = [
    (89, 90, [
        (89, "breathed his last;"),   # ἐξέψυξεν
    ]),
]
