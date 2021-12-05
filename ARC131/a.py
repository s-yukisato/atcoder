A = int(input())
B = int(input())
 
if B % 2 == 1:
    B = int(str(B) + "0")
print(str(A) + "0" + str(B // 2))