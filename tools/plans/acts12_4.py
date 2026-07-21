# -*- coding: utf-8 -*-
# Acts 12 §4 — No Small Commotion
# At daybreak there is uproar among the soldiers over Peter; Herod, not
# finding him, has the guards led away and goes down to Caesarea.
CHAPTER = "Acts 12"
SECTION = 4
BLOCKS = [
    # Now when day had come,
    (0, 3, [(1,"Now"),(2,"when day"),(0,"had come,")]),
    # there was no small commotion
    (3, 7, [(3,"there was"),(5,"no"),(6,"small"),(4,"commotion")]),
    # as to what then had become of Peter.  (fold em-dash)
    (10, 15, [(10,"as to what"),(11,"then"),(14,"had become"),(12,""),(13,"of Peter.")]),
    # But Herod, searching for
    (15, 18, [(16,"But"),(15,"Herod,"),(17,"searching for")]),
    # Judea  (fold em-dash)
    (30, 32, [(30,""),(31,"Judea")]),
]
