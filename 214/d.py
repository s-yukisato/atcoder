import sys
sys.setrecursionlimit(10**6)

n = int(input())

edges = []

for _ in range(n-1):
    u, v,w = map(int, input().split())
    u-=1
    v-=1
    edges.append((w, u, v))

edges.sort()

par = [-1]*n


def find(x):
    if par[x] < 0: return x
    par[x] = find(par[x])
    return par[x]

def unite(x, y):
    x = find(x)
    y = find(y)
    par[x] += par[y]
    par[y] = x 

def size(x):
    x = find(x)
    return -par[x]

ans = 0

for w, u, v in edges:
    ans += w *size(u) * size(v)
    unite(u, v)

print(ans)