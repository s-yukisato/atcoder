n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
t = 0
if k%n != 0:
    t = sorted(a)[k%n -1]

for i in a:
    if t >= i:
        print(k//n + 1)
    else:
        print(k//n)