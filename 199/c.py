n = int(input())
s = list(input())
q = int(input())

judge = False
for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        a -= 1
        b -= 1
        if judge:
            a = (a + n) % (2*n)
            b = (b + n) % (2*n)
        tmp = s[a] 
        s[a] = s[b]
        s[b] = tmp
    else:
        judge = not judge
else:
    if judge:
        bfe = s[:n]
        aft = s[n:]
        s = aft + bfe
    
print("".join(s))
