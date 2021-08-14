from collections import deque

h, w = map(int, input().split())
class Node:
    def __init__(self, color, row, col):
        self.color = color
        self.col = col
        self.row = row
        self.nears = [[row, col+1], [row, col-1], [row+1, col], [row-1, col]]
        self.sign = -1

def isInside(x, y):
        return 0 <= x < w and 0 <= y < h

blackCount = 0
nodes = []
for i in range(h):
    nodes.append([])
    s = list(input())
    for j in range(len(s)):
        if s[j] == ".":
            nodes[i].append(Node("white", i, j))
        else:
            nodes[i].append(Node("black", i, j))
            blackCount += 1


que = deque()
que.append(nodes[0][0])
nodes[0][0].sign = 1

while que:
    node = que.popleft()
    nears = node.nears
    for y, x in nears:
        if isInside(x, y) == False:
            continue
        if nodes[y][x].sign == -1 and nodes[y][x].color == "white":
            que.append(nodes[y][x])
            nodes[y][x].sign = node.sign + 1
        if y == h-1 and x == w-1:
            print(h*w - blackCount - nodes[y][x].sign)
            exit()

print(-1)
                                     
