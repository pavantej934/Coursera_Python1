# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 14:13:44 2016

@author: pavantej
"""
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    
import random

print ('''Howdy! Welcome to Guess the Number. 
This game is build by Pavan Tej using a Platform called CodeSkulptor (Thanks to CoursEra for this).
Game Instructions -
1. You need to guess the secret number within a limited number of chances.
2. For a number between 0 - 100, you will have 7 guesses
3. For a number between 0 - 1000, you will have 10 guesses
4. To begin, press the run button.
5. To end, simply cross the game window.
Good Luck!!
''')
secret_number = 0
max_guess_range = 100
count = 0
max_guesses = 7
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global max_guess_range
    print ("*************")
    print ("Game Starts, your range is [0,"+str(max_guess_range)+")")
    print ("You have "+str(max_guesses)+" guesses left")
    secret_number = random.randrange(0,max_guess_range) 

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global max_guesses
    global max_guess_range
    max_guess_range = 100
    max_guesses = 7
    new_game()
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global max_guesses
    global max_guess_range
    max_guess_range = 1000
    max_guesses = 10
    new_game()
    
    
def input_guess(guess):
    # main game logic goes here	
    global count
    guess = int(guess)
    print ("------------")
    print ("Guess was "+ str(guess))
    if (guess > secret_number):
        count += 1
        if count < max_guesses :
            print ("Lower")
            print ("Remaining guesses "+str(max_guesses-count))
        else:
            print ("You ran out of guesses, your number is "+ str(secret_number))
            new_game()
    elif (guess < secret_number):
        count += 1
        if count < max_guesses :
            print ("Higher")
            print ("Remaining guesses "+str(max_guesses-count))
        else:
            print ("You ran out of guesses, your number is "+ str(secret_number))
            new_game()
    else :
        print ("Correct")
        count = 0
        new_game()
        
# create frame
frame = simplegui.create_frame("Guess the Number",200,200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0,100)",range100,100)
frame.add_button("Range is [0,1000)",range1000,100)

frame.add_input("Enter your guess",input_guess,100)

frame.start()

# call new_game 
new_game()
