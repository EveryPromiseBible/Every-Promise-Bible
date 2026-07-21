# -*- coding: utf-8 -*-
# Luke 18 §0 read "so that not in the end, coming, she wears me out!’”" —
# Greek order (ἵνα μὴ εἰς τέλος ἐρχομένη ὑπωπιάζῃ με), with the negative
# stranded in front of a prepositional phrase and a bare participle wedged
# before the verb. Reordered to:
#   "so that she may not in the end wear me out by coming!’”"
#   70 μὴ        "not"        -> "she may not"  (the English subjunctive
#      auxiliary rides on the negative, the house pattern already used at
#      unit 89 "οὐ μὴ / not certainly")
#   72 τέλος     "the end,"   -> "the end"      (comma no longer needed)
#   74 ὑπωπιάζῃ  "she wears me out!’”" -> "wear me out"  (same verb; subject
#      and closing punctuation move off it)
#   73 ἐρχομένη  "coming,"    -> "by coming!’”"  (same participle, now the
#      instrumental phrase English wants; carries the exclamation mark and
#      BOTH closing quotation marks so the judge's speech and the parable
#      still close)
#   75 με stays folded, as it already is — "wear me out" keeps it covered.
CHAPTER = "Luke 18"
SECTION = 0
BLOCKS = [
    (69, 76, [
        (69, None),                # ἵνα        so that
        (70, "she may not"),       # μὴ
        (71, None),                # εἰς        in
        (72, "the end"),           # τέλος
        (74, "wear me out"),       # ὑπωπιάζῃ
        (75, None),                # με         (folded)
        (73, "by coming!’”"),      # ἐρχομένη
    ]),
]
