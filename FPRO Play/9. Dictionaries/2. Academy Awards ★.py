# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 20:47:25 2018

@author: diogo
"""

def academy_awards(alist):
    dic = {}
    for k,v in alist:
        if v not in dic.keys():
            dic[v] = 1
        else:
            dic[v] += 1
    return dic

print(academy_awards([("Best Picture", "Moonlight"), 
                      ("Best Director", "La La Land"), 
                      ("Best Actor", "Manchester by the Sea"), 
                      ("Best Actress", "La La Land"), 
                      ("Best Supporting Actor", "Moonlight"), 
                      ("Best Supporting Actress", "Fences"), 
                      ("Best Original Screenplay", "Manchester by the Sea"), 
                      ("Best Original Score", "La La Land")]))