# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 21:58:51 2018

@author: diogo
"""

num = int(input("Integer: "))
sum = 0
i = 1
while i<=num:
    if num % i == 0:
        sum = sum + i
    i = i + 1
print(sum)

#check