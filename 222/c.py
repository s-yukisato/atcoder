N, M = map(int, input().split())

d = dict()

A = [list(input()) for _ in range(2*N)]

for i in range(2*N):
    d[i] = 0

winners = []
losers = []
drawers = []
rank = [i for i in range(2*N)]

for j in range(M):
    for i in range(0, N+1, 2):
        if A[rank[i]][j] == "G":
            if A[rank[i+1]][j]== "P":
                winners.append(rank[i+1])
                d[rank[i+1]] += 1
                losers.append(rank[i])
            elif A[rank[i+1]][j]== "C":
                winners.append(rank[i])
                d[rank[i]] += 1
                losers.append(rank[i+1])
        if A[rank[i]][j]== "P":
            if A[rank[i+1]][j]== "C":
                winners.append(rank[i+1])
                d[rank[i+1]] += 1
                losers.append(rank[i])
            elif A[rank[i+1]][j]== "G":
                winners.append(rank[i])
                d[rank[i]] += 1
                losers.append(rank[i+1])
        if A[rank[i]][j] == "C":
            if A[rank[i+1]][j]== "G":
                winners.append(rank[i+1])
                d[rank[i+1]] += 1
                losers.append(rank[i])
            elif A[rank[i+1]][j]== "P":
                winners.append(rank[i])
                d[rank[i]] += 1
                losers.append(rank[i+1])
        
        if A[rank[i]][j] == A[rank[i+1]][j]:
            drawers.append(rank[i])
            drawers.append(rank[i+1])
    winners.sort()
    losers.sort()
    drawers.sort()
    rank = winners + drawers + losers
    winners = []
    losers = []
    drawers = []
    print(rank)

ans = sorted(d.items(), key=lambda x: (x[1], -x[0]), reverse=True)

for a in ans:
    print(a[0]+1)

# 勝者リスト

# 敗者リスト

# sortして並び替え

# 買った回数を記録しておく