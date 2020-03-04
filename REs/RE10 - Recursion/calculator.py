# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 11:21:28 2018

@author: diogo
"""

def calculator(expr):
    if type(expr) == int:
        return expr
    a = calculator(expr[0])
    b = calculator(expr[2])
    if expr[1] == "+": return a+b
    if expr[1] == "-": return a-b
    if expr[1] == "*": return a*b

print(calculator((1, '+', 2)))
print(calculator(((1, '+', 2), '*', 3)))