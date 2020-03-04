# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 16:14:22 2018

@author: diogo
"""
#Level 1

import string
string = "http://www.pythonchallenge.com/pc/def/map.html"
def translate(string):
#    print(string)
#    result = ""
#    print()
#    for letter in string:
#        if letter.isalpha():
#            if letter == "y": result += "a"
#            elif letter == "z": result += "b"
#            else: result += chr(ord(letter) +2)
#        else: result += letter    
#    return result
    table = string.maketrans('abcdefghijklmnopqrstuvwxyz','cdefghijklmnopqrstuvwxyzab')
    return string.translate(table)

#print(translate("diogo"))
#print(translate(string))
print(translate("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."))

#Level 2

