
def solve():
    n = int(input())
    segments = [tuple(map(int, input().split())) for _ in range(n)]
    segments.sort()

    used =set()


T = int(input())

for _ in range(T):
    solve()
