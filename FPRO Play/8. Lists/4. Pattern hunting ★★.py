# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 16:16:38 2018

@author: diogo
"""

def pattern_hunting(l1,l2,p):
    result = []
    for i in range(len(l1)):
        if p in l1[i]:
            result.append(l2[i])
    for i in range(len(l2)):
        if p in l2[i]:
            result.append(l1[i])
    result = (sorted(result))[::-1]
            
    return result

print(pattern_hunting(['a string', 'two strings', 'not here'],
                      ['choose me', 'me too', 'but not me'],
                      'string'))

print(pattern_hunting(['not found', 'pattern here', 'skip', 'next... or not?'],
                      ['pattern here indeed', 'i want to be chosen', 'not my day', 'sneakypatternbutitisthere'],
                      'pattern'))