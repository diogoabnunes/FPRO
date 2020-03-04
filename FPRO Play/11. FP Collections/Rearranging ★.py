# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 11:09:33 2018

@author: diogo
"""

def rearrange(l):
    neg = [elem for elem in l if elem <= 0]
    pos = [elem for elem in l if elem > 0]
    return neg + pos

print(rearrange([12, 11, -13, -5, 6, -7, 5, -3, -6, 0]))
print(rearrange([-19, -15, -14, -9, -18, -1, -4]))