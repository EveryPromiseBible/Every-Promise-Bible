# -*- coding: utf-8 -*-
# Matthew 12 §5: "A generation wicked and adulterous asks for a sign" reads in
# Greek order (noun before its two adjectives). Reordered to
# "A wicked and adulterous generation asks for a sign".
# Pure reorder; the opening quotation mark and the supplied indefinite article
# travel to the new first unit so the speech still opens correctly.
CHAPTER = "Matthew 12"
SECTION = 5
BLOCKS = [
    (18, 22, [
        (19, "“A wicked"),   # πονηρὰ
        (20, None),               # καὶ  — "and"
        (21, None),               # μοιχαλὶς — "adulterous"
        (18, "generation"),       # Γενεὰ
    ]),
]
