n = int(input())
a, b = map(int, input().split())

l = [0] * (n + max(a, b))
l[0] = 1

cnt = 0

for i in range(n):
    if l[i] == 0:
        cnt += 1
    else:
        l[i + a] = 1
        l[i + b] = 1
        
print(cnt)