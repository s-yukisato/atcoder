from collections import deque

h, w = 10, 10


class Node:
    def __init__(self, row, col):
        self.col = col
        self.row = row
        self.nears = [[row, col+1], [row, col-1], [row+1, col], [row-1, col]]
        self.sign = False

def isInside(x, y):
        return 0 <= x < w and 0 <= y < h

nodes = []

field = [list(input()) for _ in range(h)]

islandCount = 0

for i in range(h):
    nodes.append([])
    for j in range(w):
        if field[i][j] == "o":
            islandCount += 1
        nodes[i].append(Node(i, j))

for i in range(h):
    for j in range(w):
        if field[i][j] == "o":
            continue
        que = deque()
        que.append(nodes[i][j])
        nodes[i][j].sign = True

        cnt = 0

        while que:
            node = que.popleft()
            nears = node.nears
            for y, x in nears:
                if isInside(x, y) == False:
                    continue
                if nodes[y][x].sign == False and field[y][x] == "o":
                    cnt +=1
                    que.append(nodes[y][x])
                    nodes[y][x].sign = True
        if cnt == islandCount:
            print("YES")
            exit()
        for a in range(h):
            for b in range(w):
                nodes[a][b].sign = False
print("NO")