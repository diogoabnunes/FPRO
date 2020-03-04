# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 14:39:10 2018

@author: diogo
"""

def most_frequent(alist):
    dic = {}
    alist.sort()
    for elem in alist:
        dic[elem] = dic.get(elem,0)+1
    dic = list(dic.items())
    max_k = 0
    max_v = 0
    for k,v in dic:
        if v > max_v:
            max_v = v
            max_k = k
        if v == max_v:
            max_k = max([k,max_k])
    return max_k

print(most_frequent([-1, 2, 5, -1, 3, 3, 3, 4, 4, 2, 4, 5, -1, -1]))
print(most_frequent([-1, 111, 1, 11, -1, 11, 1, 111]))