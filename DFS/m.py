import re
s = input()
        
abc = "abcdefghijklmnopqrstuvwxyz"

d = {}
for st in abc:
    d[st] = 0

double = 1
search = -1

nums = re.findall("\d+", s)

idxs = []

for i in nums:
    for j in range(search + 1, s.index(i)):
        if s[j] == ")":
            idx = idxs.pop()
            double //= int(idx)
        else:
            d[s[j]] = d[s[j]] + double
    else:
        search = s.index(i) - 1

    n_after = s.index(i) + len(i)
    if s[n_after] in abc:
        d[s[n_after]] = d[s[n_after]] + int(i) * double
    else:
        double *= int(i)
        idxs.append(i)
    search += len(i) + 1
    s = s.replace(i, "!" * len(i), 1)
else:
    for j in range(search + 1, len(s)):
        if s[j] == ")":
            idx = idxs.pop()
            double //= int(idx)
        else:
            d[s[j]] = d[s[j]] + double
    
for key, value in d.items():
    print(key, value)