from collections import deque

n, q = map(int, input().split())

class Node:
    def __init__(self):
        self.connect = []
        self.isVisited = False
        self.counter = 0

nodeList = []
for _ in range(n+1):
    nodeList.append(Node())

for _ in range(n-1):
    a, b = map(int, input().split())
    nodeList[a].connect.append(nodeList[b])
    nodeList[b].connect.append(nodeList[a])

for _ in range(q):
    p, x = map(int, input().split())
    nodeList[p].counter += x

que = deque()
start = nodeList[1]
start.isVisited = True
que.append(start)


while que:
    nowNode = que.popleft()
    for toNode in nowNode.connect:
        if toNode.isVisited:
            continue
        toNode.counter += nowNode.counter
        toNode.isVisited = True
        que.append(toNode)

for node in nodeList[1:]:
    print(node.counter, end=" ")