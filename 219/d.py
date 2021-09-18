N = int(input())
X, Y = map(int, input().split())
 
goods = [list(map(int, input().split())) for _ in range(N)]
goods.sort()
 
INF = float('inf')
 
dp_takoyaki = [[0] * (X+1) for _ in range(N+1)]
dp_taiyaki = [[0] * (Y+1) for _ in range(N+1)]
 
for i in range(N):
    for x in range(X+1):
        if x - goods[i][0] < 0:
            dp_takoyaki[i+1][x] = dp_takoyaki[i][x]
        else:
            dp_takoyaki[i+1][x] = max(dp_takoyaki[i][x-goods[i][0]]+goods[i][1], dp_takoyaki[i][x])
 
 
for i in range(N):
    for y in range(Y+1):
        if y - goods[i][1] < 0:
            dp_taiyaki[i+1][y] = dp_taiyaki[i][y]
        else:
            dp_taiyaki[i+1][y] = max(dp_taiyaki[i][y-goods[i][1]]+goods[i][0], dp_taiyaki[i][y])
 
takoyaki_min = INF
taiyaki_min = INF
for i in range(N+1):
    if dp_takoyaki[i][X] >= Y:
        takoyaki_min = min(takoyaki_min, i)
    if dp_taiyaki[i][Y] >= X:
        taiyaki_min = min(taiyaki_min, i)
 
 
ans = max(taiyaki_min, takoyaki_min)
 
if ans == INF:
    print(-1)
else:
    print(ans-1)