# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 13:24:57 2018

@author: diogo
"""

#1. Check Armstrong number
#Write a Python program that checks if a number num with 3 digits, given by user input, is an
#Armstrong number or not. In an Armstrong number of 3 digits, the sum of the cubes of each
#digit is equal to the number itself.
#Use Spyder3 to create a new file named question1.py in your folder named PE1 .
#For example:
#● for num= 153 , the output is: True
#● for num= 234 , the output is: False

num = int(input("Number: "))
num_copy = num
soma = 0
while num > 0:
    digit = num % 10
    soma += digit**3
    num = num // 10

if num_copy == soma:
    print(True)
else:
    print(False)