with open("./onlytext.txt","r") as f:
    buf = f.readline()

arr = [0]*26

for c in buf:
    arr[ord(c) - ord('A')] += 1

print(arr)
s = 0
for i in arr:
    s = s + i*(i-1)
N = len(buf)

I = (1/(N*(N-1)))*s
print(I)
k = (0.0265 * N) // ((0.065 - I) + N*(I - 0.038))
print(k)
