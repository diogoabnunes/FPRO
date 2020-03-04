# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 14:09:03 2018

@author: diogo
"""

def f(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

print(f(4))
print(f(5))