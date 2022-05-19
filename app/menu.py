from tkinter import *
from tkinter import messagebox
from log_in import login, create_user
import database

window = Tk()

def show_menu():
    print("\n===========================================================")
    print("|                    Welcome to Hookit!                   |")
    print("|                                                         |")
    print("|               Would you like to login?      press .1    |")
    print("|               Would you like to add a user? press .2    |")
    print("|               See all users?                press .3    |")
    print("|               Search for specific user?     press .4    |")
    print("|               Delete post?                  press .     |")
    print("|               Exit                          press .5    |")
    print("===========================================================")

def see_spec_user():
    window = Tk()
    conn = database.connect()
    Label(window, text="Enter name of player: ").grid(row=1, sticky=W)
    name = Entry(window)
    name.grid(row=1, sticky=W)
    Button(window, text="Submit", command=database.get_user_by_name(conn, name.get())).grid(row=2, sticky=W)



def new_menu():
    window = Tk()
    conn = database.connect()
    Button(window, text="See all users", command=database.get_all_users(conn)).grid(row=1, sticky=W)
    Button(window, text="See specific users", command=see_spec_user).grid(row=2, sticky=W)
   # Button(window, text="See all users", command=database.delete_user).grid(row=3, sticky=W)



def login():
    window = Tk()
    Label(window, text="Enter username: ").grid(row=0, sticky=W)
    Label(window, text="Enter password: ").grid(row=1, sticky=W)
    username = Entry(window)
    password = Entry(window)
    username.grid(row=0, column=1)
    password.grid(row=1, column=1)
    connection = database.connect()
    cur = connection.cursor()
    uname_auth = username.get()
    pswd_auth = password.get()
    Button(window, text="Login", command=new_menu).grid(row=2, sticky=W)
    authentication = (uname_auth, pswd_auth)
    cur.execute("SELECT * FROM users;")
    all_users = cur.fetchall()
    
    if authentication in all_users:
        messagebox.showinfo(title="Welcome", message=uname_auth)
    # else:
    #     messagebox.showerror(title="ACCESS DENIED", message="Have you forgotten your password?")
    #     window.destroy()


Button(window, text = "Login", command=login).grid(row=1, sticky=W)
Button(window, text = "Add user", command=create_user).grid(row=2, sticky=W)
Button(window, text="Exit", command=exit).grid(row=3, sticky=W)

window.mainloop()
