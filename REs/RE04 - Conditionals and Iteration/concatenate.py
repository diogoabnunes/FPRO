# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 13:24:46 2018

@author: diogo
"""
#Write a program that, given two numbers n1 and n2 provided by the user 
#(each one in a different input() statement) produces a new number result
# from the concatenation of both of them, in the order they are given. 
#For example, if the numbers given are n1=23 and n2=567, the resulting number result=23567.
#You are not allowed to use strings.

def concatenate():
    result = "Not yet implemented"
    
#### MY CODE STARTS HERE ######################################
    n1 = input("n1: ")
    n2 = input("n2: ")
    n2len = int(len(n2))
    n1result = int(n1) * 10**(n2len)
    result = int(n1result) + int(n2)
#### MY CODE ENDS HERE ########################################

    return result
print(concatenate())