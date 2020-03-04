# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 17:24:40 2019

@author: diogo
"""

def interleave(alist1,alist2):
    if type(alist1) != list: return [alist1,alist2]
    result = []
    for i,j in zip(alist1,alist2): result += interleave(i,j)
    return result

print(interleave([1, [4,2]], [3, [7,4]])) #[1,3,4,7,2,4]
print(interleave(['a','b','c'], [1,2,3,4,5])) #['a',1,'b',2,'c',3]
print(interleave([], [1,2])) #[]