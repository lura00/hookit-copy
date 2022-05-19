from ..app import database

def test_create_table_and_insert_data():
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


def test_format_function():
    conn = database.connect()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS format_copy (id INTEGER PRIMARY KEY, format1 TEXT, format2 TEXT, format3 TEXT, format4 TEXT, format5 TEXT);")
    cur.execute("INSERT INTO format_copy VALUES (?,?,?,?,?,?)", (1, 'Scramble', 'Bestball', 'Alternate Shot', 'Match play', 'Stroke play'))
    conn.commit()
    cur.execute("SELECT * FROM format_copy;")
    data = cur.fetchall()
    # cur.execute("DELETE FROM users_copy WHERE name = (?)", ("testname",))
    cur.execute("DROP TABLE format_copy;")
    conn.commit()
    conn.close()
    assert data == [(1, 'Scramble', 'Bestball', 'Alternate Shot', 'Match play', 'Stroke play')]