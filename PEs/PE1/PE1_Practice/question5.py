# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 22:48:46 2018

@author: diogo
"""

lower = int(input("Lower: "))
upper = int(input("Upper: "))
#result = "Prime numbers between",lower,"and",upper,"are:"
result = ""
for num in range (lower,upper+1):
    if num>1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            result = str(result) + str(num) + " "
print("Prime numbers between",lower,"and",upper,"are:",result)

#check