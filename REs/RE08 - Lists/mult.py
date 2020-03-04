# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 14:28:51 2018

@author: diogo
"""

def mult(M,N):
    if len(M[0]) != len(N):
        return []
    
    result = [[0 for row in range(len(N[0]))] for col in range(len(M))]  
    for i in range(len(M)): 
        for j in range(len(N[0])): 
            for k in range(len(N)):
                result[i][j] += M[i][k] * N[k][j]
                
    return result

print(mult([[1, 2], [3, 4]], [[2, 0], [1, 2]]))
print(mult([[1, 2, 3], [4, 5, 6]], [[9], [8], [7]]))
print(mult([[7, 8, 9, 10]], [[5], [3], [2], [7]]))