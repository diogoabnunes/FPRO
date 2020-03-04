# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 12:56:15 2018

@author: diogo
"""
import math


def distance(x1, y1, x2, y2):
    """computes the distance between 2 pints"""
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


def area(radius):
    """computes the area of a circle with radius"""
    return 3.14159 * radius**2


def area_of_circle(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))


print(area_of_circle(0, 0, 0, 1))
