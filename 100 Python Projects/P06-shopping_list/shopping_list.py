""""
Este projeto tem como objetivo a criação de uma lista de compras | 
This project has a goal a shopping list
"""
import os

def show_menu(): 
    print("\nThe List")
    print("[1] - Include Item")
    print("[2] - Show list")
    print("[3] - Remove Item")
    print("[4] - Exit")
    
def add_item(list): #add itens
    item = input("Enter the item´s name: ")
    quantity = input("Enter the item quantity: ")
    list.append({"name": item, "quantity": quantity})
    print(f"'{item}' (Quantity: {quantity}) has been added to the list")
    
def show_list(list):
    if not list:
        print("Empty list")
    else:
        print("\nItems on list:")
        for count, item in enumerate(list, start=1):
            print(f"{count} - {item['name']} - Quantity: {item['quantity']}")
            
def remove_item(list):
    show_list(list)
    if list:
        try:
            index = int(input("Select the item number you want to delete from the list: "))
            if 1 <= index <= len(list):
                item_removed = list.pop(index - 1)
                print(f"{item_removed['name']} was removed from the list")
            else:
                print("wrong number")
        except ValueError:
            os.system("cls" if os.name == "nt" else "clear")
            print("Select a valid number")
            
def main():
    shopping_list = []
    while True:
        show_menu()
        choice = input("Select one option: ")
        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            show_list(shopping_list)
        elif choice == '3':
            remove_item(shopping_list)
        elif choice == '4':
            print("Exiting..")
            break
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("Wrong option. Select a valid number.")
            
main()