# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 00:08:51 2018

@author: diogo
"""

def sort_grades(records):
    from statistics import mean as media
    result = tuple(sorted(sorted(sorted(records,key = lambda x : x[1]), key = lambda y : y[0]), key = lambda z : media(z[2]), reverse = True))
    return result

print(sort_grades((('João', 'up20186042', (90, 87)),
                   ('Ana', 'up20186040', (90, 90)),
                   ('José', 'up20186063', (70, 90)),
                   ('Ana', 'up20186061', (90, 90)),
                   ('Tiago', 'up20186070', (100, 90)))))
print(sort_grades((('Maria', 'up20190001', (60, 70, 80)),
                   ('Maria', 'up20190002', (60, 70, 80)),
                   ('Mario', 'up20190003', (100, 10, 80)),
                   ('Rui', 'up20190004', (90, 100, 90)),
                   ('Ana', 'up20190005', (90, 100, 90)))))

#not think yet