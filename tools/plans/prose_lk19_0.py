# -*- coding: utf-8 -*-
# Luke 19 §0 — two defects.
#
# BLOCK 1 (83,90): read "saying that “With a sinful man he has gone in to
#   lodge!”" — a recitative ὅτι in front of an opening quotation mark, and
#   the quoted clause itself left in Greek order (Παρὰ ἁμαρτωλῷ ἀνδρὶ
#   εἰσῆλθεν καταλῦσαι), verb last. Fixed to:
#     "saying, “He has gone in to lodge with a sinful man!”"
#     83 λέγοντες "saying" -> "saying,"  (takes the comma that introduces speech)
#     84 ὅτι      "that"   -> ""         folded; recitative ὅτι marks a DIRECT
#        quotation and has no English word of its own
#     88 εἰσῆλθεν "he has gone in" -> "“He has gone in"  (same verb; it now
#        opens the quotation, so it carries the opening quotation mark)
#     87 ἀνδρὶ    "man"    -> "man!”"    (now clause-final, so it takes the
#        exclamation mark and the closing quotation mark)
#     85 Παρὰ, 86 ἁμαρτωλῷ, 89 καταλῦσαι keep their glosses unchanged.
#
# BLOCK 2 (117,120): read "And Jesus said to him, that “Today salvation has
#   come…" — the same recitative ὅτι, here sitting after the comma and in
#   front of the opening quotation mark. Folded. Nothing is reordered and
#   αὐτὸν keeps "him," with its comma, so the speech is still introduced.
CHAPTER = "Luke 19"
SECTION = 0
BLOCKS = [
    (83, 90, [
        (83, "saying,"),           # λέγοντες
        (84, ""),                  # ὅτι  recitative — folded
        (88, "“He has gone in"),   # εἰσῆλθεν
        (89, "to lodge"),          # καταλῦσαι  (was "to lodge!”" — the
                                   # exclamation and closing quote move to 87)
        (85, "with"),              # Παρὰ  (was "“With" — the opening quote
                                   # moves to 88, which now opens the speech)
        (86, None),                # ἁμαρτωλῷ   a sinful
        (87, "man!”"),             # ἀνδρὶ
    ]),
    (117, 120, [
        (117, None),   # αὐτὸν  him,
        (118, None),   # ὁ      (folded)
        (119, ""),     # ὅτι    recitative — folded
    ]),
]
