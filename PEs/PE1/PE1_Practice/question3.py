# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 22:22:02 2018

@author: diogo
"""
num = float(input("Number: "))
x0 = num/2
x1 = (x0 + num/x0)/2
while round(x0,2) != round(x1,2):
    x0 = x1
    x1 = (x0 + num/x0)/2
result = (round(x1,3))
print(format(result,".3f"))

#check