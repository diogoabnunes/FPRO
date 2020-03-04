# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 15:40:51 2018

@author: diogo
"""

def count_until(tup):
    sum = 0
    for i in range(len(tup)):
        if type(tup[i]) == tuple:
            break
        else:
            sum += 1
    if sum == len(tup):
        sum = -1
    result = sum
    return result

print(count_until((1,'2', 3, 4.0, 5j)))
print(count_until((1,2,(3,), 4.0, 5j)))