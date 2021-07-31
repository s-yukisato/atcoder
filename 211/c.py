s = input()
n = len(s)

dp = [[0] * 9]*(n+1)

mod = 10 ** 9 + 7
t = "chokudai"

for i in range(n+1):
    dp[i][0] = 1

for i in range(n):
    for j in range(8):
        if s[i] != t[j]:
            dp[i+1][j+1] = dp[i][j+1]
        else:
            dp[i+1][j+1] = dp[i][j+1] + dp[i][j] % mod

print(dp[n][8])
