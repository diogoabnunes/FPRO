# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 15:20:19 2018

@author: diogo
"""

def dogs(h_age):

    if h_age <=2:
        dog_age = h_age*10.5
    else:
        dog_age = 21 + (h_age-2)*4
    
    return dog_age

print(dogs(0))
print(dogs(1))
print(dogs(2))
print(dogs(3))
print(dogs(10))