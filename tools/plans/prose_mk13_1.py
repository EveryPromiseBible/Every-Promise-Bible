# -*- coding: utf-8 -*-
# Two object-before-verb defects in Mark 13 §1.
#
# 1) Mark 13:6 read "and many they will deceive." -> "and they will deceive many."
# 2) Mark 13:11 read "in that hour, this say;" -> "in that hour, say this;"
#
# Both are pure reorders; the only gloss edits move the sentence punctuation
# onto whichever unit now comes last.
CHAPTER = "Mark 13"
SECTION = 1
BLOCKS = [
    (19, 21, [
        (20, "they will deceive"),   # πλανήσουσιν — loses the full stop
        (19, "many."),               # πολλοὺς — takes the full stop
    ]),
    (99, 101, [
        (100, "say"),      # λαλεῖτε — loses the semicolon
        (99,  "this;"),    # τοῦτο — takes the semicolon
    ]),
]
