# -*- coding: utf-8 -*-
# John 8:16 read "And if I judge, now, I— my judgment is true" — the postposed
# δέ ("now") and the emphatic ἐγώ are both left stranded after the verb, and the
# reader hits a dash with nothing resolved. Reordered to "And yet if I judge, my
# judgment is true".
# Gloss edits, all of them putting the English back on its own Greek word:
#   83 δὲ    "now,"     -> "yet"    (adversative δέ, which is what it is doing here:
#                                    "I judge no one — and yet if I do judge…")
#   84 ἐγώ   "I—"       -> "I"      (the emphatic subject pronoun, now before the verb)
#   82 κρίνω "I judge," -> "judge," (the "I" it used to carry now sits on ἐγώ,
#                                    where it belongs; κρίνω keeps the verb)
CHAPTER = "John 8"
SECTION = 0
BLOCKS = [
    (80, 85, [
        (80, None),        # καὶ  — And
        (83, "yet"),       # δὲ
        (81, None),        # ἐὰν  — if
        (84, "I"),         # ἐγώ
        (82, "judge,"),    # κρίνω
    ]),
]
