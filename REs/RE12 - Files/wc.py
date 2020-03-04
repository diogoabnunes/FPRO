# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 12:02:59 2018

@author: diogo
"""

def wc(filename):
    with open(filename,"r") as f:
        content = f.read()
        lines = len(content.splitlines())
        words = len(content.split())
        chars = len(content)
    return lines,words,chars

print(wc("shakespeare.txt"))
print(wc("monty.txt"))