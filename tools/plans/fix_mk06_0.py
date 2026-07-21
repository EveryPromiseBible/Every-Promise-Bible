# -*- coding: utf-8 -*-
# Mark 6 §0 — two drifts.
#
# 1) #26-28: τούτῳ ("this man", dative) carried "from," while ταῦτα ("these things")
#    carried "did this man get these things". Reordered so τούτῳ holds "this man"
#    and ταῦτα holds "these things". Πόθεν already means "from where", so the
#    trailing "from" is dropped; prose reads at least as well.
#
# 2) #70-73: προφήτης ("prophet") was FOLDED BLANK while its gloss "A prophet"
#    sat on the negation Οὐκ, and ἄτιμος ("without honor") carried the negation
#    as "not without honor". Reordered to: προφήτης "A prophet" / ἔστιν "is" /
#    Οὐκ "not" / ἄτιμος "without honor". Prose unchanged.
CHAPTER = "Mark 6"
SECTION = 0
BLOCKS = [
    (26, 29, [
        (26, None),                # Πόθεν  — "“Where"
        (28, "did this man get"),  # τούτῳ
        (27, "these things,"),     # ταῦτα
    ]),
    (70, 74, [
        (73, "“A prophet"),        # προφήτης (was folded blank)
        (71, None),                # ἔστιν   — "is"
        (70, "not"),               # Οὐκ
        (72, "without honor"),     # ἄτιμος
    ]),
]
