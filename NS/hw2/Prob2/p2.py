from __future__ import print_function
from BitVector import *
from m_tables import *


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
                #i = random.randint(0, bv1.length() - 1)
                #temp[i] = 1 - temp[i]
                res = des(temp, 3)
                analyse(block_no, ev, res)
                #
            else:
                ev = des(bv1, 0)
                cipher_bits.append(ev.deep_copy())
                #i = random.randint(0, 63)
                #bv1[i] = 1 - bv1[i]
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
    print(" Average when 1 bit of plain text changed per block ", res[0])
    print(" Average when 1 bit of plain text changed per block and Custom SBox1 used ", res[1])
    print(" Average when 1 bit of plain text changed per block and Custom SBox2 used ", res[2])

    print("\n\n")
    prev_inserted = set()
    total_changed_bits = 0
    for i in range(0,64):
        mkey = key.deep_copy()
        x = random.randint(0,63)
        while x in prev_inserted:
            x = random.randint(0,63)
        prev_inserted.add(x)
        mkey[x] = 1 - mkey[x]
        getEncryptionKeys(mkey)
        enc_message(True)
        for j in range(0,len(modified_key_cipher_bits)):
            for k in range(0, 64):
                if cipher_bits[j][k] != modified_key_cipher_bits[j][k]:
                    total_changed_bits += 1
    r = float(total_changed_bits)/64
    print("Average when randomly 1 bit of key changed for 64 iterations ",r)

if __name__ == "__main__":
    main()




