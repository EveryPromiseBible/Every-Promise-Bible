# -*- coding: utf-8 -*-
# Acts 28:28 read "that to the Gentiles has been sent this salvation of God" --
# Greek order (τοῖς ἔθνεσιν ἀπεστάλη τοῦτο τὸ σωτήριον τοῦ θεοῦ) left standing;
# the subject arrives after the verb and the reader has to hold "to the
# Gentiles" for four words. Reordered to "that this salvation of God has been
# sent to the Gentiles".
# Pure reorder -- no gloss reassigned. Only the ";" moves from τοῦ θεοῦ, no
# longer last, to τοῖς ἔθνεσιν, now last.
CHAPTER = "Acts 28"
SECTION = 3
BLOCKS = [
    (102, 107, [
        (104, None),                   # τοῦτο        "this"
        (105, None),                   # τὸ σωτήριον  "salvation"
        (106, "of God"),               # τοῦ θεοῦ
        (103, None),                   # ἀπεστάλη     "has been sent"
        (102, "to the Gentiles;"),     # τοῖς ἔθνεσιν
    ]),
]
