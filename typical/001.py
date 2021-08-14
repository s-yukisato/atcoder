N, L = map(int, input().split())
K = int(input())
a = list(map(int, input().split())) + [L]
 
def solve(x):
    cnt, pre = 0, 0
    for i in range(N+1):
        if a[i] - pre >= x:
            cnt += 1
            pre = a[i]
    return (cnt >= K + 1)
 
left, right = -1, L+1
while right - left > 1:
    mid = (left + right) // 2
    left, right = [mid, right] if solve(mid) else [left, mid]
 
print(left)