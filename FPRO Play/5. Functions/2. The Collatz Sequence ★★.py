# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 21:07:41 2018

@author: diogo
"""

def collatz(n):
    result = n 
    i = 0
    while n != 1:
        if (n % 2) == 0:
            n = n // 2
        else:
            n = 3*n + 1
        result = str(result) + "," + str(n)
        i = i+1
        
    return result

print(collatz(3))
print(collatz(12))