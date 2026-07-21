# -*- coding: utf-8 -*-
# Matthew 16 §0: "A generation wicked and adulterous looks for a sign" reads in
# Greek order (noun before its two adjectives). Reordered to
# "A wicked and adulterous generation looks for a sign". Pure reorder; the
# supplied indefinite article travels to the new first unit.
CHAPTER = "Matthew 16"
SECTION = 0
BLOCKS = [
    (40, 44, [
        (41, "A wicked"),    # πονηρὰ
        (42, None),          # καὶ — "and"
        (43, None),          # μοιχαλὶς — "adulterous"
        (40, "generation"),  # Γενεὰ
    ]),
]
