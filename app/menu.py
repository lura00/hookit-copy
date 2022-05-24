from tkinter import Tk, Button, Label, Entry, W
from tkinter import messagebox
import database



window = Tk()
window.geometry('400x150')  

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


# def get_one_user(name):
#     conn = database.connect()
#     spec_user = database.get_user_by_name(conn, name)
#     messagebox.showinfo(title=f"Here is user: {name}", message=spec_user)
def listBox():
    lb = listBox(window)


def see_spec_user():
    window = Tk()
    window.geometry('400x150') 
    # conn = database.connect()
    Label(window, text="Enter name of player: ").grid(row=1, sticky=W)
    name = Entry(window)
    username = name.grid(row=1, sticky=W)
    print(username)
    Button(window, text="Submit", command=print(username)).grid(row=2, sticky=W)
    lb = listBox(window)
    lb.insert(username)
    lb.pack()
    # Text widget eller list 


def new_menu():
    window = Tk()
    window.geometry('400x150') 
    conn = database.connect()
    Button(window, text="See all users", command=database.get_all_users(conn)).grid(row=1, sticky=W)
    Button(window, text="See specific users", command=see_spec_user).grid(row=2, sticky=W)
    # Button(window, text="See all users", command=database.delete_user).grid(row=3, sticky=W)


def saveToDb():
    connection = database.connect()
    database.create_tables(connection)
    a = name.get()
    b = handicap.get()
    c = age.get()
    d = gender.get()
    e = homecourse.get()
    f = username.get()
    g = password1.get()
    database.add_user(connection, a, b, c, d, e, f, g)
    messagebox.showinfo(title="New user", message="Successfully added a new user")
    window.pack()


def create_user():
    Label(window, text="Enter your name: ").grid(row=0, sticky=W)
    Label(window, text="Enter your current handicap: ").grid(row=1, sticky=W)
    Label(window, text="Enter your age: ").grid(row=2, sticky=W)
    Label(window, text="Enter your gender: ").grid(row=3, sticky=W)
    Label(window, text="Enter your homecourse:  ").grid(row=4, sticky=W)
    Label(window, text="Enter your username: ").grid(row=5, sticky=W)
    Label(window, text="Enter your password: ").grid(row=6, sticky=W)
    global name
    global handicap
    global age
    global gender
    global homecourse
    global username
    global password1
    name = Entry(window)
    handicap = Entry(window)
    age = Entry(window)
    gender = Entry(window)
    homecourse = Entry(window)
    username = Entry(window)
    password1 = Entry(window)
    name.grid(row=0, column=1)
    handicap.grid(row=1, column=1)
    age.grid(row=2, column=1)
    gender.grid(row=3, column=1)
    homecourse.grid(row=4, column=1)
    username.grid(row=5, column=1)
    password1.grid(row=6, column=1)

    Button(window, text="Create & save", command=saveToDb).grid(row=7, sticky=W)
    window.pack()


def auth_login():
    connection = database.connect()
    cur = connection.cursor()
    authentication = [(username.get(), password.get())]
    cur.execute("SELECT username, password FROM users;")
    all_users = cur.fetchall()
    print(type(all_users))
    print(type(authentication))
    print(authentication)
    print(all_users)

    check = all(item in all_users for item in authentication)

    print(check)
    if check == True:
        messagebox.showinfo(title="Welcome", message=username.get())
        new_menu()
        window.destroy()
    else:
        messagebox.showerror(title="ACCESS DENIED", message="Have you forgotten your password?")
        # window.destroy()

# Plocka ut del av login logik och sätt i egen funktion och kalla på i "command" i knapp "Login".
def login_button():
    # window = Tk()
    # Button(window, text="Login", command=new_menu).grid(row=3, sticky=W)
    window = Tk()
    window.geometry('400x150') 
    Label(window, text="Enter username: ").grid(row=0, sticky=W)
    Label(window, text="Enter password: ").grid(row=1, sticky=W)
    global username
    global password
    username = Entry(window)
    password = Entry(window)
    username.grid(row=0, column=1)
    password.grid(row=1, column=1)
    Button(window, text="Login", command=auth_login).grid(row=3, sticky=W)
    # window.destroy()
    

Button(window, text="Login", command=login_button).grid(row=4, sticky=W)
Button(window, text="Add user", command=create_user).grid(row=5, sticky=W)
Button(window, text="Exit", command=exit).grid(row=6, sticky=W)

window.mainloop()
