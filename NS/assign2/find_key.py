from BitVector import BitVector
import sqlite3

key_permutation_2 = [13,16,10,23,0,4,2,27,14,5,20,9,22,18,11,
                      3,25,7,15,6,26,19,12,1,40,51,30,36,46,
                     54,29,39,50,44,32,47,43,48,38,55,33,52,
                     45,41,49,35,28,31]

to_pred = [8, 17, 21, 24, 34, 37, 42, 53]

bit = [0, 1]

conn = sqlite3.connect("store/possib_k0.db")
c = conn.cursor()

c.execute("select key from filter_key")

rows = c.fetchall()

c.close()

conn.close()

conn = sqlite3.connect("store/RESULT.db")


for k in rows:
    k = k[0]
    tk = BitVector(size=56)
    for i in range(48):
        tk[key_permutation_2[i]] = int(k[i])
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    for e in range(2):
                        for f in range(2):
                            for g in range(2):
                                for h in range(2):
                                    tk[8] = bit[a]
                                    tk[17] = bit[b]
                                    tk[21] = bit[c]
                                    tk[24] = bit[d]
                                    tk[34] = bit[e]
                                    tk[37] = bit[f]
                                    tk[42] = bit[g]
                                    tk[53] = bit[h]
                                    l, r = tk.divide_into_two()
                                    l >> 1
                                    r >> 1
                                    k = l+r
                                    res = str(k)
                                    conn.execute("INSERT INTO key0 VALUES('%s')" % res)
conn.commit()
conn.close()



conn = sqlite3.connect("store/possib_k1.db")
c = conn.cursor()

c.execute("select key from filter_key")

rows = c.fetchall()

c.close()

conn.close()



conn = sqlite3.connect("store/RESULT.db")

for k in rows:
    k = k[0]
    tk = BitVector(size=56)
    for i in range(48):
        tk[key_permutation_2[i]] = int(k[i])
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    for e in range(2):
                        for f in range(2):
                            for g in range(2):
                                for h in range(2):
                                    tk[8] = bit[a]
                                    tk[17] = bit[b]
                                    tk[21] = bit[c]
                                    tk[24] = bit[d]
                                    tk[34] = bit[e]
                                    tk[37] = bit[f]
                                    tk[42] = bit[g]
                                    tk[53] = bit[h]
                                    l, r = tk.divide_into_two()
                                    l >> 2
                                    r >> 2
                                    k = l+r
                                    res = str(k)
                                    conn.execute("INSERT INTO key1 VALUES('%s')" % res)

conn.commit()
conn.close()
