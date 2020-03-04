# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 22:34:41 2018

@author: diogo
"""

def unique(atuple):
    s_atuple = set(atuple)
    result = tuple(sorted(s_atuple))
#    s_atuple = tuple(sorted(atuple))
#    result = ()
#    for i in range(1,len(s_atuple)):
#        if s_atuple[i] != s_atuple[i-1]:
#            result = result + (s_atuple[i],)
#    result = (s_atuple[0],) + (result[:i])
    return result


#    s_atuple = sorted(atuple)
#    result = []
#    for elem in s_atuple:
#        if elem not in result:
#            result.append(elem)
#    return tuple(result)

print(unique((8, 8, 1, 3, 1, 3, 5)))
print(unique((1, 1, 1, 1)))