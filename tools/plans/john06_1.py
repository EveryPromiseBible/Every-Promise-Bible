# -*- coding: utf-8 -*-
# John 6 §1 — It Is I, Do Not Be Afraid
# Keeps "I am—" (ἐγώ εἰμι) literal, preserving the double sense.
CHAPTER = "John 6"
SECTION = 1
BLOCKS = [
    # Now when evening came,
    (0, 4, [(1,"Now"),(0,"when"),(2,"evening"),(3,"came,")]),
    # his disciples went down to the sea,  (fold article)
    (4, 11, [(7,"his"),(6,"disciples"),(5,""),(4,"went down"),(8,"to"),(9,"the"),(10,"sea,")]),
    # and Jesus had not yet come to them.  (fold em-dash placeholder)
    (25, 32, [(25,"and"),(31,"Jesus"),(30,""),(26,"had not yet"),(27,"come"),(28,"to"),(29,"them.")]),
    # The sea was being stirred up by a great wind blowing.
    (32, 38, [(32,"The"),(33,"sea"),(37,"was being stirred up"),(35,"by a great"),(34,"wind"),(36,"blowing.")]),
    # Then, having rowed about twenty-five or thirty stadia,  (join number)
    (38, 46, [(39,"Then,"),(38,"having rowed"),(40,"about"),(42,"twenty-five"),(43,""),(44,"or"),(45,"thirty"),(41,"stadia,")]),
    # they see Jesus walking on the sea and coming near the boat—  (fold em-dash placeholder)
    (46, 58, [(46,"they see"),(47,""),(48,"Jesus"),(49,"walking"),(50,"on"),(51,"the"),(52,"sea"),(53,"and"),(57,"coming"),(54,"near"),(55,"the"),(56,"boat—")]),
    # Then they were willing
    (67, 69, [(68,"Then"),(67,"they were willing")]),
    # the boat was at the land
    (76, 82, [(77,"the"),(78,"boat"),(76,"was"),(79,"at"),(80,"the"),(81,"land")]),
]
