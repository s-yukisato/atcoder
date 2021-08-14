n = int(input())
a = list(set(map(int, input().split())))

if len(a) == n:
    print("Yes")
else:
    print("No")