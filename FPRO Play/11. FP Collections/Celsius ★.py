# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 10:55:57 2018

@author: diogo
"""

def to_celsius(t):
    f = lambda x: round(((x-32)/1.8),2)
    result = list(map(f,t))
    return result
    
print(to_celsius([84.56, 79.7, 81.14, 82.4, 82.04]))
print(to_celsius([23.0, 28.4, 32.0, 35.6]))