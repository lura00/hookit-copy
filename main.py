import database

MENU_PROMPT = """------------------------
                 | Welcome to Hookit!   |
                 |  1. Add user         |
                 |  2. See all users    |
                 |  3. Find user by name|
                 |  4. Exit             |
                 ------------------------

Your selection:
"""


def menu():
    connection = database.connect()
    database.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "5":
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

menu()

