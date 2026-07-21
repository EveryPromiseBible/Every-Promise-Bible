# -*- coding: utf-8 -*-
# Acts 23 §4 — readability fix (23:35)
# The interrupted quote lost its close before "he said": rendered as
# "I will hear you he said, "when your accusers also arrive,". Close the
# first clause so it reads: "I will hear you," he said, "when your accusers
# also arrive,".  (English-only; Greek multiset unchanged.)
CHAPTER = "Acts 23"
SECTION = 4
BLOCKS = [
    (151, 152, [(151,"“I will hear you,”")]),
]
