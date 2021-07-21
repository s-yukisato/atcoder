p = int(input())
li = [1]
sum = 1
cnt = 0
for i in range(2, 11):
    sum = sum * i
    li.append(sum)
    if sum > p:
        break
while p != 0:
    for i in reversed(li):
        if p >= i:
            p = p - i
            cnt += 1
            break
print(cnt)
