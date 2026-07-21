# -*- coding: utf-8 -*-
# Acts 5 §3 (Gamaliel) had two verb-first Greek clauses standing in English:
#   "For before these days rose up Theudas"        -> "For before these days Theudas rose up"
#   "After this man rose up Judas the Galilean"    -> "After this man, Judas the Galilean rose up"
# Both are pure reorders — no gloss is rewritten, only commas move to the word
# that now ends each phrase.
CHAPTER = "Acts 5"
SECTION = 3
BLOCKS = [
    (42, 48, [
        (42, None),         # πρὸ γὰρ — "For before"
        (43, None),         # τούτων — "these"
        (44, None),         # τῶν — folded
        (45, None),         # ἡμερῶν — "days"
        (47, "Theudas"),    # Θευδᾶς — comma moves off
        (46, "rose up,"),   # ἀνέστη — now closes the clause
    ]),
    (70, 76, [
        (70, None),          # μετὰ — "After"
        (71, "this man,"),   # τοῦτον — comma closes the fronted phrase
        (73, None),          # Ἰούδας — "Judas"
        (74, None),          # ὁ — "the"
        (75, None),          # Γαλιλαῖος — "Galilean"
        (72, None),          # ἀνέστη — "rose up"
    ]),
]
