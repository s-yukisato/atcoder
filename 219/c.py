X = input()
N = int(input())
 
S = [input() for _ in range(N)]
 
 
B = {x: chr(idx+97) for idx, x in enumerate(X)}
C = {chr(idx+97): x for idx, x in enumerate(X)}
 
newS = []
 
for name in S:
    newS.append("".join([B[x] for x in name]))
 
newS.sort()
for name in newS:
    ans = ""
    for s in name:
        ans += C[s]
    print(ans)