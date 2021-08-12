from collections import deque

INF = 10**9

h, w = map(int, input().split())
s = [input() for _ in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j] == "s":
            sx = 1
            sy = 1
        elif s[i][j] == "g":
            gx = 1
            gy = 1

deq = deque([(sx, sy)])
distance = [[INF] * w for _ in range(h)]
distance[sx][sy] = 0
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 移動方向

while deq:
    x, y = deq.popleft()
    for dx, dy in d:
        if 0 <= x+dx < h and 0 <= y + dy < w and distance[x+dx][y+dy] == INF:
            if s[x+dx][y+dy] == "#":
                distance[x+dx][y+dy] = distance[x][y] + 1
                deq.append((x+dx, y+dy))
            else:
                distance[x+dx][y+dy] = distance[x][y]
                deq.appendleft((x+dx, y+dy))

print("Yes" if distance[gx][gy] <= 2 else "No")