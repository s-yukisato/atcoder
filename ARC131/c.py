N = int(input())
A = list(map(int, input().split()))
 
from itertools import accumulate
from operator import xor
 
xorA = list(accumulate(A, xor))[-1]
 
for a in A:
    if xorA ^ a == 0:
        print("Win")
        exit()
else:
    if N % 2 == 0:
        print("Lose")
    else:
        print("Win")