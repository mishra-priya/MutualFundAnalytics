import sqlite3

conn = sqlite3.connect("bluestock_mf.db")

cursor = conn.cursor()

with open("sql/schema.sql","r") as f:
    cursor.executescript(f.read())

conn.commit()

conn.close()

print("Database Created Successfully")