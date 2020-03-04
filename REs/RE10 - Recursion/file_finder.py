# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 11:21:43 2018

@author: diogo
"""

def file_finder(dirs,file_name):
    if file_name in dirs and file_name != dirs[0]:
        return dirs[0] + "/" + file_name
    for subd in dirs:
        if type(subd) == list:
            searcher = file_finder(subd,file_name)
            if searcher:
                return dirs[0] + "/" + searcher

dirs = ["home",
        ["Documents",
             [ "FPRO", "lists.txt", "recursion.pdf", "functions" ],
             [ "Python", "hello_world.py", "readme.md" ],],
         ["Downloads",
              [ "Movies",
                   [ "TV Series", "BreakingBad.mp4", "TheBigBangTheory.avi" ],"1.avi", "22", "001.mp4"],],"tmp.txt", "page.html"]

print(file_finder(dirs, 'Documents'))
print(file_finder(dirs, 'recursion.pdf'))
print(file_finder(dirs, "TheBigBangTheory.avi"))
print(file_finder(dirs, "001.mp4"))
print(file_finder(dirs, "page.html"))