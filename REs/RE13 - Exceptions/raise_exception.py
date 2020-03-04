# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 18:47:22 2019

@author: diogo
"""

def raise_exception(alist,value):
    result = []
    f = lambda x: x > value
    for elem in alist:
        if f(elem) == False:
            result.append(ValueError(f"{elem} is not greater than {value}"))
    return result

print(raise_exception([1, -2, 3, 0], 3))
print(raise_exception([3], 2))