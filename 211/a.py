import math

a, b = map(int, input().split())


if int((a - b)/3 + b) == math.ceil((a - b)/3 + b):
    print(int((a - b)/3 + b))
else:
    print((a - b)/3 + b)
