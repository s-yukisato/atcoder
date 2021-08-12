from collections import deque


class Node:
    def __init__(self, index) -> None:
        self.index = index
        self.nears = []
        self.sign = -1

    def __repr__(self) -> str:
        return f'Node index:{self.index} nears:{self.nears} sign: {self.sign}'


n, m = map(int, input().split())

links = [list(map(int, input().split())) for _ in range(m)]

nodes = []
for i in range(n + 1):
    nodes.append(Node(i))

for j in range(m):
    edge_start, edge_end = links[j]
    nodes[edge_start].nears.append(edge_end)
    nodes[edge_end].nears.append(edge_start)

queue = deque()
# root node
queue.append(nodes[1])

while queue:
    node = queue.popleft()
    nears = node.nears

    print(queue)

    for near in nears:
        if nodes[near].sign == -1:
            queue.append(nodes[near])
            nodes[near].sign = node.index

if -1 in [node.sign for node in nodes][2:]:
    print("No")
    exit(0)
else:
    print("Yes")

for k in range(2, n + 1):
    print(nodes[k].sign)