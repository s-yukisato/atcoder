n, x = map(int, input().split())

a = input().split()

ans = ""

for i in a:
    if i == str(x):
        continue
    ans += i + " "

print(ans)