# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 15:38:33 2018

@author: diogo
"""
from functools import reduce

def reduce_map_filter(args):
    
    if args[0] == "map":
        if type(args[2]) == list:
            return list(map(args[1],args[2]))
        return list(map(args[1],reduce_map_filter(args[2])))
    
    if args[0] == "filter":
        if type(args[2]) == list:
            return list(filter(args[1],args[2]))
        return list(filter(args[1],reduce_map_filter(args[2])))
    
    if args[0] == "reduce":
        if type(args[2]) == list:
            return reduce(args[1],args[2])
        return reduce(args[1],reduce_map_filter(args[2]))

print(reduce_map_filter(("map",
                         lambda x: 2*x,
                         [1,2,3])))

print(reduce_map_filter(("map",
                         lambda x: 2*x,
                         ("filter",
                          lambda x: x%2 != 0,
                          [1,2,3]))))

print(reduce_map_filter(("reduce",
                         lambda a,b: a+b,
                         ("map",
                          lambda x: 2*x,
                          ("filter",
                           lambda x: x%2 != 0,
                           [1,2,3])))))