N, M = map(int, input().split())


xy = [list(map(int, input().split())) for _ in range(N)]

col = xy[0][0] % 7

if col + M - 1 > 7:
    print("No")
    exit()

s = xy[0][0]

if N == 1 and M == 1:
    print("Yes")
    exit()

for i in range(1, M):
    if xy[0][i] != xy[0][i-1] + 1:
        print("No")
        exit()

for i in range(M):
    for j in range(1, N):
        if xy[j][i] != xy[j-1][i] + 7:
            print("No")
            exit()

print("Yes")