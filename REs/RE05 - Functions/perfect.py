# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 17:49:49 2018

@author: diogo
"""

#
# DESCRIPTION of exercise 3: 
#
#   Write a Python function is_perfect(n) to check whether a number n is perfect or not.
#   In number theory, a perfect number is a positive integer that is equal to the sum of its proper
#   positive divisors, that is, the sum of its positive divisors excluding the number itself. 
#
#   For example: for n=6 the function returns True, for n=12 returns False, and for n=28 returns True. 
#
# Do NOT alter the function prototype given
#
# PASTE your code inside the function block below, paying atention to the right indentation
#
# Don't forget that your program should use the return keyword in the last instruction 
# to return the appropriate value
#

def is_perfect(n):
    """
    check whether a number n is perfect 
    """
    #### MY CODE STARTS HERE ######################################
    result = 0
    i = 1
    while i < n:
        if n % i == 0:
            result = result + i
        i = i + 1
    result = (n == result)
    return result
    #### MY CODE ENDS HERE ########################################
print(is_perfect(6))
print(is_perfect(12))
print(is_perfect(28))