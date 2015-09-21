# -*- coding: utf-8 -*-

""" Se robot_writer.md för instruktioner
"""
kommun = "Säffle"
total_unemployment_2009 = 5.9
total_unemployment_2014 = 8.0

def write_story(municipality, unemployment_2009, unemployment_2014):
    change = unemployment_2014-unemployment_2009
    print("Dateline: %s/Ekot" % (municipality))
    
    print("Arbetslösheten i landet utvecklas helt enligt de mest begåvade pognoserna. I till exempel %s har arbetslösheten ändrats med %s procentenheter de senaste åren."% (municipality, change))
write_story(kommun, total_unemployment_2014, total_unemployment_2009)

"""
    # Skriv kod här!
    *********************


write_story("Stockholm", 7.1, 6.6) 
print("**************")

write_story("Kiruna", 7.6, 4.2) 
print("**************")

write_story("Lessebo", 9.5, 13.2) 
print("**************")


Källa: http://www.ekonomifakta.se/sv/Fakta/Regional-statistik/Din-kommun-i-siffror/
"""