N, Q = map(int, input().split())

G = [0] * (N+1)


for i in range(Q):
    op, *val = map(int, input().split())
    if op == 1:
        x, y = val[0], val[1]
        G[x] = y
    elif op == 2:
        x, y = val[0], val[1]
        G[x] = 0
    else:
        x = val[0]
        print(G[x])


