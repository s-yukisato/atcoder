H, W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]

flg = True
for i in range(H-1):
    for j in range(W-1):
        if A[i][j] + A[i+1][j+1] > A[i][j+1] + A[i+1][j]:
            flg = False

print("Yes" if flg else "No")