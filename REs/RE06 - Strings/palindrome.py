# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 11:56:37 2018

@author: diogo
"""

def palindrome(astring):
    length = len(astring)
    count = 0
    
    for i in range(length):
        for j in range(length+1):
            partial_str = astring[i:j]
            if partial_str == partial_str[::-1]:
                if len(partial_str) > 1:
                    count = count + 1
                
    result = "For string '{0}': {1} palindrome substrings".format(astring,count)
    return result

print(palindrome("geek"))
print(palindrome("ababa"))