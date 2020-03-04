# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 12:03:12 2018

@author: diogo
"""

def cut(filename,delimiter,field):
    with open(filename,"r") as f:
        content = f.readlines()
        alist = []
        for line in content:
            alist.append(line.rstrip("\n").split(delimiter))
        result = ""
        for line in alist:
            if isinstance(field,list):
                for elem in field:
                    result += str(line[elem-1]) + delimiter
                result = result[:-1] + "\n"
            else:
                result += str(line[field-1]) + "\n"
    return result[:-1]

print(cut("data.csv", ",", 2))
print(cut("data.csv", ",", [2,4]))