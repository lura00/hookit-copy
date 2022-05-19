from tkinter import Tk, Label, Entry, W
from tkinter import messagebox
import database


window = Tk()

# Log in labels


# def getInput():
#     a = username.get()
#     b = password.get()
#     window.destroy()

#     global params
#     params = [a,b]
#     print(params)
#     return params


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
    window.destroy()


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

    # Button(window, text="Create & save", command=saveToDb).grid(row=7, sticky=W)

# def login():

#     Label(window, text="Enter username: ").grid(row=0, sticky=W)
#     Label(window, text="Enter password: ").grid(row=1, sticky=W)
#     username = Entry(window)
#     password = Entry(window)
#     username.grid(row=0, column=1)
#     password.grid(row=1, column=1)
#     connection = database.connect()
#     cur = connection.cursor()
#     uname_auth = username.get()
#     pswd_auth = password.get()

#     authentication = (uname_auth, pswd_auth)
#     cur.execute("SELECT * FROM users;")
#     all_users = cur.fetchall()

#     if authentication in all_users:
#         messagebox.showinfo(title="Welcome", message=uname_auth)
#     else:
#         messagebox.showerror(title="ACCESS DENIED", message="Have you forgotten your password?")

# Button(window, text = "Login", command=login).grid(row=8, sticky=W)
# Button(window, text = "Create new user", command=create_user).grid(row=9, sticky=W)

# window.mainloop()
