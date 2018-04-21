tbox = { i: None for i in range(8)}

tbox[0] = {0: ['011100', '000001', '111110', '111011'], 1: ['000110', '001111', '100010', '101101'], 2: ['001000', '001011', '101100', '100111'], 3: ['010000', '011101', '111000', '110101'], 4: ['000010', '000111', '100000', '101001'], 5: ['011000', '011011', '111100', '110001'], 6: ['010100', '010011', '101010', '111101'], 7: ['011110', '000101', '110110', '101111'], 8: ['001110', '011111', '100110', '100101'], 9: ['011010', '011001', '110100', '101011'], 10: ['010010', '010001', '111010', '111001'], 11: ['001100', '010111', '101110', '110011'], 12: ['010110', '010101', '110010', '100011'], 13: ['000100', '001101', '101000', '111111'], 14: ['000000', '001001', '100100', '110111'], 15: ['001010', '000011', '110000', '100001']}
tbox[1] = {0: ['011010', '010011', '100000', '111001'], 1: ['000010', '010101', '101110', '100111'], 2: ['010100', '001011', '111100', '101111'], 3: ['001100', '000001', '111010', '101001'], 4: ['001110', '000101', '101010', '101101'], 5: ['011100', '011111', '110000', '111011'], 6: ['001000', '011001', '110110', '110011'], 7: ['010010', '000111', '100100', '110101'], 8: ['000100', '001101', '110010', '100011'], 9: ['010000', '011011', '111000', '111111'], 10: ['011110', '010111', '101000', '100101'], 11: ['001010', '011101', '100110', '110001'], 12: ['011000', '010001', '110100', '110111'], 13: ['010110', '000011', '101100', '100001'], 14: ['000110', '001111', '100010', '111101'], 15: ['000000', '001001', '111110', '101011']}
tbox[2] = {0: ['000010', '000101', '101110', '100111'], 1: ['010000', '011111', '110010', '100001'], 2: ['011100', '010001', '110100', '111101'], 3: ['001010', '001001', '101100', '110111'], 4: ['011010', '001011', '100100', '110001'], 5: ['001110', '010101', '111000', '111011'], 6: ['001000', '001101', '100010', '101001'], 7: ['010110', '000011', '111110', '101111'], 8: ['011110', '010011', '101000', '101101'], 9: ['000100', '000111', '100110', '101011'], 10: ['000000', '001111', '111010', '100011'], 11: ['011000', '011011', '110000', '111001'], 12: ['010100', '011001', '110110', '111111'], 13: ['010010', '000001', '100000', '100101'], 14: ['000110', '010111', '111100', '110101'], 15: ['001100', '011101', '101010', '110011']}
tbox[3] = {0: ['001000', '001101', '100110', '100101'], 1: ['010000', '011001', '110010', '101011'], 2: ['010010', '010101', '111010', '111101'], 3: ['000110', '001111', '110100', '100001'], 4: ['011100', '010001', '111110', '110011'], 5: ['010110', '000111', '111000', '110101'], 6: ['001010', '001001', '100010', '100111'], 7: ['000000', '010011', '101100', '111011'], 8: ['010100', '000011', '111100', '101111'], 9: ['001100', '011111', '100100', '110001'], 10: ['001110', '011011', '100000', '101001'], 11: ['011000', '000101', '101010', '110111'], 12: ['011010', '010111', '101000', '111001'], 13: ['000010', '000001', '101110', '101101'], 14: ['000100', '011101', '110110', '111111'], 15: ['011110', '001011', '110000', '100011']}
tbox[4] = {0: ['011010', '010011', '111100', '110101'], 1: ['000110', '001111', '100100', '101001'], 2: ['000000', '000101', '100010', '101101'], 3: ['010100', '011001', '111010', '111111'], 4: ['000100', '001001', '100000', '111011'], 5: ['010010', '010001', '110110', '111101'], 6: ['001110', '011111', '111000', '110001'], 7: ['001000', '001011', '101100', '100111'], 8: ['010000', '011101', '101110', '100011'], 9: ['011110', '011011', '110010', '110111'], 10: ['001010', '010111', '101000', '111001'], 11: ['001100', '000011', '100110', '100001'], 12: ['000010', '000111', '110100', '100101'], 13: ['011000', '001101', '101010', '101111'], 14: ['011100', '000001', '111110', '101011'], 15: ['010110', '010101', '110000', '110011']}
tbox[5] = {0: ['010000', '011001', '110010', '111011'], 1: ['000010', '010011', '111000', '110101'], 2: ['001010', '000111', '101000', '100101'], 3: ['010100', '011101', '101110', '100011'], 4: ['010110', '000101', '110100', '100001'], 5: ['011100', '001111', '100110', '101011'], 6: ['001100', '010001', '111110', '111001'], 7: ['011010', '001001', '110000', '110111'], 8: ['001110', '011111', '101010', '111101'], 9: ['001000', '001101', '100000', '101001'], 10: ['000100', '000001', '110110', '101111'], 11: ['011110', '011011', '111100', '110001'], 12: ['000000', '001011', '101100', '100111'], 13: ['010010', '010101', '111010', '111111'], 14: ['011000', '010111', '100010', '110011'], 15: ['000110', '000011', '100100', '101101']}
tbox[6] = {0: ['001010', '000011', '111000', '110101'], 1: ['011110', '001101', '100000', '101001'], 2: ['000100', '011001', '111110', '111011'], 3: ['010000', '010011', '101010', '111101'], 4: ['000000', '001001', '100010', '101011'], 5: ['011000', '010101', '111010', '110011'], 6: ['011100', '011111', '110100', '100001'], 7: ['010110', '000111', '101100', '101111'], 8: ['001100', '011101', '110110', '100111'], 9: ['010100', '001011', '111100', '110001'], 10: ['011010', '001111', '110000', '101101'], 11: ['000010', '000101', '100100', '100011'], 12: ['010010', '010111', '101000', '111111'], 13: ['001110', '000001', '100110', '100101'], 14: ['000110', '010001', '101110', '111001'], 15: ['001000', '011011', '110010', '110111']}
tbox[7] = {0: ['011010', '011001', '110000', '110111'], 1: ['001110', '000001', '100110', '100011'], 2: ['000010', '011111', '101110', '100001'], 3: ['010100', '001011', '111010', '111001'], 4: ['000110', '001111', '100100', '101001'], 5: ['011000', '010011', '111100', '111011'], 6: ['001000', '010101', '110010', '111101'], 7: ['011110', '001101', '100000', '100111'], 8: ['000100', '000111', '111110', '101101'], 9: ['010010', '011101', '101000', '110101'], 10: ['010000', '001001', '110100', '101011'], 11: ['001100', '010111', '100010', '111111'], 12: ['011100', '010001', '101010', '110011'], 13: ['000000', '000101', '110110', '101111'], 14: ['010110', '011011', '101100', '100101'], 15: ['001010', '000011', '111000', '110001']}