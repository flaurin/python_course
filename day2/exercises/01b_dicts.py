# -*- coding: utf-8 -*-

""" ÖVNING
"""

stockholm = {
    'unemployment_2009': 4.0,
    'unemployment_2014': 5.1
}

solna = {
    'unemployment_2009': 2.7,
    'unemployment_2014': 4.1
}


""" Hur många procentenheter har arbetslösheten stigit i Stockholm?
"""
increase=(stockholm ["unemployment_2014"] - stockholm ["unemployment_2009"])
print ("I Stockholm har de arbetslösa blivit %s procentenheter fler." % increase)


""" Hur många procentenheter har arbetslösheten stigit i Solna?"""

increase2=(solna ["unemployment_2014"] - solna ["unemployment_2009"])
print ("I Solna har de arbetslösa blivit %s procentenheter fler." % increase2)



""" Hur mycket högra arbetslöshet hade Stockholm än Solna 2014?
"""
increase3=(stockholm ["unemployment_2014"] - solna ["unemployment_2014"])
print ("I Stockholm har de arbetslösa blivit %s procentenhet fler än i Solna." % increase3)
