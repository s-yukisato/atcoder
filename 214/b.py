import sys
input = sys.stdin.readline
def II(): return int(input())
def II_(): return input()
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI_(): return list(input())
def TL(n): return [list(map(int, input().split())) for _ in range(n)]
def TL_(n): return [list(input()) for _ in range(n)]

def yn(judge, yes="Yes", no="No"): print(yes if judge else no)
MOD = 10 ** 9 + 7
INF = float('inf')

s, t = MI()

cnt = 0
for i in range(101):
    for j in range(101):
        for k in range(101):
            if s < k or s < j or s <i:
                break
            if i + j +k <=s and i*j*k <= t:
                cnt += 1

print(cnt)