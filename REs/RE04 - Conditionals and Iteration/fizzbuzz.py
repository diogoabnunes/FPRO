# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 17:32:13 2018

@author: diogo
"""

#
# DESCRIPTION of exercise 3: 
#
#   Write a Python program which “plays” the known game FizzBuzz over a sequence of integers 
#   from 0 to an integer n provided by the user. 
#   See Google Docs for implementation details.
#
# Do NOT alter the function prototype given
#
# PASTE your code inside the function block below, paying atention to the right indentation
#
# Don't forget that your program should use the return keyword in the last instruction 
# to return the appropriate value

def fizz_buzz():
    result = "Not yet implemented"
    
#### MY CODE STARTS HERE ######################################
    result = ""
    n = int(input("n: "))
    i = 1
    while i <= n:       
        if i % 3 == 0 or i % 5 == 0:
            if i % 3 == 0 and i % 5 == 0:
                result = result + ""
            if i % 3 == 0 and i % 5 != 0:
                result = result + ("Fizz")
            elif i % 5 == 0 and i % 3 != 0:
                result = result + ("Buzz")
        else:
            result = result + str(i)
        i = i + 1
        result = result + " "
#### MY CODE ENDS HERE ########################################
    
    return result
print(fizz_buzz())