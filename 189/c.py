n = int(input())
a = list(map(int, input().split()))

INF = 10**9
ans = 0

for l in range(n):
    x = INF
    for r in range(l, n):
        x = min(x, a[r])
        ans = max(ans, x * (r - l + 1))

print(ans)