H, W, K = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(H)]

used = [A[0][0]]

H -= 1
W -= 1

while H or W:
    used.append(A[H][W])
    if H == 0:
        W -= 1
        continue
    if W == 0:
        H -= 1
        continue
    
    if A[H][W-1] > A[H-1][W]:
        H -= 1
    else:
        W -= 1

used.sort(reverse=True)

print(sum(used[:K]))


