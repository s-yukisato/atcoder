N = int(input())

G = [[] for _ in range(N)]

for i in range(N-1):
    a, b = map(int, input().split())
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)

ans = False

for i in range(N):
    if len(G[i]) == N-1:
        ans = True 

print("Yes" if ans else "No")