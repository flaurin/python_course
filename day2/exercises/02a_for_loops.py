# -*- coding: utf-8 -*-


unicorns = [
    "Joachim Kerpner",
    "Nina Svanberg",
    "Johan Ronge",
    "Christian Holmén",
    "Fredrik Laurin",
    "Olle Carlsson",
    "Lolo Tode Palm",
    "Martin Jönsson"
]

"""
ÖVNING:
Gör en for-loop som skriver ut en numrerad deltagarlista.
1. Joachim Kerpner
2. Nina Svanberg
o.s.v.
"""

counter = 1
print("Nu börjar programmet! Vi sätter räknaren på 1.")
print("Nu körs loopen")
for unicorn in unicorns:
    if counter==1:
        print "Detta är första gången den körs och enda gången den visas"
    print "%s. %s" % (counter, unicorn)
    
    counter=counter+1
    
