# Rock-paper-scissors-lizard-Spock template
import random
import math

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    if name == "rock":
        result = 0
    elif name == "Spock":
        result = 1
    elif name == "paper":
        result = 2
    elif name == "lizard":
        result = 3
    elif name == "scissors":
        result = 4
    else:
        print("Error: No such name.")
    return result        

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    if number == 0:
        result = "rock"
    elif number == 1:
        result = "Spock"
    elif number == 2:
        result = "paper"
    elif number == 3:
        result = "lizard"
    elif number == 4:
        result = "scissors"
    else:
        print("Error: No such number.")
    return result
    
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    
    # print a blank line to separate consecutive games
    print("")    
    
    # print out the message for the player's choice
    print("Player's chooses: " + player_choice)
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    computer_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print("Computer chooses: " + computer_choice)
    
    # compute difference of comp_number and player_number modulo five
    difference = comp_number - player_number
    
    # use if/elif/else to determine winner, print winner message
    if difference == 0:
        print("It's a tie")
    elif difference >= 2:
        print("Player wins!")
    else:
        print("Computer wins!")
    
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")




