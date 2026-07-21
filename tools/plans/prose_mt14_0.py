# -*- coding: utf-8 -*-
# Matthew 14 §0:
#  (a) "And she prompted by her mother, “Give me she said, here on a platter the
#      head of John the Baptist.”" — the speech verb φησίν was stranded inside
#      the quotation and the main clause had no verb. Reordered to
#      "And she, prompted by her mother, said, “Give me here on a platter the
#      head of John the Baptist.”"  Pure reorder; φησίν keeps "said".
#  (b) "he sent and had beheaded John in the prison" — reglossed ἀπεκεφάλισεν
#      as plain "and beheaded", giving "he sent and beheaded John in the
#      prison". No reorder.
CHAPTER = "Matthew 14"
SECTION = 0
BLOCKS = [
    (81, 95, [
        (81, "And she,"),   # ἡ δὲ
        (82, None),         # προβιβασθεῖσα — "prompted"
        (83, None),         # ὑπὸ — "by"
        (84, None),         # αὐτῆς — "her"
        (85, None),         # τῆς μητρὸς — "mother,"
        (88, "said,"),      # φησίν
        (86, None),         # Δός — "“Give"
        (87, None),         # μοι — "me"
        (89, None),         # ὧδε — "here"
        (90, None),         # ἐπὶ — "on"
        (91, None),         # πίνακι — "a platter"
        (92, None),         # τὴν κεφαλὴν — "the head"
        (93, None),         # Ἰωάννου — "of John"
        (94, None),         # τοῦ βαπτιστοῦ — "the Baptist.”"
    ]),
    (106, 107, [
        (106, "and beheaded"),  # ἀπεκεφάλισεν
    ]),
]
