# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 14:37:45 2018

@author: diogo
"""

#5. Caesar cipher with Fib

#Caesar encrypted the messages he sent to his generals by left shifting all letters in the
#message by s ∈ ℤ places in the alphabet. For example, with a left shift of 2, C would be
#replaced by A, D would become B, and so on.

#Write a Python function caesar(message) that uses a slightly more sophisticated cipher.
#Instead of applying the same shift to all the letters, a variable shift is used. Specifically, the shift
#to be applied to the n -th character in the string will be given by the n -th value in Fibonacci's
#sequence F n given by the the formula:
#You can assume that all letters will be uppercase and special characters (like spaces, commas,
#etc.) are not to be ciphered.

#For example:
#Message H E L L O W O R L D !
#Fibonacci’s sequence 0 1 1 2 3 5 8 13 21 34 55 89
#Ciphered message H D K J L O B W D A !

#You may use the remainder operator (%) to handle shifts that circle back to the end of the
#alphabet, i.e. when you reach the beginning of the alphabet: 4 % 26 (= 4), -4 % 26 (= 22),
#-30 % 26 (= 22).

#For example:
#● caesar("HELLO WORLD!") returns the string: HDKJL OBWDA!
#● caesar("CAESAR CIPHER") returns the string: CZDQXM PNHETD
#● caesar("FIBONACCI SEQUENCE") returns the string: FHAMKVUPN PTCVRBDT

from math import sqrt

def fib(n):
    return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))

def caesar(message):
    result = ""
    for index,letter in enumerate(message):
        if letter.isalpha():
            result += chr((ord(letter)-ord("A")-fib(index)) % 26 + ord("A"))
        else:
            result += letter
    return result

print(caesar("HELLO WORLD!"))
print()
print(caesar("CAESAR CIPHER"))
print()
print(caesar("FIBONACCI SEQUENCE"))