# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 15:37:39 2018

@author: diogo
"""

def sort_by_f(l):
    return sorted(l, key= lambda x: 5-x if x>=5 else x) 
    
print(sort_by_f([-10, -6, 2, 5, 90]))
print(sort_by_f([-1, -2, 2, 15, 99]))