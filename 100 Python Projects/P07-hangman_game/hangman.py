""""
Este projeto tem como objetivo a criação de um jogo da forca| 
This project has a goal a hangman game
"""

import random


words = ["sun", "life", "children", "restaurant", "money", "games", "snake", "study", "love"]
selected_word = random.choice(words)
shadow_word = 0
shadow_list = []
chances = 6

while shadow_word < len(selected_word):
    shadow_word += 1
    shadow_list.append("_")
    
print("HANGMAN GAME")
print("Guess the word. [chances: 6]\n")
#print(selected_word) #Was commented because show the answer (Only for tests)
print(" ".join(shadow_list))

while "_" in shadow_list:
    letter = input("Enter the letter: ").lower()
    for count in range (len(selected_word)):
        if letter == selected_word[count]:
            shadow_list[count] = letter
    if letter not in selected_word:
        chances += -1
        print(f"Wrong, try again \n [Rest {chances} chances]")
        if chances == 0:
            print("You Lose!")
            break
    print(" ".join(shadow_list))
    
if "_" not in shadow_list:
    print("Congratulations, you won !")