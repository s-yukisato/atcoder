li = list(map(int, input().split()))

count = 0

blue = li[0]
red = 0

if li[1] >= li[2]:
    print(-1)
else:
    while blue > red * li[3]:
        blue += li[1]
        red += li[2]
        count += 1
    print(count)
