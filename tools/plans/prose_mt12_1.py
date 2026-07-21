# -*- coding: utf-8 -*-
# Matthew 12 §1:
#  (a) "…on the Sabbath?” So that they might accuse him." — the ἵνα clause was
#      standing as its own sentence fragment. Repunctuated so it hangs off the
#      question: "…on the Sabbath?”—so that they might accuse him."
#      No reorder; ἵνα keeps its own gloss.
#  (b) "if it falls on the Sabbath into a pit" reads in Greek order; reordered
#      to "if it falls into a pit on the Sabbath". Pure reorder.
CHAPTER = "Matthew 12"
SECTION = 1
BLOCKS = [
    (21, 22, [
        (21, "—so that"),        # ἵνα
    ]),
    (40, 43, [
        (41, None),              # εἰς — "into"
        (42, "a pit"),           # βόθυνον
        (40, "on the Sabbath,"), # τοῖς σάββασιν
    ]),
]
