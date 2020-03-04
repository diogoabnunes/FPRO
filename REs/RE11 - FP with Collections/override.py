# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 15:38:20 2018

@author: diogo
"""

def override(l1,l2):
    result = l2 + list(filter(lambda x: x[0] not in {i[0] for i in l2},l1))
    
    return sorted(sorted(result,key = lambda x: x[1]),key = lambda x: x[0])


print(override([('c','d'),('c','e'),('a','b'),('a', 'd')],
                [('a','c'),('b','d')]))

print(override([('a','b','c','e'),('f', 'p', 'r', 'o')],
                [('a','c'),('b','d')]))

print(override([('a','b'),('c','d')],
                [('b','a'),('d','c')]))