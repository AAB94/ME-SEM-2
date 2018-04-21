import sqlite3

arr = [(28,0),(35,1),(37,1),(44,0),(32,0),(25,0),(41,0)]

conn = sqlite3.connect("store/possib_k1.db")
c = conn.cursor()

c.execute("select key from possib_key")

rows = c.fetchall()

for key in rows:
    count = 0
    for i in arr:
        if key[0][i[0]] == str(i[1]):
            count += 1
    if count == 7:
        conn.execute("INSERT INTO filter_key VALUES('%s')" % key[0])

conn.commit()
