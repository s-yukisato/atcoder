import collections

s = input()
n = len(s)
li = []
count = 0
for i in range(1, n+1):
    data = s[n-i:n:1]
    reminder = int(data) % 2019
    if reminder == 0:
        count += 1
    li.append(reminder)

c = collections.Counter(li)
count += list(c.values()).count(2)
print(count)
