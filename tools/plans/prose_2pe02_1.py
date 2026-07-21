# -*- coding: utf-8 -*-
# 2 Peter 2:8-9 read:
#   "...for that righteous man, living among them, day after day, by what he saw
#    and heard tormented his righteous soul over their lawless deeds. then the
#    Lord knows how to rescue..."
# Two defects in one sentence:
#  (1) Greek order left standing: the instrumental datives βλέμματι/ἀκοῇ sit
#      between the subject ("that righteous man") and its verb ἐβασάνιζεν
#      ("tormented"), so the reader loses the subject before the verb arrives.
#      Moving them after the object restores English order.
#  (2) A full stop before "then" broke the if/then: units 0-1 open "For if God
#      did not spare...", and unit 67 "then" is the apodosis. This is the
#      corpus's last lowercase sentence-start — the fix is the comma, not a
#      capital, because "then" genuinely continues the sentence.
# Every gloss change below is punctuation only, on its own original unit.
# No English word moves onto a different Greek word.
CHAPTER = "2 Peter 2"
SECTION = 1
BLOCKS = [
    (55, 67, [
        (55, "them"),    # αὐτοῖς     — was "them," ; comma dropped so
                         #              "living among them day after day" is one phrase
        (56, None),      # ἡμέραν     — day
        (57, None),      # ἐξ         — after
        (58, None),      # ἡμέρας     — day,
        (62, None),      # ἐβασάνιζεν — tormented  (verb now follows its subject)
        (63, None),      # δικαίαν    — his righteous
        (64, None),      # ψυχὴν      — soul
        (65, None),      # ἀνόμοις    — over their lawless
        (66, "deeds"),   # ἔργοις     — was "deeds." ; sentence continues
        (59, None),      # βλέμματι   — by what he saw
        (60, None),      # καὶ        — and
        (61, "heard,"),  # ἀκοῇ       — was "heard" ; now closes the protasis
    ]),
]
