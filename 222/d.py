N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

MOD = 998244353 

cnt = 1
minV = A[-1]

for i in range(N-1, -1, -1):
    cnt *= B[i] - minV + 1

print(cnt%MOD)