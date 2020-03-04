# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 18:46:27 2019

@author: diogo
"""

def exception_str(f):
    try: f()
    except Exception as e: return e 
    return "No exception was raised"
    
print(exception_str(lambda: 1/0))
print(exception_str(lambda: 0))