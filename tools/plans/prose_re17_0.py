# -*- coding: utf-8 -*-
# Revelation 17:6 read "And I marveled when I saw her with great wonder."
# That is Greek order (ἐθαύμασα ἰδὼν αὐτὴν θαῦμα μέγα) standing in English: the
# cognate accusative θαῦμα μέγα belongs to "marveled", but because the participle
# clause "when I saw her" has been left between them, "with great wonder" reads
# as modifying "saw" — as though John looked at her in a wondering manner.
#
# Fix by moving the participle clause to the front, so the verb and its cognate
# object sit together: "And when I saw her, I marveled with great wonder."
# Pure reorder — the only text change is a comma added after "her" to close the
# fronted clause. No gloss is rewritten and no anchoring moves.
CHAPTER = "Revelation 17"
SECTION = 0
BLOCKS = [
    (136, 142, [
        (136, None),        # Καὶ — "And"
        (138, None),        # ἰδὼν — "when I saw"
        (139, "her,"),      # αὐτὴν — comma closes the fronted clause
        (137, None),        # ἐθαύμασα — "I marveled"
        (140, None),        # μέγα — "with great"
        (141, None),        # θαῦμα — "wonder."
    ]),
]
