N = sorted(list(input()), reverse=True)

ans = 0

if len(N) == 1:
    print(N)
    exit()

s = ""
t = ""
for i in range(len(N)):
    if i == 0:
        s += N[i]
    elif i == 1:
        t += N[i]
    elif int(s) > int(t):
        t += N[i]
    else:
        s += N[i]

print(int(s) * int(t))