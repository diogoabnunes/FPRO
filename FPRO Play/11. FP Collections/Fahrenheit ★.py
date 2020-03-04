# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 11:04:17 2018

@author: diogo
"""

def to_fahrenheit(t):
    f = lambda x: round(((x*1.8) + 32),2)
    result = list(map(f,t))
    return result

print(to_fahrenheit([29.2, 26.5, 27.3, 28, 27.8]))
print(to_fahrenheit([-5, -2, 0, 2]))