# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 17:14:43 2019

@author: diogo
"""

def recursive_dot(l1,l2):
    if type(l1) == int: return l1*l2
    if len(l1) == 0: return 0
    return recursive_dot(l1[0],l2[0]) + recursive_dot(l1[1:],l2[1:])

print(recursive_dot([1, [2, 3]], [4, [5, 6]])) #32
print(recursive_dot([[5, 3, 1], [2, 4]], [[4, 2, 0], [1, 3]])) #40
print(recursive_dot([2], [1])) #2