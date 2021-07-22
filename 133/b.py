import math

n, d = map(int, input().split())

x = []

for i in range(n):
    x.append(list(map(int, input().split())))

for i in range(n):
    a = x[i]
    for j in range(i+1, n):
        b = x[j]
        sum = 0
        for k in range(len(a)):
            sum += math.sqrt(abs(a[k] - b[k]))
        print(sum)