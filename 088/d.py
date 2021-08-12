from collections import deque

class Node:
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col
        self.nears = [[row-1, col], [row, col-1], [row+1, col], [row, col+1]]
        self.sign = -1

h, w = map(int, input().split())
pic = []
for i in range(h):
    pic.append(list(input()))

nodes = []
kuro = 0
for i in range(h):
    nodes.append([])
    for j in range(w):
        nodes[i].append(Node(i, j))
        if pic[i][j] == "#":
            kuro += 1