# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 13:25:11 2018

@author: diogo
"""

#
# DESCRIPTION of exercise 6: 
#
#   Write a program that given an integer in the variable num, provided by the user,
#   computes its reverse (the number with the digits by the reverse order).
#
# Do NOT alter the function prototype given
#
# PASTE your code inside the function block below, paying atention to the right indentation
#
# Don't forget that your program should use the return keyword in the last instruction 
# to return the appropriate value

def capicua():
    result = "Not yet implemented"

#### MY CODE STARTS HERE ######################################
    num = int(input("num: "))
    num_copy = num
    reverse = 0
    while num_copy > 0:
        rest = num_copy % 10
        reverse = (reverse * 10) + rest 
        num_copy = num_copy // 10
    if num == reverse:
        result = "<" + str(num) + "> is a palindrome"
    else:
        result = "<" + str(num) + "> is not a palindrome"
#### MY CODE ENDS HERE ########################################
    return result
print(capicua())