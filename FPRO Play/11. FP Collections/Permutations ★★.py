# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 18:17:59 2018

@author: diogo
"""

from itertools import permutations

def permuta(alist, step=0):
    return list(permutations(alist))

print(permuta(['Joe', 'Mary', 'John']))