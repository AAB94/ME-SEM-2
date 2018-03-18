import random
import os
# random module imported in parent file so not importing again.
s_boxes = { x:{} for x in range(2)}

random.seed(os.urandom(1))


#v v inidactes which sbox version
for v in range(2):
    for s_no in range(8):
        s_boxes[v][s_no] = [[0]*16, [0]*16, [0]*16, [0]*16]
        for r in range(4):
    #prev_inserted holds values inserted previously used to check if array will have unqiue values only
            prev_inserted = set()
            for c in range(16):
                x = random.randint(0,15)
                while x in prev_inserted:
                    x = random.randint(0,15)
                prev_inserted.add(x)
                s_boxes[v][s_no][r][c] = x

for v in range(2):
    print "\tsbox version "+str(v)
    for s_no in range(8):
        print "s_box "+str(s_no)
        print s_boxes[v][s_no]



