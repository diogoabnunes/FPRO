# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 10:40:29 2018

@author: diogo
"""

def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-1)+fib(n-2)

print(fib(10))