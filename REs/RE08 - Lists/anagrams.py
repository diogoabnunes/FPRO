# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 14:29:38 2018

@author: diogo
"""

def anagrams(alist):
    result = []
    r1 = []
    r2 = []
    for i in alist:
        i1 = i.replace(" ","")
        for n in alist:
            n1 = n.replace(" ","")
            if i != n and sorted(i1.lower()) == sorted(n1.lower()):
                result += [[i,n]]
                alist.remove(n)          
    result = sorted(result)
    for p in result:
        for l in result:
            if p != l and p[0] == l[0]:
                r1 += [sorted([p[0],p[1],l[1]])]
                result.remove(p)
                result.remove(l)
    for x in result:
        r2.append(sorted(x))
    fr = r2 + r1
    for q in alist:
        if q not in str(fr):
            fr.append([q])
    fr = sorted(fr, key = lambda s:s[0].lower())
    
    return fr

print(anagrams(["they see", 
                "eat", 
                "The eyes", 
                "car has", 
                "ate", 
                "a crash", 
                "tea"]))
    
print(anagrams(["sentence", 
                "lives", 
                "ten scene", 
                "bat", 
                "Elvis", 
                "CE sennet"]))