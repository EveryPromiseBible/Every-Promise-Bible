# -*- coding: utf-8 -*-
# John 4:12 -- gloss drift, not a prose defect. The English reads correctly
# ("Surely you are not greater than our father Jacob"), which is why every
# earlier pass walked past it. But the labels are wrong underneath:
#
#     181  εἶ  "than"
#
# εἶ is the copula, "you are". Greek has no word for "than" at all -- the
# comparison is carried by the GENITIVE (ἡμῶν πατρὸς, "than our father"). So
# clicking εἶ on the site today reports "than", which is not what that word
# means in any context.
#
# This is the same defect already repaired at John 8:53 (see fix_jn08_2b.py),
# and it is repaired the same way, so the two parallel verses now agree:
#     179 μὴ σὺ  "Surely you"   -- the interrogative negative expecting "no",
#                                  plus the pronoun; one unit holds both tokens
#     181 εἶ     "are not"      -- the copula, carrying the English negation
#     180 μείζων "greater"
#     182 ἡμῶν   "than our"     -- the genitive of comparison, which is where
#                                  English's "than" actually belongs
#     183 πατρὸς "father"
#
# The one compromise, identical to 8:53 and documented there: μή's negation
# surfaces on the copula rather than on μή itself, because English cliticises
# negation onto "are" ("are not" is a single grammatical unit) and a single
# unit cannot supply a discontinuous "Surely ... not".
#
# The visible prose is BYTE-IDENTICAL before and after. Only the anchoring
# changes -- which is the entire point.
CHAPTER = "John 4"
SECTION = 0
BLOCKS = [
    (179, 184, [
        (179, "Surely you"),   # μὴ σὺ
        (181, "are not"),      # εἶ
        (180, None),           # μείζων -> "greater"
        (182, "than our"),     # ἡμῶν
        (183, None),           # πατρὸς -> "father"
    ]),
]
