# -*- coding: utf-8 -*-
# John 19 §0 — Behold the Man
# DOCTRINE: keeps 19:7 "he made himself the Son of God"; 19:11 "You would
# have no authority against me unless it were given you from above";
# "Behold the man!"; "Behold your King!"
CHAPTER = "John 19"
SECTION = 0
BLOCKS = [
    # Then, therefore, Pilate took Jesus and flogged him.  (fold two em-dashes)
    (0, 9, [(0,"Then"),(1,"therefore,"),(3,""),(4,"Pilate"),(2,"took"),(5,""),(6,"Jesus"),(7,"and"),(8,"flogged him.")]),
    # placed it on his head, and threw a purple garment around him;  (fold article)
    (17, 25, [(17,"on his"),(18,""),(19,"head,"),(20,"and"),(23,"threw"),(22,"a purple"),(21,"garment"),(24,"around him;")]),
    # "Hail, King of the Jews!"  (fold article)
    (31, 36, [(31,"“Hail,"),(32,""),(33,"King"),(34,"of the"),(35,"Jews!”")]),
    # And Pilate went out again outside and says to them,  (fold em-dash)
    (40, 49, [(40,"And"),(44,""),(45,"Pilate"),(41,"went out"),(42,"again"),(43,"outside"),(46,"and"),(47,"says"),(48,"to them,")]),
    # "Look— I bring him out to you,
    (49, 54, [(49,"“Look—"),(50,"I bring"),(52,"him"),(53,"out"),(51,"to you,")]),
    # so that you may know that I find no charge in him."
    (54, 62, [(54,"so that"),(55,"you may know"),(56,"that"),(59,"I find"),(57,"no"),(58,"charge"),(60,"in"),(61,"him.”")]),
    # So Jesus went out outside, wearing the thorny crown and the purple garment.  (fold em-dash)
    (62, 75, [(63,"So"),(64,""),(65,"Jesus"),(62,"went out"),(66,"outside,"),(67,"wearing"),(68,"the"),(69,"thorny"),(70,"crown"),(71,"and"),(72,"the"),(73,"purple"),(74,"garment.")]),
    # So when the chief priests and the officers saw him, they cried out, saying,
    (81, 92, [(82,"So"),(81,"when"),(85,"the"),(86,"chief priests"),(87,"and"),(88,"the"),(89,"officers"),(83,"saw"),(84,"him,"),(90,"they cried out,"),(91,"saying,")]),
    # Pilate says to them, "Take him yourselves and crucify— for I do not find a charge in him."  (fold em-dash)
    (94, 109, [(96,""),(97,"Pilate"),(94,"says"),(95,"to them,"),(98,"“Take"),(99,"him"),(100,"yourselves"),(101,"and"),(102,"crucify—"),(103,"for I"),(104,"do not"),(105,"find"),(108,"a charge"),(106,"in"),(107,"him.”")]),
    # The Jews answered him, "We have a law,
    (109, 116, [(111,"The"),(112,"Jews"),(109,"answered"),(110,"him,"),(113,"“We"),(115,"have"),(114,"a law,")]),
    # because he made himself the Son of God."
    (122, 127, [(122,"because"),(126,"he made"),(125,"himself"),(123,"the Son"),(124,"of God.”")]),
    # So when Pilate heard this word, he was afraid all the more;  (fold em-dash + article)
    (127, 137, [(128,"So"),(127,"when"),(130,""),(131,"Pilate"),(129,"heard"),(132,"this"),(133,""),(134,"word,"),(136,"he was afraid"),(135,"all the more;")]),
    # But Jesus gave him no answer.
    (151, 157, [(151,"But"),(152,"Jesus"),(155,"gave"),(156,"him"),(154,"no"),(153,"answer.")]),
    # So Pilate says to him,  (fold em-dash)
    (157, 162, [(158,"So"),(160,""),(161,"Pilate"),(157,"says"),(159,"to him,")]),
    # "You do not speak to me? Do you not know that I have authority to release you, and I have authority to crucify you?"
    (162, 177, [(163,"“You do not"),(164,"speak"),(162,"to me?"),(165,"Do you not"),(166,"know"),(167,"that"),(169,"I have"),(168,"authority"),(170,"to release"),(171,"you,"),(172,"and"),(174,"I have"),(173,"authority"),(175,"to crucify"),(176,"you?”")]),
    # Jesus answered him,
    (177, 180, [(179,"Jesus"),(177,"answered"),(178,"him,")]),
    # "You would not have any authority against me,
    (180, 185, [(180,"“You would not have"),(184,"any"),(181,"authority"),(182,"against"),(183,"me,")]),
    # Because of this, the one who handed me over to you has greater sin."
    (190, 199, [(190,"Because of"),(191,"this,"),(192,"the one"),(193,"who handed"),(194,"me over"),(195,"to you"),(198,"has"),(196,"greater"),(197,"sin.”")]),
    # From this, Pilate was seeking to release him;  (fold em-dash)
    (199, 206, [(199,"From"),(200,"this,"),(201,""),(202,"Pilate"),(203,"was seeking"),(204,"to release"),(205,"him;")]),
    # "If you release this man,
    (210, 213, [(210,"“If"),(212,"you release"),(211,"this man,")]),
    # Everyone who makes himself a king speaks against Caesar!"  (fold two em-dashes)
    (217, 225, [(217,"Everyone"),(218,"who"),(221,"makes"),(220,"himself"),(219,"a king"),(222,"speaks against"),(223,""),(224,"Caesar!”")]),
    # So Pilate, hearing these words, brought Jesus outside and sat down on a judgment seat at a place called The Stone Pavement, but in Hebrew, Gabbatha.  (fold em-dashes + article)
    (225, 246, [(225,""),(226,"So"),(227,"Pilate,"),(228,"hearing"),(229,""),(231,"these"),(230,"words,"),(232,"brought"),(234,""),(235,"Jesus"),(233,"outside"),(236,"and"),(237,"sat down"),(238,"on"),(239,"a judgment seat"),(240,"at"),(241,"a place"),(242,"called"),(243,"The Stone Pavement,"),(244,"but in Hebrew,"),(245,"Gabbatha.")]),
    # Now it was the Preparation of the Passover; the hour was about the sixth.
    (246, 255, [(247,"Now"),(246,"it was"),(248,"the Preparation"),(249,"of the"),(250,"Passover;"),(251,"the hour"),(252,"was"),(253,"about"),(254,"the sixth.")]),
    # "Look— your King!"  (fold article)
    (259, 263, [(259,"“Look—"),(262,"your"),(260,""),(261,"King!”")]),
    # So they cried out, those men,
    (263, 266, [(264,"So"),(263,"they cried out,"),(265,"those men,")]),
    # Pilate says to them, "Shall I crucify your King?"  (fold em-dash + article)
    (270, 278, [(272,""),(273,"Pilate"),(270,"says"),(271,"to them,"),(277,"“Shall I crucify"),(276,"your"),(274,""),(275,"King?”")]),
    # The chief priests answered,
    (278, 281, [(279,"The"),(280,"chief priests"),(278,"answered,")]),
    # So then he handed him over to them,
    (285, 290, [(285,"So"),(286,"then,"),(287,"he handed"),(288,"him over"),(289,"to them,")]),
    # So they took Jesus.  (fold em-dash)
    (292, 296, [(293,"So"),(292,"they took"),(294,""),(295,"Jesus.")]),
]
