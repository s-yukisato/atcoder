n, m, K = map(int, input().split())

MOD = 998244353

edge = [[i] for i in range(n)]

for _ in range(m):
    u,v = map(int, input().split())
    u -=1
    v-=1
    edge[u].append(v)
    edge[v].append(u)

dp = [[0] * n for _ in range(K+1)]

dp[0][0]= 1

for k in range(1, K+1):
    all_sum = sum(dp[k-1])
    for i in range(n):
        dp[k][i] = all_sum
        for j in edge[i]:
            dp[k][i] -= dp[k-1][j]
        dp[k][i] %= MOD

print(dp[k][0])