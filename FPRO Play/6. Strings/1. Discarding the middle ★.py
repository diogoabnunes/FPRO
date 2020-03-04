# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 22:26:39 2018

@author: diogo
"""

def discard_middle(s):
    if len(s) > 3:
        result = s[0:2] + s[-2:]
    else:
        result = ""
    return result

print(discard_middle("string"))
print(discard_middle("n"))