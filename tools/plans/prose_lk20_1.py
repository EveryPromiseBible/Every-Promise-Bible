# -*- coding: utf-8 -*-
# Luke 20 §1 — four defects, all Greek word order standing in English.
#
# BLOCK 1 (46,53): read "but they, that one too having beaten and dishonored,
#   sent away empty-handed." — the object fronted before its participles and
#   the main verb left with no object at all. Reordered to
#   "but they, having beaten and dishonored that one too, sent him away
#    empty-handed."
#     47 κἀκεῖνον     "that one too" -> "that one too,"  (takes the comma)
#     50 ἀτιμάσαντες  "dishonored,"  -> "dishonored"     (gives it up)
#     51 ἐξαπέστειλαν "sent away"    -> "sent him away"  — exactly the gloss
#        this same verb already carries at unit 38 in this section, where the
#        object is present; the object here is κἀκεῖνον, which the English
#        cannot reach across the participles.
#
# BLOCK 2 (57,62): read "but they, also this one having wounded, threw out."
#   Same defect, same fix:
#   "but they, having wounded this one also, threw him out."
#     60 τραυματίσαντες "having wounded," -> "having wounded"
#     58 καὶ            "also"            -> "also,"
#     61 ἐξέβαλον       "threw out."      -> "threw him out."
#
# BLOCK 3 (76,79): read "Perhaps this one they will respect.’" — object before
#   verb. Pure reorder to "Perhaps they will respect this one.’"; the full stop
#   and closing single quotation mark move from ἐντραπήσονται onto τοῦτον so
#   the lord's speech still closes.
#
# BLOCK 4 (184,190): read "for they knew that against them he had told this
#   parable." — prepositional phrase fronted in Greek order. Pure reorder to
#   "for they knew that he had told this parable against them."; only the full
#   stop moves, from παραβολὴν onto αὐτοὺς.
CHAPTER = "Luke 20"
SECTION = 1
BLOCKS = [
    (46, 53, [
        (46, None),               # οἱ δὲ         but they,
        (48, None),               # δείραντες     having beaten
        (49, None),               # καὶ           and
        (50, "dishonored"),       # ἀτιμάσαντες
        (47, "that one too,"),    # κἀκεῖνον
        (51, "sent him away"),    # ἐξαπέστειλαν
        (52, None),               # κενόν         empty-handed.
    ]),
    (57, 62, [
        (57, None),                # οἱ δὲ            but they,
        (60, "having wounded"),    # τραυματίσαντες
        (59, None),                # τοῦτον           this one
        (58, "also,"),             # καὶ
        (61, "threw him out."),    # ἐξέβαλον
    ]),
    (76, 79, [
        (76, None),                  # ἴσως           Perhaps
        (78, "they will respect"),   # ἐντραπήσονται
        (77, "this one.’"),          # τοῦτον
    ]),
    (184, 190, [
        (186, None),        # εἶπεν       he had told
        (187, None),        # ταύτην      this
        (188, None),        # τὴν         (folded)
        (189, "parable"),   # παραβολὴν
        (184, None),        # πρὸς        against
        (185, "them."),     # αὐτοὺς
    ]),
]
