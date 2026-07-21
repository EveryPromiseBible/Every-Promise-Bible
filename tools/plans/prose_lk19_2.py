# -*- coding: utf-8 -*-
# Luke 19 §2 — three defects.
#
# BLOCK 1 (57,58): "thus you shall say, that ‘The Lord has need of it.’”" —
#   recitative ὅτι in front of an opening quotation mark. It marks a DIRECT
#   quotation and has no English word; folded. ἐρεῖτε already carries the
#   comma that introduces the speech, so nothing else moves.
#
# BLOCK 2 (63,68): "Going away now, those sent found it just as he had told
#   them." — postposed δέ stranded after the participle in Greek order.
#   Pure reorder to "Now those sent, going away, found it just as he had told
#   them." Only capitalisation and two commas migrate:
#     64 δὲ            "now,"        -> "Now"
#     66 ἀπεσταλμένοι  "sent"        -> "sent,"
#     63 ἀπελθόντες    "Going away"  -> "going away,"
#
# BLOCK 3 (87,89): "And they said that “The Lord has need of it.”" — the same
#   recitative ὅτι; folded, and the comma introducing the speech moves onto
#   εἶπαν.
CHAPTER = "Luke 19"
SECTION = 2
BLOCKS = [
    (57, 58, [
        (57, ""),   # ὅτι  recitative — folded
    ]),
    (63, 68, [
        (64, "Now"),            # δὲ
        (65, None),             # οἱ             those
        (66, "sent,"),          # ἀπεσταλμένοι
        (63, "going away,"),    # ἀπελθόντες
        (67, None),             # εὗρον          found it
    ]),
    (87, 89, [
        (87, "said,"),   # εἶπαν
        (88, ""),        # ὅτι  recitative — folded
    ]),
]
