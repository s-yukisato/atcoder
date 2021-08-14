import sys
input = sys.stdin.readline
def II_(): return input()
def II(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(MI())
def LI_(): return list(II_())
n = int(input())
print(sum(list(map(lambda x: max(0, int(x)-10), input().split()))))


N = int(input())
A = [0]*(N+1)
B = [0]*(N+1)
C = [0]*(N+1)
 
for i in range(1,N+1):
    a, b, c = map(int, input().split())
    A[i] = max(B[i-1]+a, C[i-1] + a)
    B[i] = max(C[i-1]+b, A[i-1] + b)
    C[i] = max(B[i-1]+c, A[i-1] + c)
    print(A, B, C)
 
ans = max(A[N], B[N], C[N])
print(ans)

print(a)

