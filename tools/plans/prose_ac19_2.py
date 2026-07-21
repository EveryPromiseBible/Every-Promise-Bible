# -*- coding: utf-8 -*-
# Acts 19:13 read "attempted to name over those having the evil spirits the
# name of the Lord Jesus" -- Greek order (ὀνομάζειν ἐπὶ τοὺς ἔχοντας ... τὸ
# ὄνομα ...) left standing; the object arrives long after the verb and the
# reader loses the thread. Reordered to "attempted to name the name of the Lord
# Jesus over those having the evil spirits".
# Pure reorder -- no gloss is reassigned. The only change is that the comma
# before "saying" moves from Ἰησοῦ (no longer last) to τὰ πνεύματα τὰ πονηρὰ
# (now last).
CHAPTER = "Acts 19"
SECTION = 2
BLOCKS = [
    (7, 14, [
        (7, None),                     # ὀνομάζειν            "to name"
        (11, None),                    # τὸ ὄνομα             "the name"
        (12, None),                    # τοῦ κυρίου           "of the Lord"
        (13, "Jesus"),                 # Ἰησοῦ
        (8, None),                     # ἐπὶ                  "over"
        (9, None),                     # τοὺς ἔχοντας         "those having"
        (10, "the evil spirits,"),     # τὰ πνεύματα τὰ πονηρὰ
    ]),
]
