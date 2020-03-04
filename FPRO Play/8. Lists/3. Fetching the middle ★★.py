# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 16:16:31 2018

@author: diogo
"""

def fetch_middle(lists):
    result = []
    n = len(lists)
    for i in range(n):
        
        if len(lists[i]) % 2 != 0:
            med = lists[i][n//2]
            if med < 0:
                med = lists[i][n//2 +1]
            result.append(med)
            
        else:
            med = (lists[i][(n//2)] + lists[i][(n//2 +1)])/2
            result.append(med)

    return result

print(fetch_middle([[1,2,3],[4,5,6],[7,8,9,10]]))
print(fetch_middle([[10,25,35,45],[100,-1,3,4],[-3,-5,-10,-20,-100]]))