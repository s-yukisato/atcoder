from collections import deque
from pprint import pprint

h, w = map(int, input().split())
maze = [input() for _ in range(h)]

# スタート地点とゴール地点
sx = 0
sy = 0
gx = w-1
gy = h-1

INF = int(1e9)
score = [[INF] * w for _ in range(h)]

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)


def bfs():
    que = deque()
    que.append([sy, sx])
    score[sy][sx] = 0

    while que:
        pprint(score)
        y, x = que.popleft()
        if y == gy and x == gx:
            break
        tmp = score[y][x]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not (0 <= nx < w and 0 <= ny < h):
                continue
            if maze[ny][nx] != "#" and score[ny][nx] > tmp:
                score[ny][nx] = tmp
                que.appendleft([ny, nx])
        for i in range(-2, 3):
            for j in range(-2, 3):
                ny = y + i
                nx = x + j
                if not (0 <= nx < w and 0 <= ny < h) or abs(i) + abs(j) > 3:
                    continue
                if score[ny][nx] > tmp + 1:
                    score[ny][nx] = tmp + 1
                    que.append([ny, nx])
    return score[gy][gx]

ans = bfs()
print(ans)
