# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 14:37:29 2018

@author: diogo
"""

#4. Genealogy by order

#Susana needs to build a genealogy tree of her family for her school homework. She has asked
#her family and written everything as a list of tuples, where each tuple is (name,
#relationship) . The relationship is given as "sibling”, “parent”, “cousin” or “grandparent".

#Write a Python function genealogy(l) to help her order the family. The order is given by
#relationship using the following rule: sibling < parent < cousin < grandparent .
#When there is a draw, use the relative's name by ascending order.

#For example:
#● returns the list:
#[('carlos', 'sibling'), ('paulo', 'sibling'), ('maria',
#'parent'), ('pedro', 'parent'), ('alfredo', 'cousin'), ('carla',
#'cousin'), ('artur', 'grandparent'), ('geraldes', 'grandparent'),
#('matilde', 'grandparent')]
#● returns the list:
#[('sofia', 'sibling'), ('bernardo', 'parent'), ('sara',
#'parent')]

def order(elem):
    name,relship = elem
    order = ("sibling","parent","cousin","grandparent").index(relship)
    return order,name

def genealogy(l):    
    return sorted(l, key = order)


l= [("maria", "parent"), ("matilde", "grandparent"),("geraldes", "grandparent"), ("carlos", "sibling"),
("paulo", "sibling"), ("artur", "grandparent"),("pedro", "parent"), ("alfredo", "cousin"), ("carla", "cousin")]
print(genealogy(l))
print()
print(genealogy([("sofia", "sibling"), ("sara", "parent"), ("bernardo", "parent")]))