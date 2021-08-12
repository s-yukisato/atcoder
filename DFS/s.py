n, m = map(int, input().split())

l = []
for _ in range(n):
    s = input()
    if s == "work":
        l.append(0)
    else:
        l.append(1)

ans = 0
t = 0
for j in range(n):
    tmp = m
    for i in l:
        if i == 1:
            t += 1
        else:
            if tmp > 0:
                t += 1
                tmp -= 1
            else:
                ans = max(ans, t)
                t = 0


print(ans)
