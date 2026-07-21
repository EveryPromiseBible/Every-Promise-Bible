# -*- coding: utf-8 -*-
# John 10 §1 — I Am the Good Shepherd
# DOCTRINE: keeps "I am the good shepherd"; "the good shepherd lays down
# his life for the sheep"; "just as the Father knows me and I know the
# Father"; "I lay down my life so that I may take it again... This command
# I received from my Father."
CHAPTER = "John 10"
SECTION = 1
BLOCKS = [
    # "I am the good shepherd.  (fold article)
    (0, 6, [(0,"“I"),(1,"am"),(2,"the"),(5,"good"),(3,"shepherd."),(4,"")]),
    # The good shepherd lays down his life  (fold two articles)
    (6, 14, [(6,"The"),(9,"good"),(7,"shepherd"),(8,""),(13,"lays down"),(12,"his"),(11,"life"),(10,"")]),
    # whose own the sheep are not,
    (23, 28, [(23,"whose"),(27,"own"),(25,"the"),(26,"sheep"),(24,"are not,")]),
    # because he is a hired hand
    (45, 48, [(45,"because"),(47,"he is"),(46,"a hired hand")]),
    # I am the good shepherd;  (fold article)
    (55, 61, [(55,"I"),(56,"am"),(57,"the"),(60,"good"),(58,"shepherd;"),(59,"")]),
    # and I know my own,  (fold article)
    (61, 65, [(61,"and"),(62,"I know"),(64,"my own,"),(63,"")]),
    # and my own know me—  (fold article)
    (65, 70, [(65,"and"),(69,"my own"),(68,""),(66,"know"),(67,"me—")]),
    # just as the Father knows me
    (70, 75, [(70,"just as"),(73,"the"),(74,"Father"),(71,"knows"),(72,"me")]),
    # and I lay down my life for the sheep.  (fold article)
    (79, 87, [(79,"and"),(83,"I lay down"),(82,"my"),(81,"life"),(80,""),(84,"for"),(85,"the"),(86,"sheep.")]),
    # of this fold;  (fold article)
    (93, 97, [(93,"of"),(96,"this"),(95,"fold;"),(94,"")]),
    # and they will hear my voice—  (fold article)
    (100,105,[(100,"and"),(104,"they will hear"),(103,"my"),(102,"voice—"),(101,"")]),
    # Because of this the Father loves me:
    (111,117,[(111,"Because of"),(112,"this"),(114,"the"),(115,"Father"),(116,"loves"),(113,"me:")]),
    # because I lay down my life so that I may take it again.  (fold article)
    (117,127,[(117,"because"),(118,"I"),(119,"lay down"),(122,"my"),(121,"life"),(120,""),(123,"so that"),(125,"I may take"),(126,"it"),(124,"again.")]),
    # but I lay it down of myself.
    (132,138,[(132,"but"),(133,"I"),(134,"lay"),(135,"it down"),(136,"of"),(137,"myself.")]),
    # Authority I have to lay it down,
    (138,142,[(138,"Authority"),(139,"I have"),(140,"to lay"),(141,"it down,")]),
    # and authority I have to take it again.
    (142,148,[(142,"and"),(143,"authority"),(144,"I have"),(146,"to take"),(147,"it"),(145,"again.")]),
    # This command I received from my Father.  (fold two articles)
    (148,156,[(148,"This"),(150,"command"),(149,""),(151,"I received"),(152,"from"),(155,"my"),(154,"Father.”"),(153,"")]),
    # because of these words.  (fold article)
    (162,166,[(162,"because of"),(165,"these"),(164,"words."),(163,"")]),
    # Now many of them were saying,
    (166,171,[(167,"Now"),(168,"many"),(169,"of"),(170,"them"),(166,"were saying,")]),
    # "He has a demon,
    (171,173,[(172,"“He has"),(171,"a demon,")]),
    # Why do you listen to him?
    (175,178,[(175,"Why"),(177,"do you listen to"),(176,"him?”")]),
    # "These are not the words of one demon-possessed.
    (180,185,[(180,"“These"),(183,"are not"),(181,"the"),(182,"words"),(184,"of one demon-possessed.")]),
    # Surely a demon is not able to open the eyes of blind people?
    (185,191,[(185,"Surely"),(186,"a demon"),(187,"is not able"),(190,"to open"),(189,"the eyes"),(188,"of blind people?”")]),
]
