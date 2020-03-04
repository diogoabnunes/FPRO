# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 17:14:39 2018

@author: diogo
"""

#
# DESCRIPTION of exercise 2: 
#
#   Write a program that takes a single integer n provided by the user and returns True, 
#   when it is a prime number, and False otherwise.
#
# Do NOT alter the function prototype given
#
# PASTE your code inside the function block below, paying atention to the right indentation
#
# Don't forget that your program should use the return keyword in the last instruction 
# to return the appropriate value

def is_prime():
    result = "Not yet implemented"
    
#### MY CODE STARTS HERE ######################################
    n = int(input("n: "))
    for i in range(2, n):
        if n == 2:
            result = True
            break
        if n % i == 0:
            result = False
            break
        else:
            result = True
#### MY CODE ENDS HERE ########################################
    
    return result
print(is_prime())
