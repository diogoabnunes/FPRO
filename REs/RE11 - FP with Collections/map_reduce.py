# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 15:37:58 2018

@author: diogo
"""

from functools import reduce

def map_reduce(n1,n2):
    alist = [i**2 for i in range(n1,n2) if i%2 == 1]
    return reduce((lambda x,y: x*y if x*y<50 else x+y),alist)

print(map_reduce(0, 10))
print(map_reduce(5, 100))