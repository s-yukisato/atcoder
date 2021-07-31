import collections



n, k = map(int, input().split())
c = collections.deque(list(map(int, input().split())))

ans = 0
check = []
for _ in c:
    check.append(c.pop(0))

col = collections.Counter(check)
ans = max(ans, len(col))

for i in range(1, n-k):
    
    col = collections.Counter(check)
    ans = max(ans, len(col))

print(ans)