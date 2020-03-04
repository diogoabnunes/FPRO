# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 14:26:48 2018

@author: diogo
"""
## 1. Character Input
#name = input("What's your name? ")
#age = input("What's your age? ")
#year_born = 2018 - int(age)
#year_100 = year_born + 100
#print(f"{name}, you'll turn 100 years old at {year_100}!")






## 2. Odd Or Even
#num = int(input("Number: "))
#check = int(input("Number to divide by: "))
#if num % 2 == 0:
#    print(f"The number {num} is even!")
#else:
#    print(f"The number {num} is odd!")
#if num % 4 == 0:
#    print(f"The number {num} is also multiple of 4!")
#if num % check == 0:
#    print(f"{num} divides by {check}!")







## 3. List Less Than Ten
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#print([elem for elem in a if elem < 5])
#num = int(input("Number: "))
#print([elem for elem in a if elem < num])










## 4. Divisors
#num = int(input("Number: "))
#print([i for i in range(1,num+1) if num%i == 0])









##5. List Overlap
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#result = set([x for x in a for y in b if x==y])
#print(list(result))






##6. String Lists
#astring = input("Write a word: ")
#l_astring = astring.lower()
#rev_astring = l_astring[::-1]
#pal = rev_astring == l_astring
#if pal == True:
#    print(f"The word {astring} is a palindrome!")
#else:
#    print(f"The word {astring} is not a palindrome!")






## 7. Lists Comprehensions
#a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#print([i for i in a if i%2 == 0])




## 8. Rock Paper Scissors
#u1 = input("Name of player 1: ")
#u2 = input("Name of player 2: ")
#p1 = input("Player 1: ")
#p2 = input("Player 2: ")
#print()
#if p1 == "rock":
#    if p2 == "rock":
#        print("It´s a draw!")
#    elif p2 == "paper":
#        print(f"The winner is {u2}!")
#    elif p2 == "scissors":
#        print(f"The winner is {u1}!")
#elif p1 == "paper":
#    if p2 == "rock":
#        print(f"The winner is {u1}!")
#    elif p2 == "paper":
#        print("It's a draw!")
#    elif p2 == "scissors":
#        print(f"The winner is {u2}!")
#elif p1 == "scissors":
#    if p2 == "rock":
#        print(f"The winner is {u2}!")
#    elif p2 == "paper":
#        print(f"The winner is {u1}!")
#    elif p2 == "scissors":
#        print("It's a draw!")
#else:
#    print("Your input is not valid...")










## 9. Guessing Game One
#import random
#a = random.randint(1,9)
#guess = 0
#count = 0
#while guess != a:
#    guess = input("What's your guess? ")
#    if guess == "exit":
#        break
#    count += 1
#    guess = int(guess)
#    if guess < a:
#        print("Too low!")
#    elif guess > a:
#        print("Too high!")
#    else:
#        print(f"Got it! Tries: {count}")











## 10. List Overlap Comprehensions
#import random
# 
#a = random.sample(range(1,30), 12)
#b = random.sample(range(1,30), 16)
#print(a)
#print(b)
#print([i for i in a if i in b])
    

    
    
    
    
    
    
    
    
    
    
## 11. Check Primality Functions
#num = int(input("Number: "))
#primes = [i for i in range(2,num) if num%i ==0]
#if (primes != [] or num ==1):
#    print(f"{num} is not prime!")
#else:
#    print(f"{num} is prime!")






## 12. List Ends
#def f(x):
#    return [x[0],x[-1]]
#print(f([5, 10, 15, 20, 25]))








# 13. Fibonacci


