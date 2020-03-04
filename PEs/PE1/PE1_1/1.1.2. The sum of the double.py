# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 13:25:36 2018

@author: diogo
"""

#2. The sum of the double
#Write a Python program that, given an integer with one digit d and another integer num , both
#provided by the user in that order, prints the sum of the double of the digits of num greater than
#d .
#For example:
#● for d= 3 and num= 135 , the output is 10 (because of 2*5)
#● for d= 2 and num= 135 , the output is 16 (because of 2*3+2*5)
#● for d= 3 and num= 102 , the output is 0
#● for d= 2 and num= 12345 , the output is 24

d = int(input("Digit: "))
num = int(input("Number: "))

num_copy = num
soma = 0
while num > 0:
    digit = num % 10
    if digit > d:
        soma += 2*digit
    num //= 10

print(soma)