# -*- coding: utf-8 -*-
# Luke 1 §4 (Benedictus) — nine defects, two of them real gloss drift.
#
# 1. (0-4)  "Now for Elizabeth was fulfilled the time for her to give birth" —
#    Greek order. -> "Now the time was fulfilled for Elizabeth to give birth".
#    Τῇ δὲ keeps δέ ("Now"); the dative force moves onto Ἐλισάβετ itself
#    ("for Elizabeth"), and τοῦ τεκεῖν αὐτήν loses the now-redundant "her".
# 2. (55-57) "they said to her, that “No one there is among your relatives" —
#    recitative ὅτι folded, and Οὐδείς / ἐστιν put into English order.
# 3. *** GLOSS DRIFT *** (86, 89) crossed:
#       ἀνεῴχθη   ("was opened")  was labelled "And immediately"
#       παραχρῆμα ("immediately") was labelled "was opened"
#    Each gloss returned to its own word; the clause is reordered so it still
#    reads "Immediately his mouth was opened".
# 4. *** GLOSS DRIFT *** (109-111) crossed:
#       τὰ ῥήματα ("the words/things") was labelled "these"
#       ταῦτα     ("these")            was labelled "things"
#    Reordered so the prose is unchanged ("all these things") but each Greek
#    word now carries its own gloss.
# 5. (168-173) "through the mouth of the holy from of old prophets of his—"
#    -> "through the mouth of his holy prophets from of old—".
# 6. (192-194) "to remember covenant his holy —the oath"
#    -> "to remember his holy covenant— the oath".
# 7. (201-209) "to grant us that without fear, from the hand of enemies having
#    been delivered, we might serve him" -> "to grant us that, having been
#    delivered from the hand of enemies, we might serve him without fear".
#    ἀφόβως still glosses "without fear"; the supplied "that" moves onto ἡμῖν.
# 8. (219-223) "And you child, a prophet of the Most High will be called;"
#    -> "And you, child, will be called a prophet of the Most High;".
# 9. (245-249) "by which will visit us the sunrise from on high"
#    -> "by which the sunrise from on high will visit us,".
CHAPTER = "Luke 1"
SECTION = 4
BLOCKS = [
    (0, 5, [
        (0, "Now"),                     # Τῇ δὲ — δέ carries "Now"
        (3, None),                      # ὁ χρόνος          the time
        (2, None),                      # ἐπλήσθη           was fulfilled
        (1, "for Elizabeth"),           # Ἐλισάβετ (dative)
        (4, "to give birth,"),          # τοῦ τεκεῖν αὐτήν
    ]),
    (55, 58, [
        (55, ""),                       # ὅτι — recitative, folded
        (57, "“There is"),              # ἐστιν
        (56, "no one"),                 # Οὐδείς
    ]),
    (86, 90, [
        (89, "Immediately"),            # παραχρῆμα   (was "was opened")
        (87, None),                     # αὐτοῦ       his
        (88, None),                     # τὸ στόμα    mouth
        (86, "was opened,"),            # ἀνεῴχθη δὲ  (was "And immediately")
    ]),
    (109, 112, [
        (109, None),                    # πάντα       all
        (111, "these"),                 # ταῦτα       (was "things")
        (110, "things"),                # τὰ ῥήματα   (was "these")
    ]),
    (168, 174, [
        (168, "of"),                    # τῶν         genitive article
        (173, "his"),                   # αὐτοῦ
        (169, None),                    # ἁγίων       holy
        (172, None),                    # προφητῶν    prophets
        (170, None),                    # ἀπ’         from
        (171, "of old—"),               # αἰῶνος
    ]),
    (192, 195, [
        (193, None),                    # ἁγίας αὐτοῦ his holy
        (192, "covenant—"),             # διαθήκης
        (194, "the oath"),              # ὅρκον
    ]),
    (201, 210, [
        (201, None),                    # τοῦ δοῦναι  to grant
        (202, "us that,"),              # ἡμῖν
        (207, "having been delivered"), # ῥυσθέντας
        (204, None),                    # ἐκ          from
        (205, None),                    # χειρὸς      the hand
        (206, "of enemies,"),           # ἐχθρῶν
        (208, None),                    # λατρεύειν   we might serve
        (209, None),                    # αὐτῷ        him
        (203, "without fear"),          # ἀφόβως
    ]),
    (219, 224, [
        (219, "And you,"),              # καὶ σὺ δέ
        (220, None),                    # παιδίον     child,
        (223, "will be called"),        # κληθήσῃ
        (221, None),                    # προφήτης    a prophet
        (222, "of the Most High;"),     # Ὑψίστου
    ]),
    (245, 250, [
        (247, None),                    # ἀνατολὴ     the sunrise
        (248, None),                    # ἐξ          from
        (249, "on high"),               # ὕψους
        (245, None),                    # ἐπισκέψεται will visit
        (246, "us,"),                   # ἡμᾶς
    ]),
]
