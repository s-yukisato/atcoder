from pprint import pprint
from collections import deque
from heapq import heappush, heappop
import sys
input = sys.stdin.readline
def II(): return int(input())
def II_(): return input()
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI_(): return list(input())
def TL(n): return [list(map(int, input().split())) for _ in range(n)]
def TL_(n): return [list(input()) for _ in range(n)]


def yn(judge, yes="Yes", no="No"): print(yes if judge else no)


MOD = 10 ** 9 + 7


INF = 10 ** 9

n = II()

links = [[0] * (n+1) for _ in range(n+1)]


class Node:
    def __init__(self, index):
        self.index = index
        self.nears = []
        self.sign = -1


nodes = []
for i in range(n+1):
    nodes.append(Node(i))

for _ in range(n-1):
    u, v, w = MI()
    links[u][v] = w
    links[v][u] = w
    nodes[u].nears.append(nodes[v])
    nodes[v].nears.append(nodes[u])



que = deque()
que.append(nodes[1])
nodes[1].sign = 0

ans = []
while que:
    node = que.popleft()
    nears = node.nears
    ans.append(node.index)
    for near in nears:
        if near.sign == -1:
            que.append(near)
            near.sign = node.index
            for a in ans:
                if links[a][near.index] == 0:
                    links[a][near.index] = links[node.index][near.index]
                if links[near.index][a] == 0:
                    links[near.index][a] = links[node.index][near.index]


pprint(links)

sum_ = 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        sum_ += links[i][j]

print(sum_)