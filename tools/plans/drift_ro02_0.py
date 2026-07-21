# -*- coding: utf-8 -*-
# Romans 2:9 AND 2:10 -- the same exchanged pair, twice, in parallel verses.
# Found by tools/swap_scan.py. Both read "the Jew first, and then the Greek",
# which is correct English. Underneath, in both:
#     πρῶτον      labelled "the Jew"   -- G4412 is "first"
#     Ἰουδαίου τε labelled "first,"    -- G2453 is "Jew"
# Greek order is Ἰουδαίου τε πρῶτον; the units had been swapped into English
# order but the GLOSSES travelled with the wrong slots.
#
# Pure REORDER in both blocks: the units go back into the order whose labels are
# already correct for them, so the visible sentence is byte-identical and only
# the anchoring changes.
CHAPTER = "Romans 2"
SECTION = 0
BLOCKS = [
    (120, 122, [
        (121, "the Jew"),   # Ἰουδαίου τε
        (120, "first,"),    # πρῶτον
    ]),
    (134, 136, [
        (135, "the Jew"),   # Ἰουδαίῳ τε
        (134, "first,"),    # πρῶτον
    ]),
]
