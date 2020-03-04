# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 22:44:42 2018

@author: diogo
"""

LE = int(input("LE: "))
RE = int(input("RE: "))
PE = int(input("PE: "))
TE = int(input("TE: "))
grade = (LE + RE + 4*PE + 4*TE)/50
if (0<=LE<=100) and (0<=RE<=100) and (0<=PE<=100) and (0<=TE<=100):
    if (PE<40) or (TE<40):
        print("RFC")
    else:
        print(int(grade))
else:
    print("Input error")
    
#check