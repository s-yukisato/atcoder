n, x = map(int, input().split())
li = list(map(int, input().split()))

con = len(li[1::2])
sum = 0
for i in li:
    sum += i


print("Yes" if sum - con<= x else "No")
