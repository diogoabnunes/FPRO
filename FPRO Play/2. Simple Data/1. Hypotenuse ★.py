# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 14:49:53 2018

@author: diogo
"""
import math

def hypotenuse(n):
    hypo = math.sqrt((n**2)+(n**2))
    result = "{:.2f}".format(hypo)
    return result

print(hypotenuse(2))
print(hypotenuse(6))