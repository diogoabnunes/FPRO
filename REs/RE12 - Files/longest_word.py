# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 12:03:28 2018

@author: diogo
"""

def longest_word(url):
    import urllib.request
    response = urllib.request.urlopen(url)
    html = response.read().decode()
    response.close()
    
    words_url = set(html.split())
    with open("words.txt") as f:
        words_dict = set(f.read().split("\n"))

    words = words_url.intersection(words_dict)
    max_len = len(max(words,key=len))

    word = [w for w in words if len(w) == max_len]
    return sorted(word)[0]
                
print(longest_word("https://en.wikipedia.org/wiki/Monty_Python"))
print(longest_word("https://web.fe.up.pt/~jlopes/doku.php/teach/fpro/sheet"))
print(longest_word("https://en.wikipedia.org/w/index.php?title=University_of_Porto&oldid=870279066"))
print(longest_word("https://www.w3schools.com/python/python_intro.asp"))