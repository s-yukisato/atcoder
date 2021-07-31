t = ["H", "2B", "3B", "HR"]
for i in range(4):
    s = input()
    try:
        index = t.index(s)
        t.pop(index)
    except ValueError:
        print("No")
        exit()


print("Yes")