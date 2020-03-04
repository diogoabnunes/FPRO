# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 15:42:27 2018

@author: diogo
"""

def rec_sum_digits(n):
    n = str(n)
    if len(n) == 1:
        return n
    return int(n[0]) + int(rec_sum_digits(n[1:]))

print(rec_sum_digits(12))
print(rec_sum_digits(45))