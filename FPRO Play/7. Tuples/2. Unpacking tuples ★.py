# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 15:35:39 2018

@author: diogo
"""

def unpack_rev(atuple):
    atuple = list(atuple)
    atuple = atuple[::-1]
    result = ""
    for i in range(len(atuple)):
        result += str(atuple[i]) + " "
    return result

print(unpack_rev(("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")))