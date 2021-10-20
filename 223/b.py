S = list(input())

store = []

for i in range(len(S)):

    S = S[1:] + S[0:1]
    store.append("".join(S))

store.sort()

print(store[0])
print(store[-1])