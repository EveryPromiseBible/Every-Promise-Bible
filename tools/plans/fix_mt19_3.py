# -*- coding: utf-8 -*-
# Matthew 19:24 — stranded preposition + a duplicated gloss.
# Greek: εὐκοπώτερόν ἐστιν κάμηλον διὰ τρυπήματος ῥαφίδος εἰσελθεῖν ἢ πλούσιον
#        εἰς τὴν βασιλείαν τοῦ θεοῦ
# Before, δια sat AFTER ἢ, producing the broken clause
#   "... than through for a rich person into the kingdom of God"
# and εἰσελθεῖν carried "to go through", duplicating δια's own sense.
# Fix: pure reorder — δια moves in front of τρυπήματος where the English needs
# it, and εἰσελθεῖν's gloss is trimmed to "to go" (still honest: εἰσέρχομαι).
# Prose after:
#   "... it is easier for a camel to go through the eye of a needle than for a
#    rich person into the kingdom of God."
CHAPTER = "Matthew 19"
SECTION = 3
BLOCKS = [
    (19, 26, [
        (19, None),        # κάμηλον        for a camel
        (20, "to go"),     # εἰσελθεῖν      to go
        (24, None),        # διὰ            through
        (21, None),        # τρυπήματος     the eye
        (22, None),        # ῥαφίδος        of a needle
        (23, None),        # ἢ              than
        (25, None),        # πλούσιον       for a rich person
    ]),
]
