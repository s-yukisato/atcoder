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


ans = 0
n, k = MI()
for i in range(1, n+1):
    for j in range(1, k+1):
        s = str(i) + "0" + str(j)
        ans += int(s)
    
print(ans)
