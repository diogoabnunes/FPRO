# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 22:30:37 2018

@author: diogo
"""

def longest(s):
    string_split = s.split()
    long = len(string_split[0])
    for i in range(1,len(string_split)):
        if len(string_split[i]) > long:
            long = len(string_split[i])
    return long

print(longest("A list with some words"))
print(longest("Unnecessarily long sentence since the longest word is the first one"))