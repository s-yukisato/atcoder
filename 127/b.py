r, D, x = map(int, input().split())

# x[i+1] = r*x[i] -D

for i in range(10):
    ans = r * x -D
    print(ans)
    x = ans