# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 14:04:45 2018

@author: diogo
"""

#4. Rock-Paper-Scissors

#Write a Python program to implement the two-player Rock-Paper-Scissors game. Each player
#chooses rock , scissors , or paper . The program ask the input of player A, the input or
#player B, compare them, print out a message of congratulations to the winner.
#Consider the rules: rock beats scissors , scissors beats paper , paper beats rock .

#For example:
#● for A= rock and B= paper , the output is The winner is B
#● for A= scissors and B= paper , the output is The winner is A
#● for A= paper and B= paper , the output is That's a draw

A = input("Player A: ")
B = input("Player B: ")

if A == "rock":
    if B == "rock": print("That's a draw")
    if B == "paper": print("The winner is B")
    if B == "scissors": print("The winner is A")

elif A == "paper":
    if B == "rock": print("The winner is A")
    if B == "paper": print("That's a draw")
    if B == "scissors": print("The winner is B")

elif A == "scissors":
    if B == "rock": print("The winner is B")
    if B == "paper": print("The winner is A")
    if B == "scissors": print("That's a draw")