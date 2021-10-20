from bisect import bisect_left

N = int(input())

ab = []
length = [0]
times = [0]
base = 1

for i in range(N):
    a, b = map(int, input().split())
    ab.append((a, b))
    base *= b
    times.append(times[i] + (a / b))
    length.append(length[i] + a)

length.append(10**18)

sm = 0
for a, b in ab:
    sm += a * (base/b)


middle_time = (sm/base)/2
idx = bisect_left(times, middle_time)

if length[idx] == middle_time:
    print(middle_time)
    exit()

ans = length[idx-1]
rest = middle_time - times[idx-1]


print(ans + (ab[idx-1][1] * rest))

