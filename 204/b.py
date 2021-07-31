import collections


n = int(input())
a = list(map(int, input().split()))

c = collections.Counter(a)

print('Yes' if len(c) == n else 'No') 