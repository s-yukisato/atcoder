import bisect
import math


def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)

N = int(input())
A = list(map(int, input().split()))
B = []

cnt = 0
for i in range(len(A)): 
    if i == 0:
        B.append(A[i])
        continue
    index = bisect.bisect_left(B, A[i])
    B.insert(index, A[i])
    if index != 0:
        cnt += permutations_count(index+1, index)

print(cnt)

