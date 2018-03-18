'''
Key prediction
'''
def readfile():
    with open("./onlytext.txt","r") as f:
        buf = f.readline()
    return buf


def ngramfinder(ngram, buf):
    e = len(buf)
    ngram_len = [3,4,5,6,7]
    for i in ngram_len:
        if i < e: 
            for j in range(e - i + 1):
                temp = buf[j:j+i]
                ngram.add(temp)
            

def freq_finder(ngram,buf):
    e  = len(buf)
    fc = {}
    dist = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    for d in dist:
        fc[d] = 0 
    for d in dist:
        for k in ngram:
            nl = len(k)
            for i in range(0 ,e - nl + 1, d):
                for j in dist:
                    temp = buf[i:i+j]
                    #print(temp)                
                    if temp == k:
                        fc[d] += 1
                        #print(i,temp)
    return fc


def main():
    buf = readfile()
    #buf = "abc"
    ngram = set()
    ngramfinder(ngram, buf)
    fc = freq_finder(ngram,buf)
    print(fc) 
    #print(ngram)   

if __name__ == "__main__":
    main()
