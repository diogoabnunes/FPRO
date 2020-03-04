# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 21:31:17 2019

@author: diogo
"""

def histogram(alist,bins):
    result = []
    if bins == []: return []
    for i in range(len(bins)-1):
        count = 0
        for elem in alist:
            if elem >= bins[i] and elem < bins[i+1]: count += 1
        result.append(count)
    return result

print(histogram([1, 1, 1, 4, 5, 8, 10], (0, 3, 7, 12))) #[3, 2, 2]
print(histogram([0, 3, 4, 7, 8, 1, 5], (0, 3, 7, 12))) #[2, 3, 2]
print(histogram([3, 0, 1, 5, 3, 2], (0, 3, 6))) #[3, 3]
print()
print(histogram([14, -10, 7, 6, 5, 4, 3, 4, 7, 12, 11, 10, 8], (-10, 5, 10, 15)))
#[4, 5, 4]
print(histogram([], (0, 1, 4, 5))) #[0, 0, 0]
print(histogram([3, 5, 80, 60, 60, 80, 85, 25, 86, 12, 11], (3, 10, 50, 70, 90, 100)))
#[2, 3, 2, 4, 0]
print(histogram([0, 0.5, 0.2, 0.1, 0.7, 0.8, 0.25, 0], (0, 1)))
#[8]