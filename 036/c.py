n = int(input())
a = [int(input()) for  _ in range(n)]

b = list(set(a))
d = {v: i for i, v in enumerate(b)}

for i in a:
    print(d[i])