# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 16:16:59 2018

@author: diogo
"""

def fib(n):
    result = []
    a = 0
    b = 1
    for i in range(n):  
        result.append(a)
        a,b = b,a+b
    if n == 1:
        result = [0]
    return result

print(fib(0))
print(fib(1))
print(fib(5))