# -*- coding: utf-8 -*-
# Luke 17 §0 — two defects.
#
# BLOCK 1 (133,140): read "and after these things you will eat and drink, you’?"
#   — the emphatic σύ left stranded after the verbs in Greek order, which
#   reads as a dangling repetition. Reordered to "and after these things you
#   yourself will eat and drink’?"
#     139 σύ      "you’?"        -> "you yourself"  (σύ here is the emphatic
#         nominative pronoun contrasting the servant with the master; "you
#         yourself" is exactly that word's force)
#     136 φάγεσαι "you will eat" -> "will eat"      (the subject now sits on σύ)
#     138 πίεσαι  "drink,"       -> "drink’?"       (carries the closing single
#         quotation mark and the question mark that σύ used to hold, so no
#         punctuation is lost)
#
# BLOCK 2 (158,160): read "say that ‘We are unworthy servants…". Recitative
#   ὅτι marks a DIRECT quotation and has no English word; "that" in front of
#   an opening quotation mark is a reader stumble. Folded, and the comma that
#   introduces the speech moves onto λέγετε.
CHAPTER = "Luke 17"
SECTION = 0
BLOCKS = [
    (133, 140, [
        (133, None),            # καὶ      and
        (134, None),            # μετὰ     after
        (135, None),            # ταῦτα    these things
        (139, "you yourself"),  # σύ
        (136, "will eat"),      # φάγεσαι
        (137, None),            # καὶ      and
        (138, "drink’?"),       # πίεσαι
    ]),
    (158, 160, [
        (158, "say,"),   # λέγετε
        (159, ""),       # ὅτι  recitative — folded
    ]),
]
