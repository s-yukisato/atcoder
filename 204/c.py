a, b, c = map(int, input().split())

if c % 2 == 0:
    c = 2
else:
    c = 1

if pow(a, c) == pow(b, c):
    print("=")
else:
    print(">" if pow(a, c) > pow(b, c) else "<")
