# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 23:57:47 2018

@author: diogo
"""

def translate(astring,table):
    result = astring
    for i in range(len(table)):  
        result = result.replace(str(table[i][0]),str(table[i][1])) 
    return result

print(translate("Hello world!",(("a",1),
                                ("e",2),
                                ("i",3),
                                ("o",4),
                                ("u",5),
                                ("!"," :)"))))
print(translate("Testing this string...",((' ', '--'),
                                          ('.','!'),
                                          ('i', 'o'),
                                          ('t', 'tt'))))