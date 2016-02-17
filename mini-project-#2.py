"""
This module is a game of "Guess the number".
Input will come from buttons and an input field.
All output for the game will be printed in the console.
"""

import simplegui
import random
import math

number_range = 100

def new_game():
    """
    Initialize global variables in this function.
    """
    global guess_time, secret_number
    guess_time = math.log(number_range+1,2)
    guess_time = math.ceil(guess_time)
    guess_time = int (guess_time)
    if number_range == 100:
        secret_number = random.randrange(0, 100)
    else :
        secret_number = random.randrange(0, 1000)
    print
    print "New game. Range is from 0 to" ,number_range
    print "Number of remaining guesses is ",guess_time


def range100():
    """
    Set button that changes the range to [0,100) and starts a new game.
    """
    global number_range
    number_range = 100
    new_game()

def range1000():
    """
    Set button that changes the range to [0,1000) and starts a new game.
    """
    global number_range
    number_range = 1000
    new_game()

def input_guess(guess):
    """
    Determine winner and print message.
    """
    global guess_time
    guess = int (guess)
    print
    print "Guess was ",  guess
    guess_time = guess_time -1
    print "Number of remaining guesses is ",guess_time
    if guess_time == 0 and guess != secret_number:
        print "You ran out of guesses. The number was ", secret_number
        new_game()
        return

    if  number_range > guess > secret_number:
        print "Lower!"
    elif guess < secret_number:
        print "Highr!"
    elif guess == secret_number:
        print "Correct!"
        new_game()
    else:
        print "Guesses Range : 0~",number_range

# create frame
frame = simplegui.create_frame("Guess Number",200,200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0,100)",range100,200)
frame.add_button("Range is [0,1000)",range1000,200)
frame.add_input("Enter a guess",input_guess,200)
frame.start()
# call new_game
new_game()
