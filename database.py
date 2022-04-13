import sqlite3


CREATE_USER_TABLE = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, handicap INTEGER, age INTEGER, gender TEXT, homecourse TEXT);"

INSERT_USER = "INSERT INTO users (name, handicap, age, gender, homecourse) VALUES (?, ?, ?, ?, ?);"

GET_ALL_USERS = "SELECT * FROM users;"

GET_USER_BY_NAME = "SELECT * FROM users WHERE name = ?;"

def connect():
    return sqlite3.connect("hookit.db")

def create_tables(connection):
    with connection:
        connection.execute(CREATE_USER_TABLE)


def add_user(connection, name, handicap, age, gender, homecourse):
    with connection:
        connection.execute(INSERT_USER, (name, handicap, age, gender, homecourse))


def get_all_users(connection):
    with connection:
        return connection.execute(GET_ALL_USERS).fetchall()

def get_user_by_name(connection, name):
    with connection:
        return connection.execute(GET_USER_BY_NAME, (name,)).fetchall()
