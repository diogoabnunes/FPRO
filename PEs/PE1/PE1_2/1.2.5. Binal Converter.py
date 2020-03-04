# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 14:05:11 2018

@author: diogo
"""

#5. Binary converter

#Write a Python program that converts a decimal number (base 10) dec , given by user input, into
#a binary number (base 2). Decimal numbers of base 10 numbers can use only digits from 0 to 9
#inclusive. Binary numbers can use digits from 0 to 1 inclusive.

#For example:
#● for dec=9 the output is the binary number 1001
#● for dec=64 the output is the binary number 1000000
#● for dec=234 the output is the binary number 11101010

dec = int(input("Number: "))
dec_copy = dec
place = 0
binary = 0
while dec > 0:
    binary = dec % 2 * 10**place + binary
    place += 1
    dec //= 2

print(binary)