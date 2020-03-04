# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 18:10:27 2018

@author: diogo
"""

def batch_norm(alist,batch_size):
    while alist:
        l = alist[:batch_size]
        orde = sorted(l)
        m = orde[(len(orde)-1)//2:len(orde)//2+1]
        median = sum(m)/len(m)
        yield [x-median for x in l]
        alist = alist[batch_size:]
    
    
print(batch_norm([-1, 0, 1, 1, 2, 4], 3))
print(batch_norm([10, 1, -12, 5, 1, 3, 7, 3, 3], 5))