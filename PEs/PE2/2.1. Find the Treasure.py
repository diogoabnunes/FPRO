# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 14:36:29 2018

@author: diogo
"""

#1. Find the treasure

#The path to the treasure is given as a sequence of commands that are steps of length 1: up , left ,
#right or down . Write a function map(pos, steps) that takes a coordinate pos , which is a
#tuple with values x and y as (x,y), and a sequence of commands in a string steps , with the
#steps separated by a hyphen, and computes the final position in the map.

#For example:
#● map((0,0), "up-up-left-right-up-up") returns the tuple: (0,4)
#● map((0,4), "up-up-left-left-up-up") returns the tuple: (-2,8)

def map(pos,steps):
    x = pos[0]
    y = pos[1]
    steps = steps.split("-")
    for step in steps:
        if step == "up": y += 1
        if step == "down": y -= 1
        if step == "right": x += 1
        if step == "left": x -= 1
    return x,y

print(map((0,0), "up-up-left-right-up-up"))
print()
print(map((0,4), "up-up-left-left-up-up"))