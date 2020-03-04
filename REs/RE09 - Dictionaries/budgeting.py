# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 22:24:55 2018

@author: diogo
"""

def custo(wishlist,products):
    custo = 0
    for k in wishlist:
        custo += wishlist[k]*products[k]
    return custo

def maisbarato(products,wishlist):
    mais_barato = 99999
    prod_mais_barato = None
    for wish in wishlist:
        if products[wish] < mais_barato:
            mais_barato = products[wish]
            prod_mais_barato = wish
    return prod_mais_barato


def budgeting(budget,products,wishlist):
    
    while custo(wishlist,products) > budget:
        mais_barato = maisbarato(products,wishlist)
        if wishlist[mais_barato] > 1:
            wishlist[mais_barato] -= 1
        else:
            del wishlist[mais_barato]
                    
    return wishlist

print(budgeting(1000, 
                {'ps4': 350, 
                 'smartphone': 400, 
                 'jacket': 40, 
                 'pc': 600, 
                 'glasses': 75}, 
                 {'ps4': 1, 'smartphone': 1, 'pc': 1}))

print(budgeting(1500, 
                {'xbox': 250, 
                 'smartphone': 500, 
                 'jeans': 50, 
                 'pc': 600, 
                 'glasses': 100}, 
                 {'glasses': 3, 'jeans': 2, 'pc': 1, 'xbox':1}))

print(budgeting(1200, 
                {'xbox': 250, 
                 'smartphone': 500, 
                 'jeans': 50, 
                 'pc': 600, 
                 'glasses': 100}, 
                 {'glasses': 3, 'jeans': 2, 'pc': 1, 'xbox':1}))