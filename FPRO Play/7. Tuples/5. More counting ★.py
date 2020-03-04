# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 15:47:48 2018

@author: diogo
"""

def count_elems(tup):
    result = []
    tup = list(tup)
    for i in range(len(tup)):
        if type(tup[i]) == tuple or type(tup[i]) == list:
            result.append(len(tup[i]))
            continue
        if type(tup[i]) == str:
            result.append(len(tup[i]))
            continue
        else:
            result.append(1)
    result = tuple(result)
    return result

print(count_elems((1,'234', 3, 4.0, (5j,))))
print(count_elems(('12',2,(3, 4), [4.0, 'str', 'str2'], 5j)))