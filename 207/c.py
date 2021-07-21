n = int(input())
t = [list(map(int, input().split(" "))) for _ in range(n)]


count = 0

while len(t):
    tmp = t.pop(0)
    for e in t:
        if tmp[2] == e[1]:
            if tmp[0] == 2 or tmp[0] == 4 or e[0] == 3 or e[0] == 4:
                pass
            else:
                count+=1
        elif tmp[2] > e[1]:
            count+=1

print(count)