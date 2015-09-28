# -*- coding: utf-8 -*-

"""
ÖVNING
Gör en funktion som tar en arbetslöshetsprocent och kategoriserar den
som "låg", "medel" eller "hög" med hjälp av IF-satser.
Använd IF-satser
"""


def categorize_unemployment(unemployment):
	if unemployment < 5.0:
		return "låg"
	if unemployment > 5.0 and unemployment < 7:
		return "medel"
	if unemployment > 7:
		return "hög"

print(categorize_unemployment(1.2))
print(categorize_unemployment(10.3))
print(categorize_unemployment(7.8))
print(categorize_unemployment(5.6))
print(categorize_unemployment(2.1))
