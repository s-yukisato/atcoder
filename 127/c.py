n, m = map(int, input().split())

L = []
R = []

for i in range(m):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

if min(R) - max(L) >= 0:
    print(min(R) - max(L) + 1)
else:
    print(0)
