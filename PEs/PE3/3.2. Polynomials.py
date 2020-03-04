# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 17:07:56 2019

@author: diogo
"""

def evaluate(a,x):
    xi = [x**e for e in range(len(a))]
    axi = [a[i]*xi[i] for i in range(len(a))]
    return sum(axi)

print(evaluate([1, 2, 4], 5)) #111
print(evaluate([1, 2, 4], 10)) #421
print(evaluate([1, 2, 4, 6, 8], 2)) #197