# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 13:25:59 2018

@author: diogo
"""

#5. Octal converter

#Write a Python program that converts a decimal number (base 10) dec , given by user input, into
#an octal number (base 8). 
#Decimal numbers are base 10 numbers and use only digits from 0 to 9, inclusive.
#Octal numbers can use digits from 0 to 7, inclusive.

#For example:
#● for dec= 9 , the output is the octal number 11
#● for dec= 64 , the output is the octal number 100
#● for dec= 23456 , the output is the octal number 55640

dec = int(input("Decimal number: "))
dec_copy = dec
octal = 0
place = 0
while dec > 0:
    octal = dec % 8 * 10**place + octal
    place += 1
    dec //= 8
    
print(octal)