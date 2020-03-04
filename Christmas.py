# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 19:07:07 2018

@author: diogo
"""
import time
import sys
import random


#Beginning
print("--------------")
time.sleep(1)
print("CHRISTMAS GAME")
time.sleep(1)
print("--------------")
time.sleep(1)
start = input("Do you want to play? \nYes \nNo \nAnswer: ").lower()
while start != "yes" and start != "no":
    print()
    start = input("What?: ").lower()
if start == "no": sys.exit("Bye! Merry Christmas!")
if start == "yes": print("Let's START!")
time.sleep(3)


#Choose game
game = input("Which game do you want do play? \n(1) Rock-Paper-Scissors \n(2) Rolling the dice \n(3) Guessing Game \n(4) Hangman Game \nAnswer: ")

again = "yes"
while again == "yes":
    if game == "1":
        print()
        print("Rock-Paper-Scissors")
        print("Rules: Everyone know the rules!")
        time.sleep(5)
        A = input("Player A: ")
        B = input("Player B: ")
        print("And the winner is...")
        time.sleep(3)
        
        if A == "rock":
            print()
            if B == "rock": print("That's a draw!")
            if B == "paper": print("The winner is B!")
            if B == "scissors": print("The winner is A!")
        
        elif A == "paper":
            print()
            if B == "rock": print("The winner is A!")
            if B == "paper": print("That's a draw!")
            if B == "scissors": print("The winner is B!")
        
        elif A == "scissors":
            print()
            if B == "rock": print("The winner is B!")
            if B == "paper": print("The winner is A!")
            if B == "scissors": print("That's a draw!")
            
    if game == "2":
        print()
        print("Rolling the dice between 0 and 100")
        print("Rules: The winner is the player with the higgest value. Good luck!")
        time.sleep(5)
        np = int(input("How many players? "))
        p = 1
        max_value = -1
        max_player = 0
        while np != 0:
            guess = random.randint(0,100)
            print(f"Player {p}:",guess)
            if guess > max_value:
                max_value = guess
                max_player = p
            np -= 1
            p += 1
        print(f"The winner is...")
        time.sleep(3)
        print(f"Player {max_player} with {max_value} points!")
    
    if game == "3":
        print()
        print("Guessing Game")
        print("Rules: try to guess the number between 0 and 100 in as few tries as you can!")
        time.sleep(5)
        a = random.randint(0,100)
        guess = -1
        count = 0
        while guess != a:
            guess = input("What's your guess? ")
            if guess == "exit":
                break
            count += 1
            guess = int(guess)
            if guess < a:
                print("Too low!")
            elif guess > a:
                print("Too high!")
            else:
                print(f"Got it! Tries: {count}")
                
    if game == "4":
        print()
        print("Hangman Game")
        print("Rules: try to find the word behind the spaces. You have 10 tries!")
        time.sleep(5)
        words = ["christmas","santa","tree","presents","family","love","friendship","snow"]
        word = random.choice(words)
        guesses = ''
        turns = 10
        while turns > 0:         
            failed = 0               
            for char in word:      
                if char in guesses:    
                    print (char,)
                else:
                    print ("-",)     
                    failed += 1
            if failed == 0:        
                print ("You won! Congratulations!")
                break              
            guess = input("Guess a character: ") 
            guesses += guess                    
            if guess not in word:  
                turns -= 1      
                print ("Wrong...")    
                print ("You have", + turns, 'more guesses.') 
                if turns == 0:           
                    print ("You Lose... Better luck next time!")
    
    #play again
    time.sleep(5)
    again = input("Do you want to play again? ").lower()
if again == "no": sys.exit("Bye! Merry Christmas!")