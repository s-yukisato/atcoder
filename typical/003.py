from collections import deque
import sys
input = sys.stdin.readline

def MI(): return map(int, input().split())

n = int(input())


class Node:
    def __init__(self, index):
        self.index = index
        self.nears = []
        self.sign = -1


nodes = [Node(i) for i in range(n+1)]

for _ in range(n-1):
    a, b = MI()
    nodes[a].nears.append(nodes[b])
    nodes[b].nears.append(nodes[a])

def dfs(i):
    que = deque()
    mx = 0
    que.append(nodes[i])
    nodes[i].sign = 0
    nd = 0
    while que:
        node = que.popleft()
        for near in node.nears:
            if near.sign != -1:
                continue
            near.sign = node.sign + 1
            que.append(near)
    for node in nodes:
        if node.sign > mx:
            mx = node.sign
            nd = node.index
        node.sign = -1
    return (nd, mx)

r, _ = dfs(1)
_, ans = dfs(r)
print(ans + 1)
