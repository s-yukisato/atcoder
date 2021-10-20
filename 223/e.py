X, Y, *rect = map(int, input().split())

rect.sort(reverse=True)

if X * Y < sum(rect):
    print("No")
    exit()

if (X/3) * Y < rect[0]:
    print("No")
    exit()

if (Y/3) * X < rect[0]:
    print("No")
    exit()


print("Yes")