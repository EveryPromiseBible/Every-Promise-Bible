# -*- coding: utf-8 -*-
# 2 Corinthians 8:3-4 read "...of their own accord, with much pleading they begged us
# for the favor..." — a comma splice: the sentence already has its main verb
# ("I can testify that they gave"), so the finite "they begged" starts a second
# independent clause with no conjunction. Greek δεόμενοι is a PARTICIPLE, so
# "begging" is both better English and the more honest gloss.
# Fix: render δεόμενοι as "begging" and move the participle phrase ahead of its
# prepositional modifier, giving "...of their own accord, begging us with much
# pleading for the favor and the fellowship of the ministry to the saints."
# Anchoring: δεόμενοι = begging, ἡμῶν = us, μετὰ = with, πολλῆς = much,
# παρακλήσεως = pleading, αὐθαίρετοι = of their own accord. All unchanged in sense.
CHAPTER = "2 Corinthians 8"
SECTION = 0
BLOCKS = [
    (26, 32, [
        (26, None),        # αὐθαίρετοι — "of their own accord,"
        (30, "begging"),   # δεόμενοι — participle, was finite "they begged"
        (31, None),        # ἡμῶν — "us"
        (27, None),        # μετὰ — "with"
        (28, None),        # πολλῆς — "much"
        (29, None),        # παρακλήσεως — "pleading"
    ]),
]
