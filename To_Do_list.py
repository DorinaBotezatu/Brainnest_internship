"""
To-Do List: Create a program that allows users to add, view, and mark items as complete on a to-do list.
"""

dict_to_do_list = {}


def add_items():
    user_input = int(input("Add number of items to add \n"))
    x = 1
    while x <= user_input:
        item = input("Add new to do item \n")
        if not dict_to_do_list:
            key = 1
        else:
            key = max(dict_to_do_list.keys()) + 1
        dict_to_do_list[key] = item
        x += 1


def view_to_do_list():
    for keys in dict_to_do_list:
        print(f'{keys} => {dict_to_do_list[keys]}')


def mark_complete_items():
    select_item = int(input("Type the number of item you want to mark as complete "))
    if type(select_item) is not int:
        print("Please type a number ")
    else:
        result = ''
        for c in dict_to_do_list[select_item]:
            result = result + c + '\u0336'
        dict_to_do_list[select_item] = result


def To_do_list():
    while True:
        user = input("Enter an option:\n1.Add items\n2.Display list\n3.Mark complete items\n4.Exit the program \n")
        if "1" in user:
            add_items()
        if "2" in user:
            view_to_do_list()
        if "3" in user:
            mark_complete_items()
        if "4" in user:
            break

if __name__ == "__main__":
    To_do_list()

