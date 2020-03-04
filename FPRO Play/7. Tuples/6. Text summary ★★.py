# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 16:06:16 2018

@author: diogo
"""

def summary(text):
    count = 0
    lower_text = text.lower()
    text = text.split()
    for i in range (len(text)):
        if "e" in text[i] or "E" in text[i]:
            count += 1
    
    result = (len(text),count)
    return result

print(summary("A fool thinks himself to be wise, but a wise man knows himself to be a fool."))