import database
from login import login


USER_MENU = """  
                 ------------------------
                 | Welcome to Hookit!   |
                 |  1. Login            |
                 |  2. Add user         |
                 |  3. See all users    |
                 |  4. Find user by name|
                 |  5. Exit             |
                 ------------------------

Your selection:
"""


def user_menu():
    connection = database.connect()
    database.create_tables(connection)

    while (user_input := input(USER_MENU)) != "5":
        if user_input == "1":
            logged_in = login()
            if logged_in in database.get_all_users:
                print(f"Welcome {logged_in}")
        elif user_input == "2":
            name = input("Enter your name: ")
            handicap = float(input("Enter your current handicap: "))
            age = int(input("Enter your age: "))
            gender = input("Enter your gender: ")
            homecourse = input("Enter your homecourse: ")
            username = input("Enter username ")
            password = input("Enter a password ")

            database.add_user(connection, name, handicap, age, gender, homecourse, username, password)
        elif user_input == "3":
            user = database.get_all_users(connection)

            for u in user:
                print(f"{u[1]}, {u[2]}, {u[3]}")
        elif user_input == "4":
            name = input("Enter users name to find: ")
            user = database.get_user_by_name(connection, name)
            # Adding print-statement to make this funciton work
            print(user)

        elif user_input == "5":
            # adding a bye-frase and change from pass to break
            print("Thanks, come again")
            break
        else:
            print("Invalid input!")


user_menu()