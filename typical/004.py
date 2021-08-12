import numpy as np

h, w = map(int, input().split())

a = []
row_sum = []
col_sum = []
for _ in range(h):
    s = list(map(int, input().split()))
    a.append(s)
    row_sum.append(sum(s)
    col_sum


# row_sum = np.sum(a, axis=1)
# col_sum = np.sum(a, axis=0)

for i in range(h):
    for j in range(w):
        selfValue = a[i][j]
        print(row_sum[i]  + col_sum[j] - selfValue, end=" ")
    else:
        print()