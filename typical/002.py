from itertools import product

n = int(input())

if n % 2 == 1:
    exit()

for s in product(['(', ')'], repeat=n):
    cnt = 0
    for j in range(n):
        cnt += [-1, 1][s[j] == "("]
        if cnt < 0: break
    if cnt == 0:
        print(''.join(s))
