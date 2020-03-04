# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 21:30:03 2019

@author: diogo
"""

def ackermann(m,n):
    if m == 0: return n+1
    if m > 0 and n == 0: return ackermann(m-1,1)
    else: return ackermann(m-1,ackermann(m,n-1))

print(ackermann(0, 0)) #1
print(ackermann(2, 1)) #5
print(ackermann(3, 4)) #125
print()
print(ackermann(3, 5)) #253
print(ackermann(3, 6)) #509
print(ackermann(3, 3)) #61
print(ackermann(2, 7)) #17