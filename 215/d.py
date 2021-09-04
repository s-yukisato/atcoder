
n, m = map(int, input().split())
a = sorted(set(list(map(int, input().split()))))

def make_divisors(n):
    print('yar')
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

ans = []
for t in reversed(a):
    if t in ans:
        continue
    tmp = make_divisors(t)
    ans = sum(ans, tmp)
    print(ans)
s = set(sum(ans, []))
s.remove(1)
print(s)

# res = []
# if 1 in a:
#     res.append(1)
# for i in range(2, m+1):
#     if i in delta:
#         continue
#     for v in delta:
#         if i % v == 0:
#             break
#     else:
#         res.append(i)

# print(*res, sep="\n")
