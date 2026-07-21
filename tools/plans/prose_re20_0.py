# -*- coding: utf-8 -*-
# Revelation 20:4 read as a sentence with no main clause:
#   "And the souls of those who had been beheaded for the testimony of Jesus and
#    for the word of God, and those who had not worshiped the beast or its image
#    and had not received the mark on the forehead or on their hand, and they
#    came to life and reigned with Christ a thousand years."
# The long subject runs on, and then an extra "and" (unit 85) blocks it from ever
# reaching its verb, so the reader hits "and they came to life" with nothing for
# the opening "And the souls..." to attach to.
#
# In the Greek this καί is the resumptive one that Greek puts after a long
# fronted subject; English does not use it. Fold it (english "") — the standard
# treatment for an untranslatable particle, and the Greek + tag still render.
# Nothing is reordered and no other gloss is touched.
#
# Result: "And the souls of those who had been beheaded ..., and those who had
# not worshiped ..., they came to life and reigned with Christ a thousand years."
CHAPTER = "Revelation 20"
SECTION = 0
BLOCKS = [
    (85, 86, [
        (85, ""),   # καὶ — resumptive, folded
    ]),
]
