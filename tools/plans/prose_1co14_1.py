# -*- coding: utf-8 -*-
# Three Greek-order sentences in 1 Corinthians 14 §1.
#
# BLOCK A — 14:9 read "So also you through the tongue if you don't give clear
# speech, how will what is spoken be known?" The prepositional phrase διὰ τῆς
# γλώσσης sits between subject and conditional clause, so the reader hits
# "you through the tongue if" and stalls. Moved to the end of its own clause:
# "So also you, if you don't give clear speech through the tongue, how will..."
#   57 ὑμεῖς       "you" -> "you,"           (comma follows the subject now)
#   64 λόγον       "speech," -> "speech"     (comma no longer belongs here)
#   59 τῆς γλώσσης "the tongue" -> "the tongue," (clause-final comma)
#
# BLOCK B — 14:10 read "There are so many kinds of languages perhaps in the
# world". The parenthetical εἰ τύχοι is stranded after the noun phrase it
# hedges. Pure reorder, no gloss changes:
# "There are perhaps so many kinds of languages in the world,"
#
# BLOCK C — 14:12 read "seek to the building up of the church that you may
# abound." The πρός phrase was pulled in front of its own ἵνα clause, which
# leaves "seek to the building up ... that you may abound" reading as two
# unrelated tails. Restoring English order gives "seek that you may abound for
# the building up of the church."
#   105 πρὸς          "to" -> "for"    (πρός + accusative of purpose; "for the
#       building up" is the same relation, just the English idiom after "abound")
#   109 περισσεύητε   "you may abound." -> "you may abound"
#   107 τῆς ἐκκλησίας "of the church" -> "of the church."
CHAPTER = "1 Corinthians 14"
SECTION = 1
BLOCKS = [
    (55, 65, [
        (55, None),             # οὕτως — "So"
        (56, None),             # καὶ — "also"
        (57, "you,"),           # ὑμεῖς
        (60, None),             # ἐὰν — "if"
        (61, None),             # μὴ — "you don't"
        (62, None),             # δῶτε — "give"
        (63, None),             # εὔσημον — "clear"
        (64, "speech"),         # λόγον
        (58, None),             # διὰ — "through"
        (59, "the tongue,"),    # τῆς γλώσσης
    ]),
    (73, 80, [
        (73, None),             # εἰσιν — "There are"
        (77, None),             # εἰ τύχοι — "perhaps"
        (74, None),             # τοσαῦτα — "so many"
        (75, None),             # γένη — "kinds"
        (76, None),             # φωνῶν — "of languages"
        (78, None),             # ἐν — "in"
        (79, None),             # κόσμῳ — "the world,"
    ]),
    (104, 110, [
        (104, None),                # ζητεῖτε — "seek"
        (108, None),                # ἵνα — "that"
        (109, "you may abound"),    # περισσεύητε
        (105, "for"),               # πρὸς
        (106, None),                # τὴν οἰκοδομὴν — "the building up"
        (107, "of the church."),    # τῆς ἐκκλησίας
    ]),
]
