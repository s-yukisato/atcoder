n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ma = max(a)
mb = min(b)

if mb-ma < 0:
    print(0)
else:
    print(mb-ma + 1)