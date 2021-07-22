a, b = map(int, input().split())

if 6 <= a <= 12:
    print(b//2)
elif a > 12:
    print(b)
else:
    print(0)