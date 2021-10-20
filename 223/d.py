N, M = map(int, input().split())

left = []
right = []

ans = []

for i in range(M):
    a, b = map(int, input().split())
    left.append(a)
    right.append(b)
    ans.append((a, b))

print(left, right)

print(ans)