k = int(input())
a = list(map(int, input().split()))

ans = 0
s = a[0] * 4 + a[1] * 2 + a[2]

now = 8
while k != 0:
    if k >= 8:
        ans += s
        t = len(bin(now)) - 3
        ans += a[t]
        k -= 8
        now += 8
    else:
        if k % 4 == 0:
            ans += a[2]
        elif k % 2 == 0:
            ans += a[1]
        else:
            ans += a[0]
        k -= 1

print(ans)