from collections import defaultdict, deque


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members


N = int(input())

route_list = [[] for _ in range(N+1)]
times = [0]*(N+1)

for i in range(N):
    T, K, *A = map(int, input().split())
    times[i+1] = T
    for a in A:
        route_list[i+1].append(a)

que = deque(route_list[N])

visited = [False] * (N+1)


while que:
    now = que.pop()
    if visited[now]:
        continue
    visited[now] = True
    for n in route_list[now]:
        que.append(n)

ans = times[N]
for i in range(N):
    if visited[i+1]:
        ans += times[i+1]

print(ans)
