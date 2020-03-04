# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 22:46:12 2018

@author: diogo
"""

def palindrome_index(s):
    if s == s[::-1]:
        return -1
    else:
        for i in range(len(s)):
            s_copy = s[0:i] + s[i+1:]
            if s_copy == s_copy[::-1]:
                return i
            else:
                continue
        return -1             
            
print(palindrome_index("aaab"))
print(palindrome_index("tattarrattat"))