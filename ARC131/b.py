H, W = map(int, input().split())
field = [list(input()) for _ in range(H)]
 
d = [1, 0, -1, 0]
 
 
def valid(y, x):
    return 0 <= y < H and 0 <= x < W
 
 
for y in range(H):
    for x in range(W):
        if field[y][x] == ".":
            nears = [False] * 6
            for i in range(4):
                ay, ax = d[i], d[(i + 1) % 4]
                ny, nx = y + ay, x + ax
                if valid(ny, nx):
                    if field[ny][nx] != ".":
                        nears[int(field[ny][nx])] = True
            color = nears[1:].index(False) + 1
            field[y][x] = str(color)
 
for row in field:
    print("".join(row))