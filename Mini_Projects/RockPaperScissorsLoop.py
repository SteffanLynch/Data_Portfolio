#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 14:48:23 2021

@author: steffanlynch
"""

import random

# keep track of who wins throughout the game
user_wins = 0
computer_wins = 0

# list of possible inputs to play the game
options = ["r", "p", "s"]

#user chooses how many games to play on aggregate
best_of = int(input('Best out of: '))

print(best_of)

# define a function that takes in two players as arguments
# and returns True if player wins based on the standard rules
# of rock paper scissors
def is_winner(player, opponent):
    if (player == 'r' and opponent == 's') or \
    (player == 'p' and opponent == 'r') or \
    (player == 's' and opponent == 'p'):
        return True
    
# game continues while the number of games(not inclunding ties) 
# does not exceed best_of
while (user_wins + computer_wins) < best_of:
    user_input = input("""
    What do you play?
    'r' for rock,
    'p' for paper,
    's' for scissors
    Press 'q' to quit: """).lower()
    
    # loop breaks if user enters 'q'
    if user_input == "q":
        break
    
    # if user_input is not 'r', 'p', or 's', then has to try again
    if user_input not in options:
        continue
    
    #computer selects 'r', 'p' or 's' randomly
    computer_pick = random.choice(options)

    #print each players input
    print("You picked: ", user_input)
    print("Computer picked: ", computer_pick)

    # if inputs are the same then, game is tie and goes through loop again
    if user_input == computer_pick:
        print('It\'s a tie!')
        continue

    # if the player is winner, print a win message and add 1 to the user_wins variable
    elif is_winner(user_input, computer_pick):
        print('You won!')
        user_wins += 1

    # by default, if player doesnt win AND not a tie, the computer wins
    # so prints 'you lost' and add 1 to computer_wins
    else:
        print("You lost!")
        computer_wins += 1

#print final score once game is finshed
print("You won ", user_wins, " times.")
print("The computer won ", computer_wins, " times.")
print("Goodbye!")
