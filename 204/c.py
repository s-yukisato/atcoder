from collections import deque
import sys

input = sys.stdin.readline


class Node:
    def __init__(self, index):
        self.index = index
        self.nears = []
        self.sign = False

n, m = map(int, input().split())

nodes = [Node(i) for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    nodes[a].nears.append(nodes[b])

ans = 0

for i in range(1, n+1):
    ans += 1
    que = deque()
    que.append(nodes[i])
    nodes[i].sign = True
    cnt = 0
    while que:
        node = que.popleft()
        nears = node.nears
        for near in nears:
            if near.sign == False:
                cnt += 1
                near.sign = True
                que.append(near)
    ans += cnt
    for j in range(1, n+1):
        nodes[j].sign = False

print(ans)