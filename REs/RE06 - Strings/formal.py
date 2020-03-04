# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 16:19:33 2018

@author: diogo
"""

def formal(name):
    name = name.split()
    result = name[-1] + ", "
    for i in range (len(name)-1):        
        n_name = name[i]
        n_initial = n_name[0]
        result = result + n_initial + ". "
    return result
    
print(formal("Aníbal António Cavaco Silva"))