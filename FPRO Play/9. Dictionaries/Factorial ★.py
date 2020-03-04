# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 16:38:24 2018

@author: diogo
"""

def factorial(n):
    if n == 0: return 1
    if n == 1: return 1
    return n*factorial(n-1)

print(factorial(5))