# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 17:41:59 2018

@author: diogo
"""

#
# DESCRIPTION of exercise 2: 
#
#   Write a Python function sum_numbers(n) that returns the sum of all positive
#   integers up to and including n. 
# 
#   For example: sum_numbers(10) returns the value 55 (1+2+3+. . . +10)
#
# Do NOT alter the function prototype given
#
# PASTE your code inside the function block below, paying atention to the right indentation
#
# Don't forget that your program should use the return keyword in the last instruction 
# to return the appropriate value
#

def sum_numbers(n):
    """
    returns the sum of all positive integers up to and including n
    """
    #### MY CODE STARTS HERE ######################################
    result = 0
    i = 0
    while i<=n:
        result = result + i
        i = i + 1
    return result
    #### MY CODE ENDS HERE ########################################
print(sum_numbers(10))