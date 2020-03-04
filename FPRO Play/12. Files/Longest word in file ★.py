# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 10:42:46 2018

@author: diogo
"""

def longest(filename):
    with open(filename) as f:
        content = f.read()
    words = set(content.split())
    max_len = len(max(words,key=len))
    word = [w for w in words if len(w) == max_len]
    return sorted(word)[0]

print(longest("shakespeare.txt"))
print(longest("monty.txt"))