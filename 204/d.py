n, q = map(int, input().split())
a = list(map(int, input().split()))
K = [int(input()) for _ in range(q)]


c = []
c.append(a[0] -1)

for i in range(1, n):
    c.append(c[i-1] + a[i] -a[i-1] - 1)

for k in K:
    if k < c[n-1]:
        print(a[n-1] + (k -c[n-1]))
    else:
        print(k)