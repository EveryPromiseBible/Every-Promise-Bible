# -*- coding: utf-8 -*-
# Matthew 21:33 — GLOSS DRIFT.
# Greek: καὶ περιέθηκεν φραγμὸν αὐτῷ ...
#   #10 περιέθηκεν (G4060 "to place around")  was labelled "put a wall"
#   #11 φραγμὸν αὐτῷ (G5418 "a fence / enclosing barrier" + G846) was labelled "around it"
# The noun's own gloss ("wall") had slid onto the verb, leaving the fence word
# labelled with a bare prepositional phrase. Click φραγμόν on the site and the
# popup says "around it".
# Fix: keep the same word order, move the noun's gloss back onto the noun.
# Prose is unchanged: "... and put a wall around it and dug in it a winepress ..."
CHAPTER = "Matthew 21"
SECTION = 5
BLOCKS = [
    (10, 12, [(10, "put"), (11, "a wall around it")]),
]
