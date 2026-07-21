# -*- coding: utf-8 -*-
# Mark 2:11 read "To you I say, get up" which is Greek order (Σοὶ λέγω).
# This gives "I say to you, get up".
# Pure reorder of two units plus punctuation/quote-mark carriage:
#   136 λέγω  "I say"   -> takes the opening quotation mark: "“I say"
#   135 Σοὶ   "To you"  -> loses the quotation mark and lowercases: "to you,"
# Both glosses still describe exactly their own Greek word.
CHAPTER = "Mark 2"
SECTION = 0
BLOCKS = [
    (135, 137, [
        (136, "“I say"),   # λέγω
        (135, "to you,"),       # Σοὶ
    ]),
]
