N = int(input())

xy = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for i in range(N):
    u = xy[i]
    for j in range(i+1, N):
        v = xy[j]
        for k in range(j+1, N):
            w = xy[k]
            
            if (v[1]-u[1]) * (w[0]-u[0]) != (w[1]-u[1]) * (v[0]-u[0]):
                cnt += 1

print(cnt)