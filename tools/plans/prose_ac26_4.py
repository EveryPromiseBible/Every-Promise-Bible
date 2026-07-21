# -*- coding: utf-8 -*-
# Acts 26:27,31 -- two stumbles in one section.
# (a) "Do you believe, King Agrippa, the prophets?" is Greek order
#     (πιστεύεις, βασιλεῦ Ἀγρίππα, τοῖς προφήταις;): the object is stranded
#     behind the vocative and the question only resolves at the last word.
#     Reordered to "King Agrippa, do you believe the prophets?" -- pure reorder;
#     πιστεύεις just loses the comma it no longer needs and its capital, which
#     passes to βασιλεῦ, now first in the sentence.
# (b) "...saying “This man is doing nothing..." -- speech verb with no comma
#     before the quotation mark. 109 λέγοντες ὅτι "saying" -> "saying,".
CHAPTER = "Acts 26"
SECTION = 4
BLOCKS = [
    (50, 54, [
        (51, "King"),               # βασιλεῦ
        (52, "Agrippa,"),           # Ἀγρίππα
        (50, "do you believe"),     # πιστεύεις
        (53, None),                 # τοῖς προφήταις "the prophets?"
    ]),
    (109, 110, [
        (109, "saying,"),           # λέγοντες ὅτι
    ]),
]
