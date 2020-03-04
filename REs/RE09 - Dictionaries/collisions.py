# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 22:23:40 2018

@author: diogo
"""

def collisions(list):
    dic = {}
    
    for elem in list:
        sum_elem = 0
        for i in str(elem):
            sum_elem += int(i)
        hash_elem = sum_elem % 8
        dic[hash_elem] = dic.get(hash_elem,0) + 1      
    return dic

print(collisions([24,42]))
print(collisions([1,789,100,9807,1208,92,101]))