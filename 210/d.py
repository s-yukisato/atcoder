H, W, c = map(int, input().split()) 
A = [list(map(int, input().split())) for _ in range(H)]

ans = float("inf")
for _ in range(2):
    dp = [[float("inf") for _ in range(W)] for _ in range(H)]
    dp[1][0] = A[0][0]
    dp[0][1] = A[0][0]
    for h in range(2, H):
        dp[h][0]= min(dp[h-1][0], A[h-1][0] -c*(h-1+0))
    print(dp)

print(A)