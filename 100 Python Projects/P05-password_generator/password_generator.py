""""
Este projeto tem como objetivo a criação de um gerador de senhas | 
This project has a goal a password generator
"""
import os
import random

def amount(type):  # function to ask how much each parameter will have
    try:
        quantity = int(input(f"How many {type} would you like in your password?\n"))
        return quantity
    except ValueError:  # if isn't a integer clear e ask again
        os.system("cls" if os.name == "nt" else "clear")
        print("Wrong value! Try again")
        return amount(type)

def get_amounts(parameters):
    amounts = []  # empty list to store the quantity of each parameter
    for count in parameters:
        amounts.append(amount(count))  # save parameters on list
    return amounts

def generate_password(parameters_2, amounts):
    result = []
    for count in range(len(parameters_2)):  # return the length of the list
        for i in range(amounts[count]):
            result.append(random.choice(parameters_2[count]))  # save on list, random objects from parameters_2 list
    random.shuffle(result)  # mix list order
    return result

def generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    parameters = ["letters", "symbols", "numbers"]
    parameters_2 = [letters, symbols, numbers]

    print("Welcome to the Password Generator!")
    amounts = get_amounts(parameters)
    result = generate_password(parameters_2, amounts)

    print(f"\nNew password: {''.join(result)}")


generator()