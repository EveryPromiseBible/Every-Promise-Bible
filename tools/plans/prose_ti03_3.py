# -*- coding: utf-8 -*-
# Titus 3:12 read "When I send Artemas to you or Tychicus, ..." — Greek order
# (Ἀρτεμᾶν πρὸς σὲ ἢ Τυχικόν) left standing, which strands "or Tychicus" after
# the prepositional phrase. This gives "When I send Artemas or Tychicus to you, ...".
# Pure reorder: Ἀρτεμᾶν="Artemas", ἢ="or", Τυχικόν="Tychicus", πρὸς="to", σὲ="you".
# Only punctuation moves: the comma travels from Τυχικόν (no longer clause-final)
# to σὲ (now clause-final). Every anchor is unchanged.
CHAPTER = "Titus 3"
SECTION = 3
BLOCKS = [
    (2, 7, [
        (2, None),        # Ἀρτεμᾶν   — Artemas
        (5, None),        # ἢ         — or
        (6, "Tychicus"),  # Τυχικόν   — was "Tychicus," ; comma moves off
        (3, None),        # πρὸς      — to
        (4, "you,"),      # σὲ        — was "you" ; now ends the clause
    ]),
]
