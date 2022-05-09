import sqlite3


CREATE_USER_TABLE = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, handicap INTEGER, age INTEGER, gender TEXT, homecourse TEXT, username VARCHAR, password VARCHAR);"

CREATE_FORMAT_TABLE = "CREATE TABLE IF NOT EXISTS format (id INTEGER PRIMARY KEY, format1 TEXT, format2 TEXT, format3 TEXT, format4 TEXT, format5 TEXT);"

INSERT_FORMAT = "INSERT INTO format (format1, format2, format3, format4, format5) VALUES (Scramble, Bestball, Alternate Shot, Match play, Stroke play);"

INSERT_USER = "INSERT INTO users (name, handicap, age, gender, homecourse, username, password) VALUES (?, ?, ?, ?, ?, ?, ?);"

GET_ALL_USERS = "SELECT * FROM users;"

GET_USER_BY_NAME = "SELECT * FROM users WHERE name = ?;"

def connect():
    return sqlite3.connect("hookit.db")

def create_tables(connection):
    with connection:
        connection.execute(CREATE_USER_TABLE)


def add_user(connection, name, handicap, age, gender, homecourse, username, password):
    with connection:
        connection.execute(INSERT_USER, (name, handicap, age, gender, homecourse, username, password))


def get_all_users(connection):
    with connection:
        return connection.execute(GET_ALL_USERS).fetchall()

def get_user_by_name(connection, name):
    with connection:
        return connection.execute(GET_USER_BY_NAME, (name,)).fetchall()

def create_format_table(connection):
    with connection:
        connection.execute(CREATE_FORMAT_TABLE)


def add_format(connection, format1, format2, format3, format4, format5):
    with connection:
        connection.execute(INSERT_USER, (format1, format2, format3, format4, format5))
        


