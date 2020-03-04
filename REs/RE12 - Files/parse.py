# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 12:03:19 2018

@author: diogo
"""

import ast
def parse(filename):
    with open(filename) as f:
        lines = f.read()
        lines = [x.strip() for x in lines.split("\n")]
        result = ""
        elem = [0 for x in range(lines.count("("))]
        par = 0
        for s in lines:
            if s == "(":
                if result[-1:] != "(" and elem[par-1] > 0:
                    result += ","
                if result[-1:] == ")":
                    result += ","
                    elem[par-1] += 1
                result += s
                par += 1
            elif s == ")":
                result += ","
                result += s
                par -= 1
            else:
                if result[-1:] != "(" and par > 0:
                    result += ","
                result += s
                if par > 0:
                    elem[par-1] += 1
        result = "(" + result + ",)"
        result = ast.literal_eval(result)
        return result
                
print(parse("tuple1.txt"))
print(parse("tuple2.txt"))

# falta adicionar vírgulas aos tuplos