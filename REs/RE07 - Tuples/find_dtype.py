# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 23:34:22 2018

@author: diogo
"""

def find_dtype(atuple,data_type):
    result = ()
    for i in atuple:
        if type(i).__name__ == data_type:
            result = result + (i,)
    return result
    
print(find_dtype((1, False, "hello", 2., "world"),"str"))
print(find_dtype((1, 2, 3),"float"))