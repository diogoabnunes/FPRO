# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 22:18:13 2018

@author: diogo
"""

def ugly(n):
    if n == 1:
        return True
    elif n > 1:
        for i in [2,3,5]:
            while n % i == 0:
                n = n/i
        return n == 1
    else:
        return False

print(ugly(6))
print(ugly(14))