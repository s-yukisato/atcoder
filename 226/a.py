S = list(input())

idx = S.index(".")

if int(S[idx+1]) >= 5:
    print(int("".join(S[:idx]))+1)
else:
    print("".join(S[:idx]))


