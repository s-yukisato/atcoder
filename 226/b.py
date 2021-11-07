N = int(input())

dist = set()

for _ in range(N):
    L, *A = input().split()
    dist.add("/".join(A))


print(len(dist))