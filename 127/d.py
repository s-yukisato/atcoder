from collections import deque

d = deque()

n, m = map(int, input().split())
a = list(map(int, input().split()))

store = []

for i in range(m):
    b, c = map(int, input().split())
    store.append([c, b])

store.sort(reverse=True)

ans = 0

d = sorted(a)

for i in range(m):
    if len(d) != 0:
        if d[0] < store[i][0]:
            b = store[i][1] 
            while b > 0 and d[0] < store[i][0] and len(d) != 0:
                ans += store[i][0]
                d.pop(0)
                b-=1


print(ans + sum(d))

