# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 21:33:20 2019

@author: diogo
"""

def maximum_depth(lst):
    if lst == []: return 1
    maxd = 0
    for i in lst:
        d = maximum_depth(i)
        if d > maxd:
            maxd = d
    return maxd + 1


print(maximum_depth([[], [[]], [], [[]]])) #3
print(maximum_depth([[[], [], [[]]], [[]], [], [[]]])) #4
print(maximum_depth([[[], [], [[]]], [[[[]]]]])) #5
print()
print(maximum_depth([[], [[], [[[[[]]], []]], [[]]]]))
#7
print(maximum_depth([[[], []], [], [[[], [], [], [[[]]]], []]]))
#6
print(maximum_depth([[]])) #2
print(maximum_depth([[[[[[[[[[[[[]]]]]]]]]]]]])) #13