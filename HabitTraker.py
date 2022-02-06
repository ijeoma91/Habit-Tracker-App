from User import User
import os

u = User('John')
def clear():
    os.system('cls')
def menu():
    print()
    print("**---Welcome to Habit Tracker---**")
    print()
    print(" press [1] to create a habit")
    print(" press [2] to show daily habits")
    print(" press [3] to show weekly habits")
    print(" press [4] to remove daily habit")
    print(" press [5] to remove weekly habit")
    print(" press [6] to save and track daily habits")
    print(" press [7] to show currently tracked daily habits")
    print(" press [8] to save and track weekly habits")
    print(" press [9] to show currently tracked weekly habits")
    print(" press [10] to perform daily habit")
    print(" press [11] to perform weekly habit")
    print(" press [0] to Exit")
    print()
def display_menu():
    print()
    anyKey = input(print("press anyKey to return to the main menu"))
    menu();
loop = 1
while loop == 1:
    menu()
    option = int(input("Enter your choice :"))
    if option == 1:
        t = input(print("Enter habit type"))
        hname = input(print("Enter habit name "))
        p = input(print("Enter habit periodicity "))
        u.create_Habit(hname, p, t)
    elif option == 2:
         u.show_daily_habits()
         display_menu()
    elif option == 3:
        u.show_weekly_habits()
        display_menu()
    elif option == 4:
        u.show_daily_habits()
        print()
        name = input(print("Enter name of habit to be remove"))
        u.remove_daily_habit(name)
        u.show_daily_habits()
        print()
        display_menu()
    elif option == 5:
        u.show_weekly_habits()
        print()
        name = input(print("Enter name of habit to be remove"))
        u.remove_weekly_habit(name)
        u.show_weekly_habits()
        print()
        display_menu()
    elif option == 6:
        u.save_daily_habits()
        display_menu()
    elif option == 7:
        print('Your daily habits from the database are: ')
        print()
        u.read_daily_habits()
        display_menu()
    elif option == 8:
        print()
        u.save_weekly_habits()
        display_menu()
    elif option == 9:
        print()
        print('your daily habits from the database are: ')
        print()
        u.read_weekly_habits()
        display_menu()
    elif option == 10:
        print()
        u.show_daily_habits()
        habit_name = input(print("Enter the name of habit to be perform"))
        u.perform_daily_habit_tasks(habit_name)
        print()
        display_menu()
    elif option == 11:
        print()
        u.show_weekly_habits()
        habit_name = input(print("Enter the name of habit to be perform"))
        u.perform_weekly_habit_tasks(habit_name)
        print()
        display_menu()
    else:
        print("Invalid option")
    clear()
