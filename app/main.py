import database
from log_in import getInput
import menu


# def show_menu():
#     print("\n===========================================================")
#     print("|                    Welcome to Hookit!                   |")
#     print("|                                                         |")
#     print("|               Would you like to login?      press .1    |")
#     print("|               Would you like to add a user? press .2    |")
#     print("|               See all users?                press .3    |")
#     print("|               Search for specific user?     press .4    |")
#     print("|               Delete post?                  press .     |")
#     print("|               Exit                          press .5    |")
#     print("===========================================================")


def user_menu():
    connection = database.connect()
    database.create_tables(connection)

    while True:

        menu()
        user_input = int(input("Make a choice from menu: "))

        if user_input == 1:
            logged_in = getInput()
            print(f"Hello from MAIN {logged_in}")
            all_users = database.get_all_users(connection)
            if logged_in in all_users:
                print(f"Welcome player: {logged_in}")
        elif user_input == 2:
            name = input("Enter your name: ")
            handicap = float(input("Enter your current handicap: "))
            age = int(input("Enter your age: "))
            gender = input("Enter your gender: ")
            homecourse = input("Enter your homecourse: ")
            username = input("Enter username ")
            password = input("Enter a password ")

            database.add_user(connection, name, handicap, age, gender, homecourse, username, password)
        elif user_input == 3:
            user = database.get_all_users(connection)

            for u in user:
                print(f"{u[1]}, {u[2]}, {u[3]}")
        elif user_input == 4:
            name = input("Enter users name to find: ")
            user = database.get_user_by_name(connection, name)

            print(user)

        elif user_input == 5:
            # adding a bye-frase and change from pass to break
            print("Thanks, come again")
            break
        else:
            print("Invalid input!")


if __name__ == "__main__":
    user_menu()
