# -*- coding: utf-8 -*-
# Acts 3 §2 read:
#   "But God— what he foretold through the mouth of all the prophets, his Christ
#    would suffer— he fulfilled in this way."
# The main verb sat at the very end, in Greek order, with the object clause
# stacked in front of it — a reader has to hold the whole sentence open. This
# gives:
#   "But God fulfilled in this way what he foretold through the mouth of all the
#    prophets— his Christ would suffer."
#
# Anchoring: ἐπλήρωσεν loses only its supplied pronoun ("he fulfilled" ->
# "fulfilled") because θεὸς is now the immediately preceding subject; θεὸς drops
# its em-dash; προφητῶν takes the em-dash that now opens the appositive; παθεῖν
# takes the closing full stop. Every other gloss is untouched; the article τὸν
# stays folded and moves to sit before its noun phrase.
CHAPTER = "Acts 3"
SECTION = 2
BLOCKS = [
    (13, 28, [
        (13, None),             # ὁ δὲ — "But"
        (14, "God"),            # θεὸς — em-dash removed
        (26, "fulfilled"),      # ἐπλήρωσεν — subject now adjacent
        (27, "in this way"),    # οὕτως — full stop moves off
        (15, None),             # ἃ — "what"
        (16, None),             # προκατήγγειλεν — "he foretold"
        (17, None),             # διὰ — "through"
        (18, None),             # στόματος — "the mouth"
        (19, None),             # πάντων — "of all"
        (20, None),             # τῶν — "the"
        (21, "prophets—"),      # προφητῶν — opens the appositive
        (24, None),             # τὸν — folded article of χριστὸν
        (22, None),             # αὐτοῦ — "his"
        (23, None),             # χριστὸν — "Christ"
        (25, "would suffer."),  # παθεῖν — now ends the sentence
    ]),
]
