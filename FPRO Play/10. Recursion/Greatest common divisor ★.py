# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 21:35:14 2018

@author: diogo
"""

def rec_gcd(n1,n2):
    low = min(n1,n2)
    high = max(n1,n2)
    if low == 0:
        return high
    if low == 1:
        return 1
    return rec_gcd(low,high%low)

print(rec_gcd(12,14))