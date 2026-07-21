# -*- coding: utf-8 -*-
# Luke 23 §0 — two defects.
#
# BLOCK 1 (68,70): read "But they kept insisting, saying that “He stirs up the
#   people…" — recitative ὅτι in front of an opening quotation mark. It marks
#   a DIRECT quotation and has no English word of its own; folded, and the
#   comma that introduces the speech moves onto λέγοντες.
#
# BLOCK 2 (320,322): read "But they were pressing on with voices loud," —
#   Greek order (φωναῖς μεγάλαις), adjective after its noun. Pure reorder to
#   "with loud voices,".
#     321 μεγάλαις "loud,"       -> "with loud"   (μεγάλαις still means "loud";
#        the "with" is the dative-case marker of the phrase φωναῖς μεγάλαις and
#        rides on whichever word leads it in English)
#     320 φωναῖς   "with voices" -> "voices,"     (φωναῖς is exactly "voices";
#        it now takes the comma)
CHAPTER = "Luke 23"
SECTION = 0
BLOCKS = [
    (68, 70, [
        (68, "saying,"),   # λέγοντες
        (69, ""),          # ὅτι  recitative — folded
    ]),
    (320, 322, [
        (321, "with loud"),   # μεγάλαις
        (320, "voices,"),     # φωναῖς
    ]),
]
