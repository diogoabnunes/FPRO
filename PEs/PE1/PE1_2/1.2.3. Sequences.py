# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 14:04:34 2018

@author: diogo
"""

#3. Sequences

#Write a Python program that has two lists of equal size referenced by variables integers and
#reals , with values of your choice. The program prints the sequence with the larger of the two
#numbers in the corresponding positions; when the numbers are equal, the result is the integer.

#For example:
#● for integers = [0, 2, 9, 15, 64] and reals = [0.0, 3.2, 8.4, 15.5,
#128.0] , the output is the string "0 3.2 9 15.5 128.0" (without quotes)
#● for integers = [] and reals = [] , the output is the empty string

integers = [0,2,9,15,64]
reals = [0.0,3.2,8.4,15.5,128.0]

#integers = []
#reals = []

result = ""

i = 0
for inte in integers:
    j = 0
    for real in reals:
        if i == j:
            if real > inte:
                result += str(real) + " "
            else:
                result += str(inte) + " "
        j += 1
    i += 1
    
print(result)