N, M = map(int, input().split())

L = []

for i in range(N):
    L.append(list(map(int, input().split())))

L.sort()

sum = 0
cnt = 0

for j in range(len(L)):
    for i in range(L[j][1]):
        sum += L[j][0]
        cnt += 1
        if cnt == M:
            break
    else:
        continue
    break

print(sum)