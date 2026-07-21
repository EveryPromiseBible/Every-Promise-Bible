# -*- coding: utf-8 -*-
# Revelation 9 §0 — two defects.
#
# (1) 9:5 read "And they were allowed not to kill them, but that they would be
#     tormented for five months." In English "allowed not to kill" means they had
#     permission to refrain from killing — the opposite of the sense. The Greek
#     καὶ ἐδόθη αὐτοῖς ἵνα μὴ ἀποκτείνωσιν αὐτούς is "and it was granted them
#     that they should not kill them", i.e. their commission was limited.
#     Fix by re-glossing the two units so the negative reads as a constraint:
#       ἐδόθη αὐτοῖς  "they were allowed" -> "it was granted them"
#         (ἐδόθη is aorist passive of δίδωμι, "was given/granted"; "granted"
#          is closer to the verb than "allowed" and drops the false permission)
#       ἵνα μὴ        "not to"            -> "that they should not"
#         (ἵνα = "that", μή = "not" — the negative stays on the μή unit, so
#          clicking ἵνα μὴ still shows the negation it actually carries)
#     The following ἀλλ’ / ἵνα ("but" / "that") then flow correctly into
#     "but that they would be tormented for five months."
#
# (2) 9:11 read "They have over them as king the angel of the bottomless pit."
#     That is Greek order (ἔχουσιν ἐπ’ αὐτῶν βασιλέα τὸν ἄγγελον) standing in
#     English; the object arrives last, after two stacked adjuncts. Reordering
#     "as king" ahead of "over them" gives "They have as king over them the
#     angel of the bottomless pit." Pure reorder — no gloss is rewritten.
CHAPTER = "Revelation 9"
SECTION = 0
BLOCKS = [
    (89, 91, [
        (89, "it was granted them"),      # ἐδόθη αὐτοῖς
        (90, "that they should not"),     # ἵνα μὴ
    ]),
    (188, 193, [
        (188, None),                      # ἔχουσιν — "They have"
        (190, None),                      # βασιλέα — "as king"
        (189, None),                      # ἐπ’ αὐτῶν — "over them"
        (191, None),                      # τὸν ἄγγελον — "the angel"
        (192, None),                      # τῆς ἀβύσσου — "of the bottomless pit;"
    ]),
]
