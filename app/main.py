import database


USER_MENU = """  ------------------------
                 | Welcome to Hookit!   |
                 |  1. Add user         |
                 |  2. See all users    |
                 |  3. Find user by name|
                 |  4. Exit             |
                 ------------------------

Your selection:
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
                print(f"{u[1]}, {u[2]}, {u[3]}")
        elif user_input == "3":
            name = input("Enter users name to find: ")
            user = database.get_user_by_name(connection, name)


        elif user_input == "4":
            pass
        else:
            print("Invalid input!")


user_menu()