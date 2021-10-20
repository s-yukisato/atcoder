from sys import stdin
input = stdin.readline
n = int(input())
x,y = map(int,input().split())
l = [list(map(int,input().split())) for _ in range(n)]
dp = [[500 for _ in range(x+1)] for _ in range(y+1)]
 
dp[0][0]=0
for a,b in l:
    for i in range(x,-1,-1):
        for j in range(y,-1,-1):
            if dp[j][i]!=500:
                nj = min(y,j+b)
                ni = min(x,i+a)
                dp[nj][ni] = min(dp[nj][ni],dp[j][i]+1)
    print(*dp,sep="\n")
    # print(ans,a,b)
print(dp[-1][-1] if dp[-1][-1]!=500 else -1)