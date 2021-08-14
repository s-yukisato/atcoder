import sys
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, product, combinations_with_replacement
import operator
from math import sqrt, gcd, factorial

def input(): return sys.stdin.readline().rstrip()
def devceil(n, k): return 1+(n-1)//k
def yn(judge, yes="Yes", no="No"): print(yes if judge else no)

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.group_num = n
    
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)


def main():
    # n, m = map(int, input().split())
    # ab = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
    # ans = 0
    for bit in product([0, 1], repeat=4):
        print(bit)

if __name__ == "__main__":
    main()