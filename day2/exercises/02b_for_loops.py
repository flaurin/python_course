# -*- coding: utf-8 -*-


namnlistan = [
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
Använd funktionen len(), som funkar på både strängar och listor,
och räkna ut hur många deltagare som har långa respektive korta namn.
"""

long_names = 0
short_names = 0
total_unicorns = len(namnlistan)

print("Nu börjar programmet! Låt oss räkna långa och korta namn.")
for namn in namnlistan:
    """ Skriv kod med en IF-sats här!"""
    name_length = len(namn)
    print(namn, name_length)
    if len(namn)>11:
    	long_names=long_names+1


    if len(namn)<12:
    	short_names=short_names+1

print("%s av %s enhörningar har långa namn." % (long_names, total_unicorns))
print("%s av %s enhörningar har korta namn" % (short_names, total_unicorns))
