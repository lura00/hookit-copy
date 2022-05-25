from app import database


"""Tests run with pytest. They test multiple functions"""


def test_create_table_and_insert_data():
    """Test that creates a copy of user table, insert a value and then tries to fetch it. 
        Then drops the table. Assert the output data will look like as below"""
    conn = database.connect()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users_copy (id INTEGER PRIMARY KEY, name TEXT, handicap INTEGER, age INTEGER, gender TEXT, homecourse TEXT, username VARCHAR, password VARCHAR);")
    cur.execute("INSERT INTO users_copy VALUES (NULL,?,?,?,?,?,?,?)", ("testname", 8, 25, "female", "test-course", "test-username", "testpass"))
    conn.commit()
    cur.execute("SELECT * FROM users_copy WHERE name = (?)", ("testname",))
    data = cur.fetchall()
    cur.execute("DELETE FROM users_copy WHERE name = (?)", ("testname",))
    cur.execute("DROP TABLE users_copy;")
    conn.commit()
    conn.close()
    assert data == [(1, 'testname', 8, 25, 'female', 'test-course', 'test-username', 'testpass')]


def test_post_function():
    """Test that creates a copy of posts table, insert a value and then tries to fetch it. 
        Then drops the table. Assert the output data will look like as below"""
    conn = database.connect()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS posts_copy (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL);")
    cur.execute("INSERT INTO posts_copy VALUES (NULL, ?)", ('Hello golfers',))
    conn.commit()
    cur.execute("SELECT * FROM posts_copy;")
    data = cur.fetchall()
    cur.execute("DROP TABLE posts_copy;")
    conn.commit()
    conn.close()
    assert data == [(1, 'Hello golfers')]
