# -*- coding: utf-8 -*-
# Luke 4 §4 — three defects.
#
# 1. (61)  Recitative ὅτι before an opening quotation mark
#    ("saying that “You are the Son of God!”"). Folded.
# 2. (104) Same, "said to them, that “Also I must preach...". Folded.
# 3. (105-112) "“Also I must preach the good news of the kingdom of God to the
#    other towns" — καί belongs with ταῖς ἑτέραις πόλεσιν ("to the other towns
#    also"), not with the verb; fronted, it reads as though preaching were an
#    additional activity. Moved to the end of its own phrase. Pure reorder.
CHAPTER = "Luke 4"
SECTION = 4
BLOCKS = [
    (61, 62, [
        (61, ""),                    # ὅτι — recitative, folded
    ]),
    (104, 105, [
        (104, ""),                   # ὅτι — recitative, folded
    ]),
    (105, 113, [
        (106, "“I"),                 # με
        (107, None),                 # δεῖ            must
        (108, None),                 # εὐαγγελίσασθαί preach the good news of
        (109, None),                 # τὴν βασιλείαν  the kingdom
        (110, None),                 # τοῦ θεοῦ       of God
        (111, None),                 # ταῖς ἑτέραις   to the other
        (112, "towns"),              # πόλεσιν
        (105, "also,"),              # Καὶ
    ]),
]
