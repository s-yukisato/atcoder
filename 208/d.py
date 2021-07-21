n, m = list(map(int, input().split()))
array = []
for i in range(n+1):
    array.append([0] * (n + 1))

for i in range(m):
    a, b, c = list(map(int, input().split()))
    array[a][b] = c
print(array)

count = 0

for k in range(n):
    for t in range(n):
        for s in range(n):
            if s == t:
                print(0)