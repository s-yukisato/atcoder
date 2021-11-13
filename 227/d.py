from bisect import bisect_left

N, K = map(int, input().split())

A = list(map(int, input().split()))

A.sort(reverse=True)

cnt = 0

while len(A) >= K:
    cnt += A[K-1]
    A.sort(reverse=True)