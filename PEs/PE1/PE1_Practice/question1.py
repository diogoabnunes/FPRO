# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 21:28:34 2018

@author: diogo
"""
print("A = P * (1 + (r/n))**(nt) for P = 1000 and t = 1")
def earn_comp_int():
    result = ""
    r = (float(input("Interest rate in percentage: ")))/100
    print(r)
    n = int(input("Payment frequency: "))
    print(n)
    A = float(1000 * (1 + (r/n))**(n))
    A = format(A,".3f")
    result = "For r= " + str(r) + " and n=" + str(n) + " you'll have " + str(A)
    return result

print(earn_comp_int())
print(earn_comp_int())

#check