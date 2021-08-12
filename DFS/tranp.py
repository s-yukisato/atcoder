from collections import Counter

s = input()
c = Counter(s)
ans = c.most_common()[0][1]
if c["*"]:
    if ans == c["*"]:
        del c["*"]
        ans += c.most_common()[0][1]
    else:
        ans += c["*"]
        del c["*"]
    
if ans == 4:
    print("FourCard")
elif ans == 3:
    print("ThreeCard")
elif ans == 2:
    if len(c) == 2:
        print("TwoPair")
    elif len(c) == 3:
        print("OnePair")
else:
    print("NoPair")