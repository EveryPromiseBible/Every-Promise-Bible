# -*- coding: utf-8 -*-
# Luke 9 §5 — He Set His Face Toward Jerusalem
CHAPTER = "Luke 9"
SECTION = 5
BLOCKS = [
    # Now it happened,
    (0, 2, [(1,"Now"),(0,"it happened,")]),
    # as the days of his taking up were being fulfilled,
    (2, 9, [(2,"as"),(4,"the"),(5,"days"),(6,"of"),(8,"his"),(7,"taking up"),(3,"were being fulfilled,")]),
    # that he firmly set his face to go to Jerusalem.
    (9, 17, [(9,"that"),(10,"he"),(13,"firmly set"),(11,"his"),(12,"face"),(14,"to go"),(15,"to"),(16,"Jerusalem.")]),
    # because his face was going to Jerusalem  (fold article)
    (35, 43, [(35,"because"),(38,"his"),(37,"face"),(36,""),(39,"was"),(40,"going"),(41,"to"),(42,"Jerusalem.")]),
    # Now seeing it,
    (43, 45, [(44,"Now"),(43,"seeing it,")]),
    # as they went on the road  (fold resumptive pronoun)
    (71, 72, [(71,"")]),
    # someone said to him,
    (75, 79, [(76,"someone"),(75,"said"),(77,"to"),(78,"him,")]),
    # And Jesus said to him,
    (83, 87, [(83,"And"),(86,"Jesus"),(84,"said"),(85,"to him,")]),
    # "The foxes have dens,
    (87, 91, [(87,"“The"),(88,"foxes"),(90,"have"),(89,"dens,")]),
    # have nests;  (supply gapped verb)
    (95, 96, [(95,"have nests;")]),
    # but the Son of Man does not have where to lay his head
    (96, 105,[(96,"but the"),(97,"Son"),(98,"of Man"),(99,"does not"),(100,"have"),(101,"where"),
              (104,"to lay"),(102,"his"),(103,"head.”")]),
    # Now he said to another,
    (105,107,[(106,"Now"),(105,"he said")]),
    # allow me first to go and bury my father
    (114,121,[(114,"allow"),(115,"me"),(117,"first"),(116,"to go and"),(118,"bury"),(119,"my"),(120,"father.”")]),
    # Now he said to him,
    (121,124,[(122,"Now"),(121,"he said"),(123,"to him,")]),
    # but you, go and announce
    (131,132,[(131,"go and")]),
    # Now another also said,
    (136,140,[(137,"Now"),(139,"another"),(138,"also"),(136,"said,")]),
    # But Jesus said,  (fold em-dash article placeholder)
    (151,155,[(152,"But"),(154,"Jesus"),(151,"said,"),(153,"")]),
    # putting his hand
    (157,158,[(157,"his")]),
    # looking back  (fold "at the things")
    (162,166,[(162,"looking"),(163,""),(164,""),(165,"back")]),
    # is fit for the kingdom of God  (remove doubled "is")
    (166,171,[(167,"is"),(166,"fit"),(168,"for the"),(169,"kingdom"),(170,"of God.”")]),
]
