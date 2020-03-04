# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 14:29:23 2018

@author: diogo
"""

def local_minima(alist,n):
    result = [] 
    
    if n % 2 == 0:
        n_low = n / 2
        n_up = n_low - 1
    else:
        n_low = n // 2
        n_up = n // 2
    counter = 0  
    for i in alist:
        lower = counter - n_low
        upper = counter + n_up + 1 
        if lower < 0:
            lower = 0
        if upper > (len(alist) - 1):
            upper = len(alist)     
        local_minimum = min(alist[lower:upper])
        count = 0  
        for u in alist[lower:upper]:
            if u == local_minimum:
                count += 1        
        if count > 1:
            ind = alist.index(local_minimum) 
        else:
            ind = counter  
        if i == local_minimum and (local_minimum, ind) not in result:
            result.append((local_minimum, counter))
        counter += 1
        
    return result

print(local_minima([10, 3, 3, 14, 5, 7, 4], 3))
print(local_minima([0, 3, 3, 14, 5, 7, 4], 3))
print(local_minima([2, 1, 1, 1, 7, 3, 1], 5))