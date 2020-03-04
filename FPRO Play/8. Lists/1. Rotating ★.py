# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 16:16:07 2018

@author: diogo
"""

def rotate_list(l):
    result = []
    if len(l) >= 3:
        for i in range(3,len(l)):
            result.append(l[i])
        for k in range(3):
            result.append(l[k])
    return result

print(rotate_list([1,2,3,4,5,6]))
print(rotate_list([5,20,21,0,-1,3]))