from bisect import bisect_left

INF = float('inf')

n = int(input())
a = list(map(int, input().split())) + [-INF, INF]
a.sort()
q = int(input())
for _ in range(q):
    b = int(input())
    idx = bisect_left(a, b)
    s = min(abs(a[idx-1]-b), abs(a[idx]-b))
    print(s)


