# -*- coding: utf-8 -*-
# Mark 5:26 read "but rather for the worse having come" — Greek order, with the
# participle stranded after its prepositional phrase.
# This gives "but rather having come to the worse".
# Reorder plus one gloss change: εἰς "for" -> "to", which is the ordinary sense
# of εἰς and the one this construction requires in English. Every other word
# stays on its own Greek.
CHAPTER = "Mark 5"
SECTION = 1
BLOCKS = [
    (79, 85, [
        (79, None),   # ἀλλὰ — but
        (80, None),   # μᾶλλον — rather
        (84, "having come"),   # ἐλθοῦσα — drops the trailing comma
        (81, "to"),            # εἰς
        (82, None),            # τὸ — the
        (83, "worse,"),        # χεῖρον — takes the comma that ends the clause
    ]),
]
