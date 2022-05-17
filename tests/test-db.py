import sys

sys.path.insert(1, '/home/lura/Dokument/src/python/hookit/app')

import database

def test_create_table():
    conn = database.connect()
    database.create_tables(conn)
    database.INSERT_USER("testname", 8, 25, "female", "test-course", "test-username", "testpass")
    assert database.get_user_by_name("testname") == 

# name, handicap, age, gender, homecourse, username, password