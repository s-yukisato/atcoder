import numpy as np

N = int(input())
S = np.array([list(input()) for _ in range(N)])
T = np.array([list(input()) for _ in range(N)])

s_list = []
B = S.flatten()
tmp = -1
for i, b in enumerate(B):
    if b == "#":
        tmp = 1 if tmp == -1 else tmp + 1
        s_list.append(tmp)
    elif tmp != -1:
        tmp = tmp + 1


for i in range(4):
    tmp = -1
    A = T.flatten()
    t_list = []
    for i, b in enumerate(A):
        if b == "#":
            tmp = 1 if tmp == -1 else tmp + 1
            t_list.append(tmp)
        elif tmp != -1:
            tmp = tmp + 1

    if all([s == t for s, t in zip(s_list, t_list)]):
        print("Yes")
        break
    T = np.rot90(T)
else:
    print("No")