a, b, c, d = map(int, input().split())
 
while(a > 0 and c > 0):
    c -= b
    a -= d

if c <= 0:
    print("Yes")
elif a <= 0:
    print("No")