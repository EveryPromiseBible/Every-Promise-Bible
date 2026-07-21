# -*- coding: utf-8 -*-
# Romans 15 §3 read: "...and made sure they've received this fruit, them I'll go
# on by way of you to Spain." The bare "them" is αὐτοῖς left standing in Greek
# position (σφραγισάμενος αὐτοῖς τὸν καρπὸν τοῦτον), and it lands between two
# clauses where a reader can only read it as an object of "go on".
#
# Underneath it was also a small drift: αὐτοῖς is a dative pronoun, but its
# sense ("they") had been absorbed into σφραγισάμενος's gloss "made sure they've
# received", leaving αὐτοῖς itself with a homeless "them".
#
# Fix, within [74,78): σφραγισάμενος takes the verb alone — "safely delivered",
# which is its ordinary sense here (to seal/secure a delivery, cf. ESV
# "delivered to them what has been collected") — and αὐτοῖς is moved to the end
# of its own phrase as the dative it is, "to them,". The comma before the main
# clause is preserved.
#
# Result: "...and safely delivered this fruit to them, I'll go on by way of you
# to Spain."
CHAPTER = "Romans 15"
SECTION = 3
BLOCKS = [
    (74, 78, [
        (74, "safely delivered"),  # σφραγισάμενος
        (75, None),                # τοῦτον — "this"
        (76, "fruit"),             # τὸν καρπὸν — was "fruit,"; the comma now
                                   # belongs on αὐτοῖς, which ends the phrase

        (77, "to them,"),          # αὐτοῖς
    ]),
]
