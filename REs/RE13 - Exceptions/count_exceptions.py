# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 18:46:54 2019

@author: diogo
"""

def count_exceptions(f,n1,n2):
    interval = [x for x in range(n1,n2+1)]
    count = 0
    for i in interval:
        try:
            f(i)
        except:
            count += 1
    return count

print(count_exceptions(lambda x: 1/(abs(x)-2), -5, 5))
print(count_exceptions(lambda x: 1/0 if x > 10 else 0, 0, 50))