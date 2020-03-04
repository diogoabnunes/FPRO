# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 22:23:51 2018

@author: diogo
"""

def isomorphic(astring1, astring2):
    dict1 = {a: b for (a,b) in zip(astring1, astring2)}
    values = [i for i in dict1.values()]
    list1 = [(a,b) for a,b in zip(dict1, dict1.values())]
    if sorted(values) == sorted(list(set(astring2))):
        return "'{0}' and '{1}' are isomorphic because we can map: {2}".format(astring1, astring2, list1)
    else:
        return "'{0}' and '{1}' are not isomorphic".format(astring1, astring2)

print(isomorphic('ab', 'aa'))
print(isomorphic('paper', 'title'))
print(isomorphic('foo', 'bar'))
print(isomorphic('turtle', 'tletur'))