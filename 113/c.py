import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
 
l = [[] for _ in range(n+1)]
 
List = []
 
for _ in range(m):
    p, y = map(int, input().split())
    l[p].append(y)
    List.append((p, y))
 
for pref in l:
    if pref == []:
        continue
    pref.sort()
 
[print("{:06}{:06}".format(p, l[p].index(y)+1)) for p, y in List]