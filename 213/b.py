n = int(input())
a = list(map(int, input().split()))
n, m, k = map(int, input().split())
List = [list(map(int, input().split())) for _ in range(n)]

total_time = 0
print(total_time)
s = sorted(a, reverse=True)

print(a.index(s[1]) + 1)