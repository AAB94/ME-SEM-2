from __future__ import print_function
from BitVector import *
from tables import *


#key file
key_filename = 'key.txt'

#message file
msg_filename = 'encrypted.txt'

#holds key for all 16 rounds
key_round = []


def getEncryptionKeys(key):
    mkey = key.deep_copy()
    mkey = mkey.permute(pc1)
    left, right = mkey.divide_into_two()
    for r in shift_round:
        left<<r
        right<<r
        k = left+right
        k = k.permute(pc2)
        key_round.append(k.deep_copy())
    return key_round


def read_key():
    bv = BitVector(filename='./'+key_filename)
    bv1 = bv.read_bits_from_file(64)
    bv.close_file_object()
    return bv1


def dec_message():
    bv = BitVector(filename='./'+msg_filename)
    bv1 = bv.read_bits_from_file(64)
    output_file = open('./decrypted.txt', 'wb')
    while bv1.length() > 0:
        ev = des(bv1)
        ev.write_to_file(output_file)
        bv1 = bv.read_bits_from_file(64)
    output_file.close()
    bv.close_file_object()


def des(msg):
    global key_round
    msg = msg.permute(ip)
    left, right = msg.divide_into_two()
    for i in range(15,-1,-1):
        temp_right = substitute(right,key_round[i])
        temp_right = left ^ temp_right
        left, right = right, temp_right
    msg = right + left
    msg = msg.permute(inverse_ip)
    return msg


def substitute(right, key):
    mright = right.deep_copy()
    mright = mright.permute(exp_perm)
    mright = mright ^ key
    count = 0
    sv = []
    for i in range(0,43,6):
        t = mright[i:i+6]
        r = str(t[0]) + str(t[5])
        c = t[1:5]
        x = s_boxes[count][int(r, 2)][int(c)]
        sv.append(BitVector(intVal=x, size=4))
        count += 1
    rsv = sv[0]
    for i in range(1, len(sv)):
        rsv = rsv + sv[i]
    rsv = rsv.permute(perm)
    return rsv


def main():
    key = read_key()
    getEncryptionKeys(key)
    dec_message()


if __name__ == "__main__":
    main()




