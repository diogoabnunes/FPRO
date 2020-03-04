# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 20:44:39 2018

@author: diogo
"""
import math

def pascal(n):
    result = ""
    
    def combinations(r,n):
        comb = int(math.factorial(n)/(math.factorial(n-r)*math.factorial(r)))
        return comb
    
    for i in range(n):
        for r in range(i+1):
            result += str(combinations(r,i)) + " "
        result += "\n"
    return result

print(pascal(3))
print()
print(pascal(5))