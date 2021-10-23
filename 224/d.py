from collections import deque

N = int(input())

G = [[] for _ in range(10)]

for i in range(N):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

A = list(map(int, input().split())) + [0]

correct = [1, 2, 3, 4, 5, 6, 7, 8, 0] 

que = deque([9])
cnt = 0

while que:
    if A == correct:
        break
    cnt += 1
    now = que.pop()
    nears = G[now]
    for to in nears:
        A[now] = to
        A[to] = 0
        que

