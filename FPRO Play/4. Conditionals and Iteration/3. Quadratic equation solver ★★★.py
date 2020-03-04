# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 14:10:59 2018

@author: diogo
"""
import math

def solver(a,b,c):
    delta = (b**2) - (4*a*c)
    solutions = []
    if delta >= 0:
        xp = (-b + math.sqrt(delta))/(2*a)
        xn = (-b - math.sqrt(delta))/(2*a)
        
        if delta > 0:
            solutions.insert(0,xp)
            solutions.insert(1,xn)
            return sorted(solutions)
        
        elif delta == 0:
            solutions.insert(0,xp)
            return solutions
    
    else:
        return solutions