# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 15:45:06 2022

@author: Egbua Golden
"""

import random

print("\n Rules for winning the game are as follows: \n"
                                +"Paper beats rock \n"
                                + "Rock beats scissors \n"
                                +"Scissors beats paper \n")
 

while True:
    player = input("Enter a choice (R - rock, P - paper, S - scissors): ").upper()
    options = ("R", "P", "S")
    CPU = random.choice(options)

    while player not in options:
        print("oops! your choice is not in the list")
        player = input("choose a valid option from the list (R, P, or S): ").upper()
    print(f"\nYou chose {player} \n" + f"computer chose {CPU}.\n")
    if player == CPU:
        print(f"Both players selected {player}. \n" + "It's a tie!")
    elif player == "R":
        if CPU == "S":
            print("Rock beats scissors! \n" + " You win!")
        else:
            print("Paper beats rock! You lose.")
    elif player == "P":
        if CPU == "R":
            print("Paper beats rock! You win!")
        else:
            print("Scissors beats paper! You lose.")
    elif player == "S":
        if CPU == "P":
            print("Scissors beats paper! You win!")
        else:
            print("Rock beats scissors! You lose.")

    again = input("Will you like to play again? (yes or no): ")
    if again.lower() != "yes":
        break