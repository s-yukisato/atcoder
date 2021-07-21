cnt = {}

a = list(map(int,input().split()))

for e in a:
    if e not in cnt:
        cnt[e] = 0
    cnt[e] += 1

print(cnt)