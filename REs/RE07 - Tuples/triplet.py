# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 00:08:38 2018

@author: diogo
"""

def triplet(atuple):
    result = ()
    if len(atuple) > 3:
        for i in range(len(atuple)):
            for j in range(1,len(atuple)):
                for k in range(2,len(atuple)):
                    if atuple[i] + atuple[j] + atuple[k] == 0:
                        if atuple[i] != atuple[j] and atuple[j] != atuple[k] and atuple[k] != atuple[i]:
                            result = (atuple[i],atuple[j],atuple[k])
                            return result
    return result

print(triplet((-8, 0, 4, -2, -1, 1, 2)))
print(triplet((-1, 1, 1, 1)))
print(triplet((-4, 3, 0, -2, -1, -3)))