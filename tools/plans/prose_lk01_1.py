# -*- coding: utf-8 -*-
# Luke 1 §1 — four prose defects.
#
# 1. The section opened "It happened in the days of Herod ... a certain priest
#    named Zechariah, of the division of Abijah;" — a verbless fragment. Greek
#    Ἐγένετο ... ἱερεύς τις is the existential "there arose / there was".
#    Regloss unit 0 only: "It happened" -> "There was". No reorder.
# 2. "walking in all the commandments and requirements of the Lord blameless."
#    ἄμεμπτοι was stranded at the end. Move it next to πορευόμενοι and gloss it
#    adverbially — it still labels ἄμεμπτοι and nothing else.
# 3. "And many of the sons of Israel he will turn to the Lord their God." is
#    Greek order. Move ἐπιστρέψει ("he will turn") to the front of its own
#    clause; every other gloss is untouched.
# 4. "they realized that a vision he had seen in the temple" — Greek order.
#    Swap ὀπτασίαν / ἑώρακεν so it reads "that he had seen a vision".
# 5. "saying, that “Thus the Lord has done for me" — ὅτι here is recitative
#    (it marks the direct speech that the quotation mark already marks).
#    Fold it: Greek stays visible, English blank.
CHAPTER = "Luke 1"
SECTION = 1
BLOCKS = [
    (0, 1, [
        (0, "There was"),          # Ἐγένετο
    ]),
    (30, 38, [
        (30, None),                # πορευόμενοι  walking
        (37, "blamelessly"),       # ἄμεμπτοι
        (31, None),                # ἐν           in
        (32, None),                # πάσαις       all
        (33, None),                # ταῖς ἐντολαῖς the commandments
        (34, None),                # καὶ          and
        (35, None),                # δικαιώμασιν  requirements
        (36, "of the Lord."),      # τοῦ κυρίου — takes the full stop that
                                   #   used to sit on the moved "blameless."
    ]),
    (153, 162, [
        (157, None),               # ἐπιστρέψει   he will turn
        (153, None),               # πολλοὺς      many
        (154, None),               # τῶν          of the
        (155, None),               # υἱῶν         sons
        (156, None),               # Ἰσραὴλ       of Israel
        (158, None),               # ἐπὶ          to
        (159, None),               # κύριον       the Lord
        (160, None),               # αὐτῶν        their
        (161, None),               # τὸν θεὸν     God.
    ]),
    (266, 268, [
        (267, None),               # ἑώρακεν      he had seen
        (266, None),               # ὀπτασίαν     a vision
    ]),
    (302, 303, [
        (302, ""),                 # ὅτι — recitative, folded
    ]),
]
