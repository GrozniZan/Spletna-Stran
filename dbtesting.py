import sqlite3

CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS contacts (
    contact_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);
"""

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute(CREATE_TABLE)
conn.commit()


insert_command = """
INSERT INTO contacts (first_name, last_name)
VALUES("ab", "CD");
"""
cursor = conn.cursor()
cursor.execute(insert_command)
conn.commit()

cursor = conn.cursor()
cursor.execute("SELECT * FROM contacts;")
print(cursor.fetchall())


conn.close()