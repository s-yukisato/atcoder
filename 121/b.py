N, M, C = map(int, input().split())
B = list(map(int, input().split()))

ans = 0

for i in range(1, N+1):
    score = 0
    A = list(map(int, input().split()))
    for j in range(M):
        score += A[j] * B[j]
    if score > -C:
        ans += 1

print(ans)
