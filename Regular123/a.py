a = list(map(int, input().split()))

print(a[1]-a[0])
print(a[2]-a[1])
if a[1]-a[0] == a[2] - a[1]:
    print(0)
while a[1]-a[0] != a[2] - a[1]:
    if a[1]-a[0] > a[2] - a[1]:
        
