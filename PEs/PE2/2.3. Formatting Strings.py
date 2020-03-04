# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 14:37:17 2018

@author: diogo
"""

#3. Formatting strings

#Write a Python function exactly(s) that, given a string s , where each character is
#guaranteed to be a lowercase letter, a digit or a question mark, checks if there are exactly three
#question marks between all pairs of digits whose sum is exactly 10. The function must return a
#properly formatted string:
#The sequence <s> is OK with the pairs: <t>
#or
#The sequence <s> is NOT OK with first violation with pair: <t>
#if the string respects or not the restriction, respectively. <s> represents the input string and <t>
#represents a tuple with all concatenated pairs of digits that meet the condition or the first
#concatenated pair that does not meet the condition, respectively.

#For example:
#● exactly("acc?7??sss?3rr1??????5???5") returns the string:
#The sequence acc?7??sss?3rr1??????5???5 is OK with the pairs:
#('73', '55')

#● exactly("acc?7??sss3rr1??????5") returns the string:
#The sequence acc?7??sss3rr1??????5 is NOT OK with first violation
#with pair: ('73',)

#● exactly("aa6?9") returns the string:
#The sequence aa6?9 is OK with the pairs: ()

def exactly(s):
    tup = ()
    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            if s[i].isdigit() and s[j].isdigit() and int(s[i]) + int(s[j]) == 10:
                aux = s[i:j]
                if aux.count("?") == 3:
                    tup += (s[i] + s[j],)
                else:
                    tup = (s[i] + s[j],)
                    return f"The sequence {s} is NOT OK with first violation with pair: {tup}"
    return f"The sequence {s} is OK with the pairs: {tup}"

print(exactly("acc?7??sss?3rr1??????5???5"))
print()
print(exactly("acc?7??sss3rr1??????5"))
print()
print(exactly("aa6?9"))