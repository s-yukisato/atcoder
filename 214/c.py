
def II(): return int(input())
def LI(): return list(map(int, input().split()))

n = II()
S = LI()
T = LI()

ans = []
time = 0
for i in range(n):
    if i == 0:
        ans.append(T[0])
        time = T[0]
        continue
    time = min(time+S[i-1], T[i-1] + S[i-1], T[i])
    ans.append(time)
else:
    time += S[i]

for i in range(n):
    if time < ans[i]:
        ans[i] = time
    time += S[i]
    
for a in ans:
    print(a)