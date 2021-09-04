from collections import deque

Q = int(input())
A = deque()
sA = []

for _ in range(Q):
    L = list(map(int, input().split()))
    if L[0] == 1:
        A.append(L[1])
    elif L[0] == 2:
        if not sA:
            print(A.pop())
        else:
            print(sA.pop())
    else:
        sA.append(A)
        sA.sort(reverse=True)


