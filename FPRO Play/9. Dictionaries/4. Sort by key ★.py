# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 21:11:44 2018

@author: diogo
"""

def sort_by_key(dict):
    dict = sorted(list(dict.items()))
    return dict

print(sort_by_key({"Blue":"#0000FF", 
                   "Green":"#008000", 
                   "Black":"#000000", 
                   "White":"#FFFFFF"}))