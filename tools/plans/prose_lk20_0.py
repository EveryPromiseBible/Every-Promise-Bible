# -*- coding: utf-8 -*-
# Luke 20 §0 — two defects.
#
# BLOCK 1 (45,47): read "Answering now, he said to them," — postposed δέ
#   stranded after the participle. Pure reorder to "Now answering, he said to
#   them,", which is how every other narrative δέ in this chapter reads.
#   Only capitalisation and the comma migrate:
#     46 δὲ          "now,"      -> "Now"
#     45 ἀποκριθεὶς  "Answering" -> "answering,"
#
# BLOCK 2 (70,72): read "saying that “If we say, ‘From heaven,’…" — recitative
#   ὅτι in front of an opening quotation mark. It marks a DIRECT quotation and
#   has no English word of its own; folded, and the comma that introduces the
#   speech moves onto λέγοντες.
CHAPTER = "Luke 20"
SECTION = 0
BLOCKS = [
    (45, 47, [
        (46, "Now"),           # δὲ
        (45, "answering,"),    # ἀποκριθεὶς
    ]),
    (70, 72, [
        (70, "saying,"),   # λέγοντες
        (71, ""),          # ὅτι  recitative — folded
    ]),
]
