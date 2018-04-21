from BitVector import BitVector
from tbox import *
import sqlite3

expansion_permutation = [31, 0, 1, 2, 3, 4, 3, 4, 5, 6, 7, 8,
                         7, 8, 9, 10, 11, 12, 11, 12, 13, 14,
                         15, 16, 15, 16, 17, 18, 19, 20, 19,
                         20, 21, 22, 23, 24, 23, 24, 25, 26,
                         27, 28, 27, 28, 29, 30, 31, 0]

pbox = [15, 6, 19, 20, 28, 11, 27, 16, 0, 14, 22,
        25, 4, 17, 30, 9, 1, 7, 23, 13, 31, 26,
        2, 8, 18, 12, 29, 5, 21, 10, 3, 24]

bv = BitVector(filename="store/f2.txt")

bv1 = bv.read_bits_from_file(32)

d = bv1.unpermute(pbox)

bv = BitVector(filename="sample_ciphertext.txt")
bv1 = bv.read_bits_from_file(64)
L2, R2 = bv1.divide_into_two()
L2, R2 = R2, L2

L2 = L2.permute(expansion_permutation)

arr = []
for i in range(0, 32, 4):
    arr.append(int(d[i:i+4]))

arr1 = []

for i in range(8):
    arr1.append(tbox[i][arr[i]])

conn = sqlite3.connect('store/possib_k1.db')


for a in arr1[0]:
    for b in arr1[1]:
        for c in arr1[2]:
            for d in arr1[3]:
                for e in arr1[4]:
                    for f in arr1[5]:
                        for g in arr1[6]:
                            for h in arr1[7]:
                                res = str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)
                                bres = BitVector(bitstring=res) ^ L2
                                res = str(bres)
                                conn.execute("INSERT INTO possib_key(key) VALUES('%s')" % res)
conn.commit()
conn.close()