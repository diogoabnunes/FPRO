# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 15:58:48 2018

@author: diogo
"""

def count(word,phrase):
    word = word.lower()
    phrase = phrase.lower()
    phrase = phrase.split()
    count = phrase.count(word)
    return count
    
print(count("CRAM","How can a clam cram in a clean cream can?"))
print(count("shells"," Sally sells sea shells by the sea shore. But if Sally sells sea shells by the sea shore then where are the sea shells Sally sells? "))