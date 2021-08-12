n = int(input())
a = list(map(int, input().split()))
s = sorted(a, reverse=True)

print(a.index(s[1]) + 1)