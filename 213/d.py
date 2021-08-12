from collections import deque


class Node:
    def __init__(self, index) -> None:
        self.index = index
        self.connect = []
        self.sign = -1


n = int(input())

nodes = []
for i in range(n+1):
    nodes.append(Node(i))

for _ in range(n-1):
    a, b = map(int, input().split())
    nodes[a].connect.append(b)
    nodes[b].connect.append(a)

for node in nodes:
    node.connect.sort()

que = deque()
que.append(1)
nodes[1].sign = 1

route = []

while que:
    now = nodes[que.pop()]
    route.append(now.index)
    for to in now.connect:
        if nodes[to].sign < 0:
            que.append(nodes[to].index)
            nodes[to].sign = now.index
            break
    else:
        if now.index != 1:
            que.append(now.sign)

print(*route)
