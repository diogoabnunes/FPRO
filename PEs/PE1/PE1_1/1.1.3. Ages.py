# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 13:25:44 2018

@author: diogo
"""

#3. Ages
#Write a Python program that has two lists of equal size referenced by variables names (a list of
#strings) and ages (a list of integers), with values of your choice. The program prints all pairs
#name-age where name is from list names and age is from list age at the same position.
#For example:
#● for names = ["bart", "marie", "jo"] and ages = [23, 75, 19] , the output is bart-23 marie-75 jo-19
#● for names = ["mary", "john"] and ages = [13, 95] , the output is mary-13 john-95

names = ["bart","marie","jo"]
ages = [23,75,19]

names = ["mary","john"]
ages = [13,95]

result = ""
n = 1
for name in names:
    a = 1
    for age in ages:  
        if n == a:
            result += str(name) + "-" + str(age) + " "
        a += 1
    n += 1

print(result)