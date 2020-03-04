# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 17:57:42 2018

@author: diogo
"""

#
# DESCRIPTION of exercise 4: 
#
#    Write a Python function adigits that receives 3 strings, each one with a 
#    single character, representing a decimal digit.
#    The function should return the highest integer number that you can assemble 
#    with the 3 digits given as parameters.
#
#    For example: adigits("4", "2", "5") returns the integer 542
#
# Do NOT alter the function prototype given
#
# PASTE your code inside the function block below, paying atention to the right indentation
#
# Don't forget that your program should use the return keyword in the last instruction 
# to return the appropriate value
#

def adigits(n1, n2, n3):
    """
    build the highest possible number out of the combination of 3 digits
    """
    #### MY CODE STARTS HERE ######################################
    alist = [n1,n2,n3]
    alist.sort()
    result = "".join(alist[::-1])
#    if (int(n1) >= int(n2) and int(n1) >= int(n3)):
#        if int(n2) >= int(n3):
#            result = int(str(n1) + str(n2) + str(n3))
#        else:
#            result = int(str(n1) + str(n3) + str(n2))
#    if (int(n2) >= int(n1) and int(n2) >= int(n3)):
#        if int(n1) >= int(n3):
#            result = int(str(n2) + str(n1) + str(n3))
#        else:
#            result = int(str(n2) + str(n3) + str(n1))
#    if (int(n3) >= int(n1) and int(n3) >= int(n2)):
#        if int(n1) >= int(n2):
#            result = int(str(n3) + str(n1) + str(n2))
#        else:
#            result = int(str(n3) + str(n2) + str(n1))
    return result
    #### MY CODE ENDS HERE ########################################
print(adigits("4","5","9"))
print(adigits("9","1","9"))