from unicodedata import name
import database
import random

USER_MENU = """------------------------
                 | Welcome to Hookit!   |
                 |  1. Add user         |
                 |  2. See all users    |
                 |  3. Find user by name|
                 |  4. Exit             |
                 ------------------------

Your selection:
"""

FORMAT_MENU = """
Spin the Wheel!
Press Enter to spin the wheel!
"""


def user_menu():
    connection = database.connect()
    database.create_tables(connection)

    while (user_input := input(USER_MENU)) != "5":
        if user_input == "1":
            name = input("Enter your name: ")
            handicap = float(input("Enter your current handicap: "))
            age = int(input("Enter your age: "))
            gender = input("Enter your gender: ")
            homecourse = input("Enter your homecourse: ")

            database.add_user(connection, name, handicap, age, gender, homecourse)
        elif user_input == "2":
            user = database.get_all_users(connection)

            for u in user:
                print(f"{user[1]}, {user[2]}, {user[3]}")
        elif user_input == "3":
            name = input("Enter users name to find: ")
            user = database.get_user_by_name(connection, name)


        elif user_input == "4":
            pass
        else:
            print("Invalid input!")

random_number = random.randint(1, 5)
answer = ""
while (format_input := input(FORMAT_MENU)) != "6":
    def format_menu():
        connection = database.connect()
        database.create_tables(connection)
        format_input = input()
        if random_number == 1:
            answer = "Match Play"
        
        elif random_number == 2:
            answer = "Scramble"

        elif random_number == 3:
            answer = "Stroke Play"
        
        elif random_number == 4:
            answer = "Bestball"

        elif random_number == 5:
            answer = "Alternate Shot"

        else:
            "Error, please try again"

        print(f'The format you will be playing is: {answer}')

        


format_menu()
user_menu()

