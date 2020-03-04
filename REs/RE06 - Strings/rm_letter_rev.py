# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 15:30:08 2018

@author: diogo
"""

def rm_letter_rev (l , astr):
    new_str = astr.replace(l,"")
    return new_str[::-1]
    
print(rm_letter_rev("s","A Style Guide is about consistency"))
print(rm_letter_rev(" ","a nut for a jar of tuna"))