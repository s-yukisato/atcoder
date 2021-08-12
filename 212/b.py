s = input()

# weak = []
# for i in range(10):
#     weak.append(str(i)*4)
#     increase = ""
#     for j in range(4):
#         increase += str((i+j) % 10)
#     weak.append(increase)

# print(["Strong", "Weak"][s in weak])

print(["Strong", "Weak"][len(set(s))==1 or s in '0123456789012'])