N = int(input())

S = list(map(int, input().split()))

pos = set()

for a in range(1, 200):
    for b in range(1, 200):
        pos.add(3*(a+b) + 4*a*b)

cnt = 0

for s in S:
    if s not in pos:
        cnt += 1


print(cnt)