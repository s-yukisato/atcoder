ss = [input(), input(), input()]
idx = [0, 0, 0]
x = 0
while True:
    if len(ss[x]) == idx[x]:
        print(chr(65+x))
        break
    nx = ord(ss[x][idx[x]])-97
    idx[x] += 1
    x = nx