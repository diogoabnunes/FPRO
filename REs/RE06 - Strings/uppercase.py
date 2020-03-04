# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 23:03:14 2018

@author: diogo
"""

def uppercase (astring):
    astring_up = astring.upper()
    for i in range(3):
        if astring[i].isupper():
            astring = astring_up
            break
    return astring

print(uppercase("gin tonic"))
print(uppercase("Gin tonic"))
print(uppercase("...tonic..."))
print(uppercase("Καλημέρα"))