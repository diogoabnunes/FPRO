# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 18:47:07 2019

@author: diogo
"""

def compatible(A,B):
    cond = len(A[0]) == len(B)
    if cond: return "A and B can be multiplied"
    else: return AssertionError("A and B cannot be multiplied")

print(compatible([[2,2], [1,1]], [[5,5,5,5], [5,5,5,5]]))
print(compatible([[1,2,2], [1,2,2]], [[1,2,3,4], [1,2,3,4]]))