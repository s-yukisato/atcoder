import numpy as np

h, w, k = map(int, input().split())

def f(strs):
    List = []
    for i in strs:
        if i == "#":
            List.append(0)
        elif i == "N":
            List.append(-1)
        else:
            List.append(int(i))
    return List

s = np.array([f(input()) for _ in range(h)])

n_idx = np.where(s == -1)
ni, nj = n_idx[0][0], n_idx[1][0]

idxs = np.nonzero(s)

ans = []
min_dis = 10000
for i, j in np.transpose(idxs):
    if s[i][j] == -1:
        continue
    distance = abs(ni - i) + abs(nj - j)
    if distance > min_dis:
        continue
    if distance < min_dis:
        ans = []
        min_dis = distance
    ans.append(s[i][j])

print(len(ans))
for i in sorted(ans):
    print(i)