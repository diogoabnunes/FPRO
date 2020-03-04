# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 22:45:58 2018

@author: diogo
"""

def interleave(f1,f2):
    with open(f1) as f:
        with open(f2) as g:
            result = ""
            flines = f.readlines()
            glines = g.readlines()
            for i in len(flines):
                print(flines[i])
                print(glines[i])
        
print(interleave("monty.txt", "shakespeare.txt"))