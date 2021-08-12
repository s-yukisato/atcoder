n = int(input())

ans = 0

for _ in range(n):
    x = int(input())
    
    if 100_000 < x <= 750_000:
        tmp = min(650_000, x - 100_000)
        ans += tmp * 0.1
    if 750_000 < x <= 1_500_000:
        tmp = min(750_000, x - 750_000)
        ans += tmp * 0.2
    if x > 1_500_000:
        ans += (x - 1_500_000) * 0.4 
print(ans)