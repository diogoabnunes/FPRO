# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 21:33:46 2019

@author: diogo
"""

def sum_zip(functions,arguments):
    result = []
    for elem in arguments:
        sublist = []
        for function in functions:
            evaluation = function(elem) # realiza a função para o elemento
            sublist.append(evaluation) # acrescenta o resultado á sublista
        sum_eval = sum(sublist)
        subtuple = (sublist,sum_eval)
        result.append(subtuple)
#    return result
    for elem in result:
        yield elem

print(sum_zip([lambda x: x*2,lambda x: x**2,lambda x: -x],[-5, 10, 3]))
#[([-10, 25, 5], 20), ([20, 100, -10], 110), ([6, 9, -3], 12)]
print(sum_zip([lambda x: x*2,lambda x: x**2],[2, 3, 9]))
#[([4, 4], 8), ([6,9],15) ([18, 81], 99)]
print(sum_zip([lambda x: x+2], [1])) #[([3], 3)]
print()
print(sum_zip([], [10, 20, -5, 6, 10]))