N = int(input())

res = [0] * (N+1)
logs = []

for i in range(1, N+1):
    a, b = map(int, input().split())
    logs.append((a-1, "l"))
    logs.append((a+b-1,"r"))

logs.sort()

now = logs[0][0]
nums = 1

for day, w in logs[1:]:
    if w == "l":
        res[nums] += day - now
        nums += 1
        now = day
    elif w == "r":
        res[nums] += day - now
        nums -= 1
        now = day

print(*res[1:])