# -*- coding: utf-8 -*-
# Acts 8 §1 — six defects, all Greek order or a resumptive pronoun.
#
# 1) "to whom were paying attention all, from small to great" -> "to whom all
#    were paying attention, …". Pure reorder; the comma moves to προσεῖχον.
#
# 2) "…hearing that Samaria had received the word of God, they sent to them
#    Peter and John" — "the apostles" is already the stated subject, so the
#    resumptive "they" breaks the sentence. ἀπέστειλαν -> "sent".
#
# 3) "seeing that through the laying on of the apostles' hands is given the
#    Spirit," -> "seeing that the Spirit is given through the laying on of the
#    apostles' hands,". Pure reorder; the comma moves from πνεῦμα to χειρῶν.
#
# 4) "…, he offered them money" — same resumptive-pronoun break after the
#    participial clause. προσήνεγκεν -> "offered".
#
# 5) "“Your silver with you may it be to destruction—" — the verb was stranded
#    behind its prepositional phrase. -> "“Your silver— may it be to destruction
#    with you—". Pure reorder; the dashes move to the words that now end each
#    part.
#
# 6) "There is to you no part nor a share in this matter" -> "There is no part
#    nor a share for you in this matter". σοι moves to its natural English slot
#    and reads "for you" rather than "to you" — same dative, ordinary English.
CHAPTER = "Acts 8"
SECTION = 1
BLOCKS = [
    (21, 24, [
        (21, None),                       # ᾧ — "to whom"
        (23, "all"),                      # πάντες — comma moves off
        (22, "were paying attention,"),   # προσεῖχον — now closes the clause
    ]),
    (102, 103, [
        (102, "sent"),                    # ἀπέστειλαν — resumptive "they" removed
    ]),
    (148, 158, [
        (156, None),        # τὸ — "the"
        (157, "Spirit"),    # πνεῦμα — comma moves off
        (155, None),        # δίδοται — "is given"
        (148, None),        # διὰ — "through"
        (149, None),        # τῆς — "the"
        (150, None),        # ἐπιθέσεως — "laying on"
        (151, None),        # τῶν — "of the"
        (152, None),        # ἀποστόλων — "apostles'"
        (153, None),        # τῶν — folded
        (154, "hands,"),    # χειρῶν — now closes the clause
    ]),
    (158, 159, [
        (158, "offered"),   # προσήνεγκεν — resumptive "he" removed
    ]),
    (180, 188, [
        (180, None),           # σου — "“Your"
        (181, "silver—"),      # ἀργύριόν
        (182, None),           # Τὸ — folded
        (185, None),           # εἴη — "may it be"
        (186, None),           # εἰς — "to"
        (187, "destruction"),  # ἀπώλειαν — dash moves off
        (183, None),           # σὺν — "with"
        (184, "you—"),         # σοὶ — now closes the clause
    ]),
    (197, 202, [
        (197, None),        # οὐκ ἔστιν — "There is"
        (199, None),        # μερὶς — "no part"
        (200, None),        # οὐδὲ — "nor"
        (201, None),        # κλῆρος — "a share"
        (198, "for you"),   # σοι — dative, now in its English slot
    ]),
]
