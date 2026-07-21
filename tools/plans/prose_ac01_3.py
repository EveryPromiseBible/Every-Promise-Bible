# -*- coding: utf-8 -*-
# Acts 1 §3 — two Greek-order sentences.
#
# 1) Ps 109:8 quotation read "'His overseership let another take.'" — object-first
#    Greek order standing in English. Reordered to "'Another must take his
#    overseership.'"  Anchoring: ἕτερος = "Another" (subject), λαβέτω = "must take"
#    (3sg aorist imperative — "let him take" / "must take"; the jussive force stays
#    on the verb, which is more honest than the old split where "let" sat on λαβέτω
#    and "take" on ἕτερος), τὴν stays folded, αὐτοῦ = "his", ἐπισκοπὴν =
#    "overseership". Opening quote mark moves with the new first word; closing
#    quote + full stop move to the new last word.
#
# 2) "show which you have chosen of these two" — Greek order. Reordered to
#    "show which of these two you have chosen,". Every gloss is unchanged except
#    the comma, which moves from δύο to ἐξελέξω because ἐξελέξω now ends the clause.
CHAPTER = "Acts 1"
SECTION = 3
BLOCKS = [
    (114, 120, [
        (114, None),                # καί  — "and,"
        (119, "‘Another"),          # ἕτερος
        (118, "must take"),         # λαβέτω
        (117, None),                # Τὴν — folded
        (115, "his"),               # αὐτοῦ
        (116, "overseership.’"),    # ἐπισκοπὴν
    ]),
    (178, 185, [
        (178, None),                # ἀνάδειξον — "show"
        (179, None),                # ὃν — "which"
        (181, None),                # ἐκ — "of"
        (182, None),                # τούτων — "these"
        (183, None),                # τῶν — folded
        (184, "two"),               # δύο — comma moves off
        (180, "you have chosen,"),  # ἐξελέξω — now ends the clause
    ]),
]
