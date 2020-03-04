# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 11:22:10 2018

@author: diogo
"""

def budgeting2(budget, products, wishlist):
    if budget <= 0 or len(wishlist) == 0:
        return {}
    max_spent = 0
    max_bought = {}
    for name, quantity in wishlist.items():
        price = products[name]
        if price <= budget:
            # -> let's try to buy this "item"
            # 1. the item was bought: no longer required in the wishlist
            wishlist2 = wishlist.copy()
            if wishlist2[name] > 1:
                wishlist2[name] -= 1
            else:
                del wishlist2[name]
            # 2. what is the best basket if we use the new wishlist
            bought = budgeting2(budget - price, products, wishlist2)
            if name in bought:
                bought[name] += 1
            else:
                bought[name] = 1
            # 3. how much have we spent: have we maximized our goal?
            spent = 0
            for name, quantity in bought.items():
                spent += quantity * products[name]
            if spent > max_spent:
                max_spent = spent
                max_bought = bought
    return max_bought

print(budgeting2 (1000, 
                  {'ps4': 350, 
                   'smartphone': 400, 
                   'jacket': 40,
                   'pc': 600, 
                   'glasses': 75}, 
                   {'ps4': 1, 'smartphone': 1, 'pc': 1}))
print()
print(budgeting2 (1500, 
                  {'xbox': 250, 
                   'smartphone': 500, 
                   'jeans': 50,
                   'pc': 600, 
                   'glasses': 100}, 
                   {'glasses': 3, 'jeans': 2, 'pc': 1, 'xbox': 1}))
print()
print(budgeting2 (1000, 
                  {'laptop': 2000, 
                   'jeans': 50}, 
                   {'laptop': 2, 'jeans': 3}))