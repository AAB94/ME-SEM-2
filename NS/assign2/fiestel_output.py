'''
Reads the 64 bit block from file. We find result of Fiestel block for Round 1 and Round 2.
'''

from BitVector import BitVector

if __name__ == "__main__":
    bv = BitVector(filename="sample_ciphertext.txt")
    bv1 = bv.read_bits_from_file(64)
    L2, R2 = bv1.divide_into_two()
    L2, R2 = R2, L2
    bv = BitVector(filename="sample_plaintext.txt")
    bv1 = bv.read_bits_from_file(64)
    L0, R0 = bv1.divide_into_two()

    f1 = L2 ^ L0
    f2 = R2 ^ R0

    fil0 = open("store/f1.txt", "wb")
    fil1 = open("store/f2.txt", "wb")

    f1.write_to_file(fil0)
    f2.write_to_file(fil1)
