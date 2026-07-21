# -*- coding: utf-8 -*-
# Acts 21 §4 — readability fix (21:39)
# "I am a man a Jew, of Tarsus" -> "I am a Jewish man, of Tarsus" (matches
# the parallel wording at 22:3).  (English-only; Greek multiset unchanged.)
CHAPTER = "Acts 21"
SECTION = 4
BLOCKS = [
    (40, 42, [(41,"a Jewish"),(40,"man,")]),
]
