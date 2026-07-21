# -*- coding: utf-8 -*-
# Matthew 6 §1: the Lord's Prayer closes its quotation early — "...our debtors.'
# And lead us not into temptation..." — leaving the last petition outside the
# prayer, then closing again at "the evil one.'" Drop the stray closing quote.
# Punctuation only; no reorder, no gloss change.
CHAPTER = "Matthew 6"
SECTION = 1
BLOCKS = [
    (106, 107, [(106, "debtors.")]),   # τοῖς ὀφειλέταις (was "debtors.'")
]
