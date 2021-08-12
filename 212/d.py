import heapq

all_added = 0
hp = []

q = int(input())

for _ in range(q):
    query = list(map(int, input().split()))
    if len(query) == 2:
        p, x = query
        if p == 1:
            heapq.heappush(hp, x-all_added)
        else:
            all_added += x
    else:
        min_value = heapq.heappop(hp)
        print(min_value + all_added)