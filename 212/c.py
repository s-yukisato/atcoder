import bisect

ans = INF = 10 ** 10
n ,m =  map(int, input().split())
a = sorted(list(set(map(int, input().split()))))
b = sorted(list(set(map(int, input().split()))) + [-INF, INF])

for x in a:
    pos = bisect.bisect_right(b, x)
    ans = min(ans, abs(b[pos] -x))
    ans = min(ans, abs(b[pos-1] - x))

print(ans)