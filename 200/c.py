c = int(input())
a = list(map(int, input().split()))

mp = set()
ans = 0
for i in range(c):
    tmp = a[i]
    for j in range(i+1, c):
        if (tmp - a[j]) %200 == 0:
            ans += 1

print(ans)

