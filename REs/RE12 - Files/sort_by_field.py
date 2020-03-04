# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 12:03:45 2018

@author: diogo
"""

def sort_by_field(filename,field):
    with open(filename,"r") as f:
        lines = f.read()
        lines = [x.split(",") for x in lines.split("\n")]
        index = lines[0].index(field)
        lines = [lines[0]] + sorted(lines[1:],key=lambda x: x[index])
        f.close()
    result = ""
    for line in lines:
        result += (",".join(x for x in line)) + "\n"
    return result

print(sort_by_field("emails.txt", "surname"))
print(sort_by_field("emails.txt", "mail"))
