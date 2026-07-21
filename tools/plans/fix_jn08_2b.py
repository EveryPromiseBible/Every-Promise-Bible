# -*- coding: utf-8 -*-
# John 8:53 -- second pass. The first fix corrected a real error (εἶ, "are", was
# glossed "than") but cost the prose: it read
#     "Surely not— are you greater than our father Abraham, who died?"
# which is worse English than what it replaced. Rule 1 of this project is that it
# has to read well, so this restores the natural sentence while keeping every
# label honest:
#     μή   "Surely"    -- the interrogative negative, which expects the answer "no"
#     σὺ   "you"
#     εἶ   "are not"   -- the copula, carrying the English negation
#     μείζων "greater"
# The one compromise is that μή's negation surfaces on the copula rather than on
# μή itself. English cliticises negation onto "are" ("are not" is a single
# grammatical unit) and μή cannot supply a discontinuous "Surely ... not" from one
# unit. Every word still contributes its own sense, and nothing carries a label
# belonging to a different word -- which the previous state did.
CHAPTER = "John 8"
SECTION = 2
BLOCKS = [
    (88, 92, [
        (88, "Surely"),     # μή
        (90, "you"),        # σὺ
        (89, "are not"),    # εἶ
        (91, None),         # μείζων -> "greater"
    ]),
]
