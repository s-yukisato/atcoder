from bisect import bisect_left
 
n, q = map(int, input().split())
a = list(map(int, input().split()))

s = [a[i] - (i+1) for i in range(n)]
 
for _ in range(q):
    k = int(input())
    i = bisect_left(s, k)
    if i == 0:
        print(k)
    else:
        print(a[i - 1] + (k - s[i - 1]))
