from tkinter import Tk, Button, Label, Entry, W, Text
from tkinter import messagebox
import tkinter as tk
from format import format_menu
import database


"""Program that runs with pythons tkinter GUI. Stores and fetches data from sqlite-database.
    format_menu and database is two other py-files with functionalities exaclty what they sound like.
    format has a function that randomly choose between 5 games to play on the golf court and database
    has the database functionality."""


window = Tk()
window.geometry('450x200')  


def listBox():
    window = Tk()
    conn = database.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE name = (?)", (name.get(),))
    user = cur.fetchone()
    print(f"This is user: {user}")
    textBox = Text(window, height=5, width=52)
    label = Label(window, text="Here is your user")
    textBox.pack()
    label.pack()
    textBox.insert(tk.END, user)


def get_all_users():
    window = Tk()
    conn = database.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    users = cur.fetchall()
    textBox = Text(window, height=7, width=55)
    label = Label(window, text="Here is all users")
    textBox.pack()
    label.pack()
    textBox.insert(tk.END, users)


def see_spec_user():
    window = Tk()
    window.geometry('400x150') 
    Label(window, text="Enter name of player: ").grid(row=1, sticky=W)
    global name
    name = Entry(window)
    name.grid(row=1, sticky=W)
    Button(window, text="Submit", command=listBox).grid(row=2, sticky=W)


def get_play():
    window = Tk()
    game = format_menu()
    textBox = Text(window, height=7, width=55)
    label = Label(window, text="Your game format")
    textBox.pack()
    label.pack()
    textBox.insert(tk.END, game)


def get_all_posts():
    window = Tk()
    conn = database.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM posts;")
    posts = cur.fetchall()
    textBox = Text(window, height=7, width=55)
    label = Label(window, text="the Wall")
    textBox.pack()
    label.pack()
    textBox.insert(tk.END, posts)


def save_post():
    connection = database.connect()
    database.create_post_table(connection)
    a = post.get()
    database.add_post(connection, a)
    messagebox.showinfo(title="New post", message="Successfully posted!")


def create_post():
    window = Tk()
    window.geometry('400x150') 
    Label(window, text="Enter post: ").grid(row=0, sticky=W)
    global post
    post = Entry(window)
    post.grid(row=0, column=1)
    Button(window, text="Submit", command=save_post).grid(row=3, sticky=W)


def delete():
    conn = database.connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM posts WHERE id = (?)", (post_id.get(),))
    conn.commit()
    messagebox.showinfo(title="Delete post", message="Successfully deleted your post")


def delete_post():
    window = Tk()
    window.geometry('400x150')
    Label(window, text="Enter post id: ").grid(row=0, sticky=W)
    global post_id
    post_id = Entry(window)
    post_id.grid(row=0, column=1)
    Button(window, text="Submit", command=delete).grid(row=3, sticky=W)


def new_menu():
    window = Tk()
    window.geometry('500x250')
    window.title("MENU")
    Button(window, text="See all users", command=get_all_users).grid(row=1, sticky=W)
    Button(window, text="See specific users", command=see_spec_user).grid(row=2, sticky=W)
    Button(window, text="See what game to play", command=get_play).grid(row=3, sticky=W)
    Button(window, text="Create a post", command=create_post).grid(row=4, sticky=W)
    Button(window, text="View the feed", command=get_all_posts).grid(row=5, sticky=W)
    Button(window, text="Delete post", command=delete_post).grid(row=6, sticky=W)
    Button(window, text="Exit", command=exit).grid(row=7, sticky=W)


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
