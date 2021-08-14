from collections import defaultdict
def MI(): return map(int, input().split())


d = defaultdict(int)
n, k = MI()
for i in range(n):
    a, b =MI()
    d[a] += b

dd =  sorted(d.items())

for kl, tl in dd:
    if k >= kl:
        k += tl
    else:
        break

print(k)