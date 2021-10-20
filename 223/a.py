N = int(input())

if N == 0:
    print("No")
    exit()

print("Yes" if N%100 == 0 else "No")
