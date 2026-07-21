# -*- coding: utf-8 -*-
# Mark 16 longer ending — four gloss drifts:
#  16:13 ἐκείνοις ("them") carried "they did not believe" while ἐπίστευσαν
#        ("they believed") carried "them" — a straight swap.
#  16:17 σημεῖα ("signs") was labelled only "And"; "signs will follow" sat on
#        παρακολουθήσει.
#  16:17 δαιμόνια ("demons") carried "they will cast out demons" while the
#        verb ἐκβαλοῦσιν was rendered BLANK.
#  16:18 θανάσιμόν ("deadly") was labelled "anything" and τι ("anything")
#        was labelled "deadly," — a straight swap.
CHAPTER = "Mark 16"
SECTION = 2
BLOCKS = [
    (49, 52, [
        (51, "neither"),            # οὐδὲ
        (50, "did they believe"),   # ἐπίστευσαν
        (49, "them."),              # ἐκείνοις
    ]),
    (89, 94, [
        (90, "And these"),          # ταῦτα
        (89, "signs"),              # σημεῖα δὲ
        (91, "will follow"),        # παρακολουθήσει
        (92, None),                 # τοῖς — those
        (93, None),                 # πιστεύσασιν — who believe:
    ]),
    (94, 96, [
        (95, "they will cast out"), # ἐκβαλοῦσιν
        (94, "demons"),             # δαιμόνια
    ]),
    (106, 108, [
        (107, "anything"),          # τι
        (106, "deadly,"),           # θανάσιμόν
    ]),
]
