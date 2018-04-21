import sqlite3

conn = sqlite3.connect("store/possib_k0.db")

conn.execute("CREATE TABLE possib_key(key TEXT)")

conn.execute("CREATE TABLE filter_key(key TEXT)")

conn.commit()

conn.close()

conn = sqlite3.connect("store/possib_k1.db")

conn.execute("CREATE TABLE possib_key(key TEXT)")

conn.execute("CREATE TABLE filter_key(key TEXT)")

conn.commit()

conn.close()

conn = sqlite3.connect("store/RESULT.db")

conn.execute("CREATE TABLE key0(key TEXT)")

conn.execute("CREATE TABLE key1(key TEXT)")

conn.commit()

conn.close()

print("Done!")



