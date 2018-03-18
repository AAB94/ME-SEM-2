from __future__ import print_function
from BitVector import *
import random

########################################################################################################################
#file is for modified sboxes

# variables starting with _ are not adjusted for array index values

#Initial and post shift permutation for Key Rounds
pc1 = [56,48,40,32,24,16,8,0,57,49,41,33,25,17,
       9,1,58,50,42,34,26,18,10,2,59,51,43,35,
       62,54,46,38,30,22,14,6,61,53,45,37,29,21,
       13,5,60,52,44,36,28,20,12,4,27,19,11,3]

pc2 = [13,16,10,23,0,4,2,27,14,5,20,9,22,18,11,
       3,25,7,15,6,26,19,12,1,40,51,30,36,46,
       54,29,39,50,44,32,47,43,48,38,55,33,52,
       45,41,49,35,28,31]

shift_round = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]


# expansion of right 32 bit to 48
exp_perm =  [31,  0,  1,  2,  3,  4,
              3,  4,  5,  6,  7,  8,
              7,  8,  9, 10, 11, 12,
             11, 12, 13, 14, 15, 16,
             15, 16, 17, 18, 19, 20,
             19, 20, 21, 22, 23, 24,
             23, 24, 25, 26, 27, 28,
             27, 28, 29, 30, 31, 0]
# Post Sbox Permutation
_perm = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
]

perm = []

for i in _perm:
    perm.append(i-1)


#Initial and Inverse of Initial Permutation of DES
_ip = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

ip = []

for i in _ip:
    ip.append(i-1)

_inverse_ip = [
     40, 8, 48, 16, 56, 24, 64, 32,
     39, 7, 47, 15, 55, 23, 63, 31,
     38, 6, 46, 14, 54, 22, 62, 30,
     37, 5, 45, 13, 53, 21, 61, 29,
     36, 4, 44, 12, 52, 20, 60, 28,
     35, 3, 43, 11, 51, 19, 59, 27,
     34, 2, 42, 10, 50, 18, 58, 26,
     33, 1, 41, 9, 49, 17, 57, 25
]

inverse_ip = []
for i in _inverse_ip:
    inverse_ip.append(i-1)


#Sboxes

s_boxes = { i:{} for i in range(3)}

s_boxes[0][0] = [ [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
               [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
               [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
               [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13] ]

s_boxes[0][1] = [ [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
               [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
               [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
               [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9] ]

s_boxes[0][2] = [ [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
               [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
               [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
               [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12] ]

s_boxes[0][3] = [ [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
               [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
               [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
               [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14] ]

s_boxes[0][4] = [ [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
               [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
               [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
               [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3] ]

s_boxes[0][5] = [ [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
               [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
               [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
               [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13] ]

s_boxes[0][6] = [ [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
               [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
               [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
               [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12] ]

s_boxes[0][7] = [ [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
               [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
               [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
               [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11] ]



#v v inidactes which sbox version
for v in range(1,3):
    for s_no in range(8):
        s_boxes[v][s_no] = []
        for r in range(4):
            s_boxes[v][s_no].append(random.sample(range(0,16),16))

############################################################################################################



#key file
key_filename = 'key.txt'

#message file
msg_filename = 'message.txt'

#holds key for all 16 rounds
key_round = []

# Stores tuples regarding round_no,no_of_change when 1 bit plain text changed

analysis_list = []

cipher_bits = [] # holds 64 bit cipher created with plain text that has not been modified and Sbox mentioned in Assignment file
modified_key_cipher_bits = []


def getEncryptionKeys(key):
    global key_round
    key_round = []
    mkey = key.deep_copy()
    mkey = mkey.permute(pc1)
    left, right = mkey.divide_into_two()
    for r in shift_round:
        left<<r
        right<<r
        k = left + right
        k = k.permute(pc2)
        key_round.append(k.deep_copy())


def read_key():
    bv = BitVector(filename='./'+key_filename)
    bv1 = bv.read_bits_from_file(64)
    bv.close_file_object()
    return bv1


def enc_message(key_mod):
    bv = BitVector(filename='./'+msg_filename)
    bv1 = bv.read_bits_from_file(64)
    block_no = 0  # Number of 64 bit blocks
    if not key_mod:
        while bv1.length() > 0:
            if bv1.length() < 64:
                pad = 64 - bv1.length()
                temp = bv1 + BitVector(intVal=0, size=pad)
                ev = des(temp, 0)
                cipher_bits.append(ev.deep_copy())
                i = random.randint(0, bv1.length() - 1)
                temp[i] = 1 - temp[i]
                res = des(temp, 3)
                analyse(block_no, ev, res)
                #
            else:
                ev = des(bv1, 0)
                cipher_bits.append(ev.deep_copy())
                i = random.randint(0, 63)
                bv1[i] = 1 - bv1[i]
                res = des(bv1, 3)
                analyse(block_no, ev, res)
                #
            block_no += 1
            bv1 = bv.read_bits_from_file(64)
    else:
        global modified_key_cipher_bits
        modified_key_cipher_bits = []
        while bv1.length() > 0:
            if bv1.length() < 64:
                pad = 64 - bv1.length()
                temp = bv1 + BitVector(intVal=0, size=pad)
                ev = des(temp, 0)
                modified_key_cipher_bits.append(ev.deep_copy())
                #
            else:
                ev = des(bv1, 0)
                modified_key_cipher_bits.append(ev.deep_copy())
                #
            bv1 = bv.read_bits_from_file(64)
    bv.close_file_object()


def des(msg, v):
    if v == 0:
        msg = msg.deep_copy()
        msg = msg.permute(ip)
        left, right = msg.divide_into_two()
        for i in range(0, 16):
            temp_right = substitute(right,key_round[i],v)
            temp_right = left ^ temp_right
            left, right = right, temp_right
        msg = right + left
        msg = msg.permute(inverse_ip)
        return msg
    else:
        res = []
        for j in range(0, 3):
            tmsg = msg.deep_copy()
            tmsg = tmsg.permute(ip)
            left, right = tmsg.divide_into_two()
            for i in range(0, 16):
                temp_right = substitute(right,key_round[i],j)
                temp_right = left ^ temp_right
                left, right = right, temp_right
            tmsg = right + left
            tmsg = tmsg.permute(inverse_ip)
            res.append(tmsg)
        return res


def substitute(right,key,sbox_ver):
    mright = right.deep_copy()
    mright = mright.permute(exp_perm)
    mright = mright ^ key
    count = 0
    sv = []
    for i in range(0,43,6):
        t = mright[i:i+6]
        r = str(t[0]) + str(t[5])
        c = t[1:5]
        x = s_boxes[sbox_ver][count][int(r, 2)][int(c)]
        sv.append(BitVector(intVal=x, size=4))
        count += 1
    rsv = sv[0]
    for i in range(1, len(sv)):
        rsv = rsv + sv[i]
    rsv = rsv.permute(perm)
    return rsv

#ev, mev modified ev
def analyse(block_no,ev,res):
    mev= []
    for i in res:
        mev.append(i)
    changed_bits = [0,0,0] # no of changed bits
    for i in range(3):
        for j in range(0,64):
            if ev[j] != mev[i][j]:
                changed_bits[i] += 1
    analysis_list.append((block_no,changed_bits))


def main():
    key = read_key()
    getEncryptionKeys(key)
    enc_message(False)
    s = [0,0,0]
    for i in range(3):
        for j in range(len(analysis_list)):
            s[i] += analysis_list[j][1][i]
    res = []
    for i in range(3):
        t = float(s[i])/float(analysis_list[len(analysis_list) - 1][0] + 1)
        res.append(t)
    print(" Average when 1 bit of plain text changed per block : ", res[0])
    print(" Average when 1 bit of plain text changed per block and Custom SBox1 used : ", res[1])
    print(" Average when 1 bit of plain text changed per block and Custom SBox2 used : ", res[2],"\n")


    total_changed_bits = 0
    bit_index_to_change_in_key = random.sample(range(0,20),20)
    for i in bit_index_to_change_in_key:
        mkey = key.deep_copy()
        mkey[i] = 1 - mkey[i]
        getEncryptionKeys(mkey)
        enc_message(True)
        for j in range(0, len(modified_key_cipher_bits)):
            for k in range(0, 64):
                if cipher_bits[j][k] != modified_key_cipher_bits[j][k]:
                    total_changed_bits += 1
    r = float(total_changed_bits)/64
    print("Average when randomly 1 bit of key changed for 20 iterations : ",r,"\n")

if __name__ == "__main__":
    main()




