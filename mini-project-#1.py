"""
This module is a game of Rock-paper-scissors-lizard-Spock.
"""

import random

def name_to_number(name):
    """
    Convert name to number.
    """
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else :
        return "False"

def number_to_name(number):
    """
    Convert number to a name.
    """
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else :
        return "False"

def rpsls(player_choice):
    """
    Determine winner, print winner message
    """
    print
    # print out the message for the player's choice
    print "Player chooses", player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    if player_number == "False":
        print "Wrong input."
        return
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    # convert comp_number to comp_choice using the function ()
    comp_choice = number_to_name(comp_number)

    if comp_choice == "False":
        print "Wrong input."
        return

    # print out the message for computer's choice
    print "Computer chooses", comp_choice
    # compute difference of comp_number and player_number modulo five
    who_win = (player_number-comp_number)%5
    if who_win ==1 or who_win ==2:
        print "Player wins!"
    elif who_win ==3 or who_win ==4:
        print "Computer wins!"
    else :
        print "Player and computer tie!"

# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
