""""
Este projeto tem como objetivo a criação de um jogo de caça ao tesouro | 
This project has a goal a treasure hunt game
"""


print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

while True:
    path = input("You're at a cross road. Choose your path\n (Type 'left' or 'right')\n").lower()
    if path == "left":
        while True:
            path = input("You've come to a lake. There's an island in the middle of it.\n Type 'wait' to wait for a boat. Type 'swim' to swim across\n").lower()
            if path == "wait":
                while True:
                    path = input("You arrive at the island unharmed. There is a house with 3 doors.\n Type the color of the door (Red, Yellow, Blue)\n").lower()
                    if path == "yellow":
                        print("You Win!")
                        break
                    elif path == "blue":
                        print("Eaten by beasts. Game Over.")
                        break
                    elif path == "red":
                        print("Burned by fire. Game Over.")
                        break
                    else:
                        print("Wrong information.")
                break
            elif path == "swim":
                print("Attacked by trout. Game Over.")
                break
            else:
                print("Wrong information.")
        break
    elif path == "right":
        print("Fall into a hole. Game Over.")
        break
    else:
        print("Wrong information.")
