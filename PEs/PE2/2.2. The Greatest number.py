# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 14:37:03 2018

@author: diogo
"""

#2. The greatest number

#Write a Python function greatest(num) that, given a non-negative integer num , computes the
#greatest number that can be made using all digits of num .

#For example:
#● greatest(310909) returns the integer: 993100
#● greatest(7187) returns the integer: 8771
#● greatest(99) returns the integer: 99

def greatest(num):
    return "".join(sorted(str(num)))[::-1]

print(greatest(310909))
print()
print(greatest(7187))
print()
print(greatest(99))