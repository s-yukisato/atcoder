from collections import deque
import sys
input = sys.stdin.readline
def II_(): return input()
def II(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(MI())
def LI_(): return list(II_())
def TL(n): return [list(map(int, input().split())) for _ in range(n)]


class Node:
    def __init__(self, index):
        self.index = index
        self.nears = []
        self.sign = -1


n, m = MI()
links = TL(m)

nodes = []
for i in range(n+1):
    nodes.append(Node(i))

for i in range(m):
    s, e = links[i]
    nodes[s].nears.append(e)
    nodes[e].nears.append(s)

que = deque()
que.append(nodes[1])

while que:
    node = que.popleft()
    nears = node.nears
    for near in nears:
        if nodes[near].sign == -1:
            que.append(nodes[near])
            nodes[near].sign = node.index

if -1 in [node.sign for node in nodes][2:]:
    print("No")
    exit()
else:
    print("Yes")

for k in range(2, n+1):
    print(nodes[k].sign)