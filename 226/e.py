from collections import defaultdict


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

MOD = 998244353
N, M = map(int, input().split())
if M == 1:
    print(0)
    exit()

G = [[] for _ in range(N)]

uf = UnionFind(N)

for _ in range(M):
    u, v = map(int, input().split())
    G[u-1].append(v-1)
    uf.union(u-1, v-1)

flg = True
for g in G:
    if len(g) % 2 == 1:
        flg = not flg

if not flg:
    print(0)
    exit()

gc = uf.group_count()

print(2**gc % MOD)
