from tkinter import *
import sqlite3
import random


root = Tk()
root.title('Hookit')
root.geometry("325x250")




#Create database connection
def submit():
   
    conn = sqlite3.connect('hookit.db')

    c = conn.cursor()
    # c.execute("CREATE TABLE player (username TEXT, password TEXT);")
#     values = {
#     'id': Integer, 'username': text, 'password': text
    
# }
#     c.execute(
#     'INSERT INTO players (id, username, password) VALUES (:id, :username, :password);', 
#     values)
    c.execute("INSERT INTO players VALUES (:id, :username, :password);", {"id": key.get(), "username": username.get(), "password": password.get()})
    
    conn.commit()
    conn.close()

key = {k: random.random() for k in range(100)}


    
  

username = Entry(root, width=30)
username.grid(row=0, column=1, padx=20)
password = Entry(root, width=30)
password.grid(row=1, column=1)

username_label = Label(root, text='Username')
username_label.grid(row=0, column=0)
password_label = Label(root, text="Password")
password_label.grid(row=1, column=0)

submit_btn = Button(root, text="Add User", command=submit)
submit_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


root.mainloop()

    
# root.mainloop()
# Label(text = "Hookit - Hook your wedge or hook with your friends", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
# Label(text = "").pack()
# Button(text = "Login", height = "2", width = "30").pack()
# Label(text = "").pack()
# Button(text = "Register", height = "2", width = "30", command = submit).pack()



# def register():
#     screen1 = Toplevel(screen)
#     screen1.title("Register")
#     screen1.geometry("300x250")
#     username = StringVar()
#     password = StringVar()

#     Label(screen1, text = "Enter details below ").pack()
#     Label(screen1, text = "").pack()
#     Label(screen1, text = "Username * ").pack()
#     Entry(screen1, textvariable = username).pack()
#     Label(screen1, text = "Password * ").pack()
#     Entry(screen1, textvariable = password).pack()
#     Button(screen1, text = "Register", width = 10, height = 1, command = submit).pack()







# def main_screen():
#     global screen
#     screen = Tk()
#     screen.geometry("300x250")
#     screen.title("Hookit - Hook your wedge or hook with your friends")
#     Label(text = "Hookit", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
#     Label(text = "").pack()
#     Button(text = "Login", height = "2", width = "30").pack()
#     Label(text = "").pack()
#     Button(text = "Register", height = "2", width = "30", command = register).pack()

#     screen.mainloop()

# main_screen()

