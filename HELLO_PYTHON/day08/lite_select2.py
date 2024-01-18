import sqlite3

conn = sqlite3.connect('.\\python.db')

cur = conn.cursor()
cur.execute("SELECT * FROM emp")

rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()