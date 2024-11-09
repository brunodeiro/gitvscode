""" 
Este projeto tem como objetivo a criação de um jogo de pedra, papel e tesoura contra o computador. |
This project has a goal, a rock paper and scissor game against a machine. 
"""

import random
import os


def player_choice(types):
    player_hand = input("What do you choose ? [Rock] [Paper] [Scissor]\n").lower()
    if player_hand not in types:
        os.system('cls' if os.name=="nt" else "clear") # clear terminal
        print("Wrong, Try again\n")
        return player_choice(types) #calling a function again until enter the correct info
    return player_hand

def check_winner(player_hand,computer_hand):
    if (player_hand == "rock" and computer_hand == "scissor") or \
       (player_hand == "paper" and computer_hand == "rock") or \
       (player_hand == "scissor" and computer_hand == "paper"):
         return f"\nYOU WIN !"
    elif player_hand == computer_hand:
        return "\nDRAW GAME!"
    else:
        return f"\nYOU LOSE !"
    
def game ():
    types = ["rock", "paper", "scissor"]
    intro = "\nWelcome to rock, paper and scissor game !"
    print(intro.upper())
    player = player_choice(types) #calling player choice function with list
    computer = random.choice(types) #randomize computer choice
    print(f"Computer choose: {computer.capitalize()}")
    print(check_winner(player,computer))
    
    
game() #calling the game function