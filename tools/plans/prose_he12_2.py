# -*- coding: utf-8 -*-
# Hebrews 12:18-19. Two separate stumbles in one section, so both go in this one file.
#
# BLOCK 1 (units 4-6) read "...to what may be touched and that burned with fire, and
# darkness..."  "and that burned" reads as a past-tense finite verb with no subject;
# the reader parses "that burned" as a clause and then hits "with fire" and has to
# back up. This is the Greek order κεκαυμένῳ πυρὶ (participle before its noun) left
# standing. Reordering the noun ahead of its participle gives ordinary English:
#   6  πυρὶ        "with fire," -> "a fire"           (dative in the series governed by
#                                                      προσεληλύθατε, like ὄρει/πόλει below)
#   5  κεκαυμένῳ   "that burned" -> "that was blazing," (perf. pass. ptc of καίω,
#                                                      "having been kindled / burning")
# -> "...to what may be touched and a fire that was blazing, and darkness and gloom..."
#
# BLOCK 2 (units 18-20) read "and a voice whose words those who heard begged that no
# further word be spoken to them."  "whose words those who heard begged" has no verb
# joining the relative to the clause — the reader cannot tell what "whose words" does.
# The Greek is φωνῇ ῥημάτων, ἧς οἱ ἀκούσαντες παρῃτήσαντο...: ἧς is genitive dependent
# on οἱ ἀκούσαντες, i.e. "the hearers OF WHICH [voice] begged". Re-glossing to match
# the actual Greek grammar both fixes the English and tightens the anchoring:
#   18  ῥημάτων ἧς    "whose words" -> "of words, whose"  (ῥημάτων = "of words";
#                                                          ἧς = "whose")
#   19  οἱ ἀκούσαντες "those who heard" -> "hearers"      (same aorist ptc, noun form)
#   20  παρῃτήσαντο   "begged" -> unchanged
# -> "...and a voice of words, whose hearers begged that no further word be spoken to them."
# No unit is moved in block 2 and no Greek is touched in either block.
CHAPTER = "Hebrews 12"
SECTION = 2
BLOCKS = [
    (4, 7, [
        (4, None),                    # καὶ  "and"
        (6, "a fire"),                # πυρὶ
        (5, "that was blazing,"),     # κεκαυμένῳ
    ]),
    (18, 21, [
        (18, "of words, whose"),      # ῥημάτων ἧς
        (19, "hearers"),              # οἱ ἀκούσαντες
        (20, None),                   # παρῃτήσαντο  "begged"
    ]),
]
