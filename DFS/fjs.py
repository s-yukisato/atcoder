s, t = input().split()

s_list = [ord(i) - 96 for i in s]
t_list = [ord(i) - 96 for i in t]

def f(li):
    old_list = li
    while len(old_list) != 1:
        new_list = []
        for i in range(len(old_list) - 1):
            new_list.append((old_list[i] + old_list[i + 1]) % 101)
        else:
            old_list = new_list[:]
    return old_list[0]
    
print(max(f(s_list + t_list), f(t_list + s_list)))