
import sys
input = sys.stdin.readline

INF = float('inf')
V, E = map(int, input().split())
es = [list(map(int, input().split())) for _ in range(E)]

def bellmanford(s):
    d = [INF] * V
    d[s] = 0

    for i in range(V):
        for j in range(E):
            frm, to, cost = es[j]
            if d[to] > d[frm] + cost:
                d[to] = d[frm] + cost
                if i == V-1:
                    d[to] = -INF
                    while True:
                        update = False
                        for k in range(len(es)):
                            e = es[k]