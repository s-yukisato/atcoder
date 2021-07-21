n, q = map(int, input().split())
S = input()
print(S.count("AC"))


for i in range(q):
    l, r = map(int, input().split())
    s = S[l-1:r]
    print(s.count("AC"))