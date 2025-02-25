import sqlite3

conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()
cursor.execute("PRAGMA integrity_check;")
print(cursor.fetchall())
conn.close()