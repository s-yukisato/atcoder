ATK, DEF, AGI = map(int, input().split())
N = int(input())

isEvo = False
for _ in range(N):
    s, *nums = [_ for _ in input().split()]
    [MINATK, MAXATK, MINDEF, MAXDEF, MINAGI, MAXAGI] = map(int, nums)
    
    if MINATK <= ATK <= MAXATK:
        if MINDEF <= DEF <= MAXDEF:
            if MINAGI <= AGI <= MAXAGI:
                print(s)
                isEvo = True
else:
    if not isEvo:
        print("no evolution")
