N, t = input().split()
n = int(N)
s = list(input())

abc = list("abcdefghijklmnopqrstuvwxyz")
code = list(t)

# 暗号化
for i in range(n):
    num = list(map(lambda x: ord(x) - 97, code))
    cnt = 0
    tmp = ["_"] * 26
    for j in abc:
        tmp[num[cnt]] = j
        cnt += 1
    code = tmp

print(tmp)

ans = ""

for i in s:
    if i == " ":
        ans += " "
        continue
    index = tmp.index(i)
    ans += abc[index]
print(ans)
