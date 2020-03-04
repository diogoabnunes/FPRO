# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 11:21:58 2018

@author: diogo
"""

def find(matrix,x,y,chr,word):
    if word == "":
        return True
    controlx0 = x != 0
    controlxmax = x != len(matrix)
    controly0 = y != 0
    controlymax = y != len(matrix)
    
    if matrix[x][y] == chr:
        if ((controlxmax and find(matrix,x+1,y,word[0],word[1:]))
        or (controlymax and controlxmax and find(matrix,x+1,y+1,word[0],word[1:])) 
        or (controlymax and find(matrix,x,y+1,word[0],word[1:]))
        or (controlx0 and find(matrix,x-1,y,word[0],word[1:]))
        or (controly0 and controlx0 and find(matrix,x-1,y-1,word[0],word[1:]))
        or (controly0 and find(matrix,x,y-1,word[0],word[1:]))
        or (controly0 and controlxmax and find(matrix,x+1,y-1,word[0],word[1:]))
        or (controlymax and controlx0 and find(matrix,x-1,y+1,word[0],word[1:]))):
            return True
    return False

def soup(matrix,word):
    for i in range(len(matrix)):
        for k in range(len(matrix)):
            if find(matrix,i,k,word[0],word[1:]):
                return str(chr(i+65)) + str(k+1)

mx = (('X', 'A', 'B', 'N', 'T', 'O'),
      ('Y', 'T', 'N', 'R', 'I', 'T'),
      ('U', 'P', 'O', 'M', 'D', 'S'),
      ('I', 'O', 'H', 'U', 'O', 'O'),
      ('R', 'T', 'E', 'L', 'Q', 'X'),
      ('I', 'W', 'J', 'K', 'P', 'Z'))

print(soup(mx, 'PORTO'))
print(soup(mx, 'HOTEL'))
print(soup(mx, 'RIO'))
#print(soup(mx,"OTN"))
#print(soup(mx,"SDM"))
#print(soup(mx,"PQO"))
