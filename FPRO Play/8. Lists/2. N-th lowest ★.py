# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 16:16:22 2018

@author: diogo
"""

def nth_lowest(lnum,n):
    lnum = sorted(lnum)
    result = lnum[n-1]
    return result

print(nth_lowest([42, 234, 135, 21, 232, 12312, -2343],2))
print(nth_lowest([73,100,23,18,84,61,56,75,92,38,54,73,3,13],12))