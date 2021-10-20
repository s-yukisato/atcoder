N, P = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0

for i in A:
    if i < P:
        cnt += 1

print(cnt)
