from typing import Collection


form collections import deque

que = deque()

N, Q = map(int, input().split())

#　各頂点が連結している頂点のリスト
connect = [[] for _ in range(N+1)]

# 繋がっている頂点の受け取り
for _ in range(N-1):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)

#　各頂点のカウンタを用意
counter = [0] * (N+1)

for _ in range(Q):
    p, x = map(int, input().split())
    counter[p] += x

#　訪問済みリスト
visited = [False] * (N+1)

# ==========　実装　==============

# スタート地点をqueにぶち込む
que.append(1)
# 訪問済みに１を追加する
visited[1] = True

# queが空っぽになったら終了
while que:
    # queの左側から出す
    now = que.popleft()
    # nowのカウンタの値を取り出す
    now_number = counter[now]
    # nowから繋がっている頂点を順に回る
    for to in connect[now]:
        if visited[to]:
            continue
        counter[to] += now_number
        visited[to] = True
        que.append(to)

print(*counter[1:])