S = input()
T = input()
 
 
wrongS = ""
wrongT = ""
 
flg = False
cnt = 0
 
for s, t in zip(S, T):
    if flg:
        if wrongS == t and wrongT == s:
            flg = False
            continue
        else:
            break
    if s != t:
        wrongS = s
        wrongT = t
        cnt += 1
        flg = True
else:
    if cnt <= 1 and not flg:
        print("Yes")
        exit()
 
 
print('No')