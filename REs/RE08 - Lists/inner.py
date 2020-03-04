# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 14:28:18 2018

@author: diogo
"""

def inner(u,v):
#    result = 0
#    for i in range(len(u)):
#        part_result = u[i]*v[i]
#        result = result + part_result
#    return result
    return sum([u[i]*v[i] for i in range(len(u))])

print(inner([],[]))
print(inner([1,2],[2,4]))
print(inner([1,2,3,4,5],[2,3,4,5,6]))