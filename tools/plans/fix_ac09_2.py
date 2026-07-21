# -*- coding: utf-8 -*-
# Two gloss-drift defects in Acts 9 §2:
#  (a) u24 ἐστιν was glossed "the man"; "the man" belongs to the folded article ὁ
#      (u25) heading the participle πορθήσας, and u22 Οὐχ carried the copula ("Is
#      not"). Reorder so ἐστιν carries "Is", Οὐχ carries "not", ὁ carries "the man".
#      Matches the correct οὗτός/ἐστιν pair at u60-61 of this same section.
#      The opening curly quote travels to the new first unit.
#  (b) u66 ἡμέραι ("days") was glossed "many" and u67 ἱκαναί ("many") glossed
#      "days" — plainly inverted. Swap the glosses onto their own Greek.
#      Acts 9 §3 (~u214-215) is the model: ἱκανὰς "many" / ἡμέρας "days".
# Prose identical in both places.
CHAPTER = "Acts 9"
SECTION = 2
BLOCKS = [
    (22, 27, [(24, '“Is'), (22, 'not'), (23, 'this'), (25, 'the man'), (26, None)]),
    (66, 68, [(67, 'many'), (66, 'days')]),
]
