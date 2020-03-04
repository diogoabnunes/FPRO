# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 21:30:38 2018

@author: diogo
"""

def rec_to_base(n,base):
    hexa = "0123456789ABCDEF"
    if n < base:
        return hexa[n]
    else:
        return rec_to_base(n // base, base) + hexa[n % base]

print(rec_to_base(16,16))