# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 21:15:04 2018

@author: diogo
"""

def sort_by_value(dict):
    dict1 = sorted(dict.items(), key = lambda x: x[1])
    return dict1

print(sort_by_value({"Blue":"#0000FF", 
                   "Green":"#008000", 
                   "Black":"#000000", 
                   "White":"#FFFFFF"}))