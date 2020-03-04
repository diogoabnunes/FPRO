# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 22:24:17 2018

@author: diogo
"""

def sparse_dot_product(dict1,dict2):
    result = 0
    for key,value in dict1.items():
        if key in dict2:
            result += dict2[key]*value       
    return result

print(sparse_dot_product({1: 3, 7: 1}, {1: 3, 7: 1}))
print(sparse_dot_product({0: 1, 1: 1}, {2: 1, 3: 1}))