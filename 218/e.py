N, M = map(int, input().split())

G = [[] for _ in range(N)]

score = []

for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
    score.append((c, a, b))

score.sort(reverse=True)

ans = 0

for c, a, b in score:
    if c <= 0:
        break
    if len(G[a]) >= 2 and len(G[b]) >= 2: 
        ans += c
        G[a].remove(b)
        G[b].remove(a)

print(ans)