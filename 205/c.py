a, b, c = map(int, input().split())

c = c % 2 + 2
print([">", "<", "="][(pow(a, c) <= pow(b, c)) + (pow(a, c) == pow(b, c))])