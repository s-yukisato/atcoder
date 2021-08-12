n = int(input())
v = sorted(list(map(int, input().split())))
tmp = v[0]
for i in range(1, n):
    tmp = (tmp + v[i]) /2
print(tmp)


import numpy as np

h, w = map(int, input().split())
s = np.array([[0] + list(map(int, input().split())) + [0] for _ in range(h)])

for row in range(h-1):
    for col in range(w):
        maxValue = max(s[row][col], s[row][col + 1], s[row][col + 2])
        target = s[row+1][col+1]
        s[row+1][col+1] = max(s[row+1][col+1], maxValue)
        

print(s)