# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 11:12:57 2018

@author: diogo
"""

from functools import reduce

def map_filter_reduce(lst,f1,f2,f3):
    r1 = list(filter(f1,lst))
    r2 = list(map(f2,r1))
    r3 = reduce(f3,r2)
    return r3

print(map_filter_reduce([1, 2, 3, 4, 5, 6, 7, 8],
                        lambda i: i % 2 == 0,
                        lambda i: i**2,
                        lambda a, b: a+b))