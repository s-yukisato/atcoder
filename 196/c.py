n = int(input())

num = 0
cnt =1
while num <= n:
    num = str(cnt) + str(cnt)
    cnt+=1
    num = int(num)

print(cnt-2)