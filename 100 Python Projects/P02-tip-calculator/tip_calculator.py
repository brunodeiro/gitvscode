""""
Este projeto tem como objetivo a criação de uma calculadora de gorjetas | 
This project has a goal a tip calculator
"""

def calculate_percentage(amount,percentage): #Function to calculate the percentage
    if amount == 0:
        return 0
    return (amount * percentage) / 100


def calculate_amount_for_person (total, percentage, num_people): #Function to calculate the amount for each person
    tip_value = calculate_percentage(total,percentage)
    total_person = (total + tip_value) / num_people
    return total_person
    

print("Welcome to the Tip Calculator. \n") #Introduction

total_bill = float(input("Whats was the total bill?\n")) #total of bill

tip_selected = int(input("Select the amount of tip you want to tip for the service\n[10], [12] or [15] ")) #tip give

people_split_bill = int(input("How many people to split the bill?\n"))


#VERSION 1 - without function
#valor_percent = calculate_percentage(total_bill,tip_selected)
#amount_for_person = (total_bill+valor_percent) / people_split_bill

#VERSION 2 - With function
amount_for_person = calculate_amount_for_person(total_bill, tip_selected, people_split_bill)



print(f'Each person should pay: {amount_for_person:.2f}')











