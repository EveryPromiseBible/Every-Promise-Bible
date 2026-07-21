# -*- coding: utf-8 -*-
# Acts 6 §1 — two fixes.
#
# 1) "But some rose up of those from the synagogue called Of the Freedmen, and of
#    Cyrenians and …" — the verb was wedged between "some" and its partitive
#    genitive, so the reader meets "of those from…" twenty words after the word it
#    belongs to. Moving ἀνέστησαν to the end of the subject phrase gives
#    "But some of those from the synagogue called Of the Freedmen, … and Asia
#    rose up, disputing with Stephen—". Pure reorder; only the comma moves from
#    Ἀσίας to ἀνέστησαν, which now closes the subject.
#
# 2) "they secretly instigated men saying “We have heard…" — a comma was missing
#    before the direct quotation. λέγοντας gains it; nothing else changes.
CHAPTER = "Acts 6"
SECTION = 1
BLOCKS = [
    (14, 34, [
        (14, None),         # δέ — "But"
        (15, None),         # τινες — "some"
        (17, None),         # τῶν — "of those"
        (18, None),         # ἐκ — "from"
        (19, None),         # τῆς — "the"
        (20, None),         # συναγωγῆς — "synagogue"
        (21, None),         # τῆς — folded
        (22, None),         # λεγομένης — "called"
        (23, None),         # Λιβερτίνων — "Of the Freedmen,"
        (24, None),         # καὶ — "and"
        (25, None),         # Κυρηναίων — "of Cyrenians"
        (26, None),         # καὶ — "and"
        (27, None),         # Ἀλεξανδρέων — "of Alexandrians"
        (28, None),         # καὶ — "and"
        (29, None),         # τῶν — "of those"
        (30, None),         # ἀπὸ — "from"
        (31, None),         # Κιλικίας — "Cilicia"
        (32, None),         # καὶ — "and"
        (33, "Asia"),       # Ἀσίας — comma moves off
        (16, "rose up,"),   # ἀνέστησαν — now closes the subject
    ]),
    (50, 51, [
        (50, "saying,"),    # λέγοντας — comma before the quotation
    ]),
]
