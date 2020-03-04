# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 15:49:41 2019

@author: diogo
"""

def treasure(clues):
    pos = (0,0)
    while pos in clues:
        oldpos = pos
        pos = clues[pos]
        del clues[oldpos]
    return pos

print(treasure({(0,0): (1,0), (1,0): (2,0), (2,0): (3,0)})) #(3,0)
print(treasure({(0,0): (1,0), (2,1): (3,5), (1,0): (2,1)})) #(3,5)
print(treasure({(0,0): (5,6), (7,8): (6,7), (5,6): (6,7), (6,7): (7,8)})) #(6,7)