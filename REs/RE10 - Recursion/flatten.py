# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 11:21:03 2018

@author: diogo
"""

def flatten(alist):
    if alist == []:
        return []
    if type(alist[0]) == list:
        return flatten(alist[0]) + flatten(alist[1:])
    return alist[:1] + flatten(alist[1:])

print(flatten(['Hello', [2, [[], False]], [True]]))
print(flatten([[]]))