# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 18:47:35 2019

@author: diogo
"""

def rec_exceptions(l):
    result = []
    for elem in l:
        try:
            elem = elem()
            if type(elem) == list: 
                result.extend(rec_exceptions(elem))
            else: 
                continue
        except Exception as e: result.append(e)
            
    return result

#print(rec_exceptions([lambda: 1/0]))
print(rec_exceptions([lambda: [lambda: [1,2,3].index(-1), 
                               lambda: ''[2]], 
                    lambda: [1,2,3][4], 
                    lambda: [lambda: [lambda: 1/0]]]))