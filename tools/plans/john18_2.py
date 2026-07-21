# -*- coding: utf-8 -*-
# John 18 §2 — What Is Truth?
# DOCTRINE: keeps 18:36 "My kingdom is not of this world... but now my
# kingdom is not from here"; 18:37 "You say that I am a king. For this I
# have been born... to testify to the truth. Everyone who is of the truth
# hears my voice."
CHAPTER = "John 18"
SECTION = 2
BLOCKS = [
    # Then they lead Jesus from Caiaphas to the praetorium; now it was early morning.  (fold two articles)
    (0, 13, [(1,"Then"),(0,"they lead"),(2,""),(3,"Jesus"),(4,"from"),(5,""),(6,"Caiaphas"),(7,"to"),(8,"the"),(9,"praetorium;"),(11,"now"),(10,"it was"),(12,"early morning.")]),
    # So Pilate went out to them outside and says, "What accusation do you bring against this man?"  (fold articles)
    (27, 43, [(28,"So"),(29,""),(30,"Pilate"),(27,"went out"),(31,"outside"),(32,"to"),(33,"them,"),(34,"and"),(35,"says,"),(36,"“What"),(37,"accusation"),(38,"do you bring"),(39,"against"),(40,""),(42,"this"),(41,"man?”")]),
    # "If this man were not doing evil, we would not have handed him over to you."
    (47, 57, [(47,"“If"),(50,"this man"),(49,"were"),(48,"not"),(52,"doing"),(51,"evil,"),(53,"we would not"),(55,"have handed"),(56,"him over"),(54,"to you.”")]),
    # So Pilate said to them, "Take him yourselves and judge him according to your law."  (fold articles)
    (57, 72, [(58,"So"),(60,""),(61,"Pilate"),(57,"said"),(59,"to them,"),(62,"“Take"),(63,"him"),(64,"yourselves"),(65,"and"),(70,"judge"),(71,"him"),(66,"according to"),(67,""),(69,"your"),(68,"law.”")]),
    # The Jews said to him,
    (72, 76, [(74,"The"),(75,"Jews"),(72,"said"),(73,"to him,")]),
    # So Pilate entered again into the praetorium and called Jesus and said to him, "Are you the King of the Jews?"  (fold em-dashes)
    (94, 115, [(95,"So"),(100,""),(101,"Pilate"),(94,"entered"),(96,"again"),(97,"into"),(98,"the"),(99,"praetorium"),(102,"and"),(103,"called"),(104,""),(105,"Jesus"),(106,"and"),(107,"said"),(108,"to him,"),(109,"“Are"),(110,"you"),(111,"the"),(112,"King"),(113,"of the"),(114,"Jews?”")]),
    # Jesus answered,
    (115, 117, [(116,"Jesus"),(115,"answered,")]),
    # "From yourself do you say this,
    (117, 122, [(117,"“From"),(118,"yourself"),(119,"do you"),(121,"say"),(120,"this,")]),
    # Pilate answered, "I am not a Jew? Your own nation and the chief priests handed you over to me. What have you done?"  (fold em-dash + articles)
    (128, 147, [(129,""),(130,"Pilate"),(128,"answered,"),(132,"“I"),(134,"am"),(131,"not"),(133,"a Jew?"),(138,"Your own"),(136,"nation"),(135,""),(137,""),(139,"and"),(140,"the"),(141,"chief priests"),(142,"handed"),(143,"you over"),(144,"to me."),(145,"What"),(146,"have you done?”")]),
    # Jesus answered, "My kingdom is not of this world. If my kingdom were of this world, my servants would be fighting, so that I should not be handed over to the Jews. But now my kingdom is not from here."  (fold articles)
    (147, 185, [(148,"Jesus"),(147,"answered,"),(152,"“My"),(150,"kingdom"),(149,""),(151,""),(153,"is not"),(154,"of"),(155,""),(157,"this"),(156,"world."),(158,"If"),(167,"my"),(165,"kingdom"),(164,""),(166,""),(163,"were"),(159,"of"),(160,""),(162,"this"),(161,"world,"),(171,"my"),(169,"servants"),(168,""),(170,""),(172,"would be fighting"),(173,"so that"),(174,"I should not"),(175,"be handed over"),(176,"to the"),(177,"Jews."),(178,"But now"),(182,"my"),(180,"kingdom"),(179,""),(181,""),(183,"is not"),(184,"from here.”")]),
    # So Pilate said to him, "So then, you are a king?"  (fold em-dash)
    (185, 194, [(186,"So"),(188,""),(189,"Pilate"),(185,"said"),(187,"to him,"),(190,"“So then,"),(193,"you"),(192,"are"),(191,"a king?”")]),
    # Jesus answered, "You say that I am a king. For this I have been born, and for this I have come into the world: so that I might testify to the truth. Everyone who is of the truth hears my voice."  (fold em-dash + articles)
    (194, 227, [(196,"Jesus"),(194,"answered,"),(195,""),(197,"“You"),(198,"say"),(199,"that"),(201,"I am"),(200,"a king."),(203,"For"),(204,"this"),(202,"I"),(205,"have been born,"),(206,"and"),(207,"for"),(208,"this"),(209,"I have come"),(210,"into"),(211,"the"),(212,"world:"),(213,"so that"),(214,"I might testify"),(215,"to the"),(216,"truth."),(217,"Everyone"),(218,""),(219,"who is"),(220,"of"),(221,"the"),(222,"truth"),(223,"hears"),(224,"my"),(225,""),(226,"voice.”")]),
    # Pilate says to him, "What is truth?"  (fold em-dash)
    (227, 234, [(229,""),(230,"Pilate"),(227,"says"),(228,"to him,"),(231,"“What"),(232,"is"),(233,"truth?”")]),
    # And having said this, he went out again to the Jews and says to them, "I find no charge in him.
    (234, 251, [(234,"And"),(236,"having said"),(235,"this,"),(238,"he went out"),(237,"again"),(239,"to"),(240,"the"),(241,"Jews"),(242,"and"),(243,"says"),(244,"to them,"),(245,"“I"),(247,"find"),(246,"no"),(250,"charge"),(248,"in"),(249,"him.")]),
    # Now there is a custom for you that I should release one for you at the Passover.
    (251, 262, [(252,"Now"),(251,"there is"),(253,"a custom"),(254,"for you,"),(255,"that"),(257,"I should release"),(256,"one"),(258,"for you"),(259,"at"),(260,"the"),(261,"Passover.")]),
    # So do you want that I release for you the King of the Jews?"
    (262, 270, [(263,"So"),(262,"do you want"),(264,"that I release"),(265,"for you"),(266,"the"),(267,"King"),(268,"of the"),(269,"Jews?”")]),
    # So they shouted again, saying, "Not this man, but Barabbas!"  (fold em-dash)
    (270, 279, [(271,"So"),(270,"they shouted"),(272,"again,"),(273,"saying,"),(274,"“Not"),(275,"this man,"),(276,"but"),(277,""),(278,"Barabbas!”")]),
    # Now Barabbas was a robber.  (fold em-dash)
    (279, 284, [(280,"Now"),(281,""),(282,"Barabbas"),(279,"was"),(283,"a robber.")]),
]
