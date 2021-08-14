from collections import deque
import sys


def main():
    input = sys.stdin.readline

    class Node:
        def __init__(self, row, col) -> None:
            self.row = row
            self.col = col
            self.nears = [[row, col+1], [row+1, col],
                          [row, col-1], [row-1, col]]
            self.sign = False

    h, w = map(int, input().split())
    field = [list(input()) for _ in range(h)]

    def isInside(x, y):
        return 0 <= x < w and 0 <= y < h
    
    que = deque()

    nodes = []
    for i in range(h):
        nodes.append([])
        for j in range(w):
            nodes[i].append(Node(i,j))
            if field[i][j] == "s":
                que.append(nodes[i][j])
                nodes[i][j].sign = True
    
    while que:
        node = que.pop()
        nears = node.nears
        for y, x in nears:
            if isInside(x, y) == False:
                continue
            if nodes[y][x].sign == False:
                if field[y][x] == ".":
                    nodes[y][x].sign = True
                    que.append(nodes[y][x])
                elif field[y][x] == "g":
                    print("Yes")
                    exit()
    
    print("No")

if __name__ == "__main__":
    main()

