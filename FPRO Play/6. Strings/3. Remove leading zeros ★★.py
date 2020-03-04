# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 22:42:46 2018

@author: diogo
"""

def remove_leading(ip):
    ip = ip.split(".")
    for i in range(len(ip)):
        ip[i] = str(int(ip[i]))
    result = ".".join(ip)
    return result

print(remove_leading("255.024.01.01"))
print(remove_leading("192.168.0.24"))