# -*- coding: utf-8 -*-
# John 13 §3 — A New Commandment
# DOCTRINE: keeps 13:31-32 "Now the Son of Man has been glorified, and God
# has been glorified in him... God will glorify him in himself"; 13:34 "A
# new commandment I give you, that you love one another"; 13:35 "By this
# all will know that you are my disciples."
CHAPTER = "John 13"
SECTION = 3
BLOCKS = [
    # Jesus says,
    (3, 5, [(4,"Jesus"),(3,"says,")]),
    # "Now the Son of Man has been glorified,
    (5, 11, [(5,"“Now"),(7,"the"),(8,"Son"),(9,"of"),(10,"Man"),(6,"has been glorified,")]),
    # and God has been glorified in him.  (fold em-dash placeholder)
    (11, 17, [(11,"and"),(12,""),(13,"God"),(14,"has been glorified"),(15,"in"),(16,"him.")]),
    # If God has been glorified in him,  (fold em-dash placeholder)
    (17, 23, [(17,"If"),(18,""),(19,"God"),(20,"has been glorified"),(21,"in"),(22,"him,")]),
    # God will also glorify him in himself—  (fold em-dash placeholder)
    (23, 30, [(25,"God"),(24,""),(23,"will also"),(26,"glorify"),(27,"him"),(28,"in"),(29,"himself—")]),
    # Little children, still a little while I am with you.
    (34, 40, [(34,"Little children,"),(35,"still"),(36,"a little while"),(39,"I am"),(37,"with"),(38,"you.")]),
    # A new commandment I give you—
    (58, 62, [(59,"A new"),(58,"commandment"),(60,"I give"),(61,"you—")]),
    # By this all will know that you are my disciples—
    (73, 81, [(73,"By"),(74,"this"),(76,"all"),(75,"will know"),(77,"that"),(80,"you are"),(78,"my"),(79,"disciples—")]),
    # if you have love among one another.
    (81, 86, [(81,"if"),(83,"you have"),(82,"love"),(84,"among"),(85,"one another.”")]),
    # Simon Peter says to him,
    (86, 90, [(88,"Simon"),(89,"Peter"),(86,"says"),(87,"to him,")]),
    # Jesus answered,
    (93, 95, [(94,"Jesus"),(93,"answered,")]),
    # you cannot follow me now—
    (97,101,[(97,"you cannot"),(100,"follow"),(98,"me"),(99,"now—")]),
    # Peter says to him,  (fold em-dash placeholder)
    (103,107,[(106,"Peter"),(105,""),(103,"says"),(104,"to him,")]),
    # why can I not follow you now?
    (108,113,[(108,"why"),(109,"can I not"),(111,"follow"),(110,"you"),(112,"now?")]),
    # I will lay down my life for you!  (fold article)
    (113,119,[(118,"I will lay down"),(115,"my"),(114,"life"),(113,""),(116,"for"),(117,"you!”")]),
    # Jesus answers,
    (119,121,[(120,"Jesus"),(119,"answers,")]),
    # "Will you lay down your life for me?  (fold article)
    (121,127,[(126,"“Will you lay down"),(123,"your"),(122,"life"),(121,""),(124,"for"),(125,"me?")]),
    # a rooster will certainly not crow
    (131,134,[(132,"a rooster"),(131,"will certainly not"),(133,"crow")]),
]
