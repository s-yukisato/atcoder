n, m = map(int, input().split())

row = -1
if m % n == 0:
    row = m // n - 1
else:
    row = m // n

if row % 2 == 0:
    dif = ((row+1) * n) - m
    print(m + 2*dif + 1)
else:
    dif = m - (row * n)
    print(m - 2*dif + 1)