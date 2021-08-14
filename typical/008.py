"""
a             :
at            :
atc          :
atco        :
atcod      :
atcode    :
atcoder  :
"""
def II(): return int(input())
def LI_(): return list(input())

MOD = 10 ** 9 + 7

n = II()
s = LI_()
sample = list("atcoder")

dp = [[0] * n for _ in range(7)]

for i in range(7):
    for j in range(i, n):
        if sample[i] == s[j]:
            if i == 0 and j == 0:
                dp[i][j] = 1
            elif i == 0:
                dp[i][j] += dp[i][j-1]+ 1
            else:
                dp[i][j] += dp[i-1][j-1] + dp[i][j-1]
        else:
            dp[i][j] += dp[i][j-1]

print(dp[6][n-1] % MOD)
