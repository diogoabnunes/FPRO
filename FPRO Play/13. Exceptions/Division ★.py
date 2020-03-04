# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 11:58:26 2019

@author: diogo
"""

def division(a,b):
    try:
        return f"{a}/{b} = {a/b}"
    except Exception as e:
        if b == 0: return "can't divide by 0!"
        if b != int or a != int: 
            raise e
            return "unsupported operand type(s) for division"

#print(division(10,2))
#print(division(10,0))
print(division(10,b))