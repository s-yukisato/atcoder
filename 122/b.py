s = input()

len = 0
ans = 0
for char in s:
    if char in "ATCG":
        len += 1
        ans = max(ans, len)
    else:
        len = 0

print(ans)