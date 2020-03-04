# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 15:29:44 2018

@author: diogo
"""

def add_item(tup,idx,item):
    tup = list(tup)
    if idx == 0 or idx == len(tup)-1:
        tup[idx] = item
    else:
        tup.insert(idx,item)
    result = tuple(tup)
    return result

print(add_item((1,2,3),1,[4,5]))
print(add_item(("a",2,"c"),2,"new item"))