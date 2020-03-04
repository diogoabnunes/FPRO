# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 21:28:07 2019

@author: diogo
"""

def gcd(a,b):
    if b == 0: return a
    c = a % b
    if c == 0: return b
    else: return gcd(b,c)

print(gcd(25, 5)) #5
print(gcd(21, 14)) #7
print(gcd(65, 26)) #13
print()
print(gcd(17, 3)) #1
print(gcd(1122, 17)) #17
print(gcd(50, 1)) #1
print(gcd(50, 0)) #50