# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 14:04:00 2018

@author: diogo
"""

#1. Integers

#Write a Python program that takes the list of integers ints = [1, 2, 2, 3, 5, 9, 13,
#21, 34] and a number num given by user input, and separes the list in two strings: one with
#the numbers less than num and the other with the numbers greater than num .

#For example:
#● for num=3 the first line of the output is "Less: 1 2 2" and a second line with "Greater: 5 9 13 21 34" (without quotes)
#● for num=9 the output is "Less: 1 2 2 3 5" and a second line with "Greater: 13 21 34" (without quotes)

ints = [1,2,2,3,5,9,13,21,34]
num = int(input("Number: "))
less = ""
greater = ""
for elem in ints:
    if elem > num:
        greater += str(elem) + " "
    elif elem < num:
        less += str(elem) + " "

print("Less: " + less)
print("Greater: " + greater)