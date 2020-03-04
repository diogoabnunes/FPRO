# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 22:24:31 2018

@author: diogo
"""

def roman_to_integer(astring):
    astring = list(astring)
    astring.append(" ")
#    print(astring)
    result = 0
    roman_integer = {}
    roman_integer["M"] = 1000
    roman_integer["D"] = 500
    roman_integer["C"] = 100
    roman_integer["L"] = 50
    roman_integer["X"] = 10
    roman_integer["V"] = 5
    roman_integer["I"] = 1
    roman_integer[" "] = 0
    
    for i in range(len(astring)-1):
        if int(roman_integer[astring[i]]) >= int(roman_integer[astring[i+1]]):
            result = result + roman_integer[astring[i]]

        else:
            result = result - roman_integer[astring[i]]            
    
    return result

print(roman_to_integer('LXXXIV'))
print(roman_to_integer('XLIII'))
print(roman_to_integer('MMMCMXCIX'))