# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 15:38:09 2018

@author: diogo
"""

def odd_range(start,stop,step):
    
    if start % 2 == 0:
        start += 1
    result = [i for i in range(start,stop,2*step) if i % 2 != 0]
    for i in result:
        yield i

print(odd_range(1, 10, 1))
print(odd_range(100, 150, 5))
print(odd_range(0,20,2))
print(odd_range(3,35,10))