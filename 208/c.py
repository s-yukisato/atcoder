n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
num = -1
if k % n != 0:
    num  = sorted(a)[k%n -1]
for i in a:
    if i <= num:
        print(k//n + 1)
    else:
        print(k // n)