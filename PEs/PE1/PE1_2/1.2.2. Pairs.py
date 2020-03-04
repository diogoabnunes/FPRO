# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 14:04:14 2018

@author: diogo
"""

#2. Pairs

#Write a Python program that, given a non negative integer number by user input, computes the
#number of two consecutive digits (pairs) that are equal.

#For example:
#● for number=1122234997550 the output is 5 (the pairs are 11, 22, 22, 99 and 55)
#● for number = 1988887 the output is 3 (the pairs are 88, 88 and 88)

number = int(input("Number: "))
number_copy = number
cons_pairs = 0
while number > 10:
    if (number % 100) // 10 == number % 10:
        cons_pairs += 1
    number //= 10
print(cons_pairs)