H,W,N=map(int,input().split())
X,Y=[],[]
for i in range(N):
  x,y=map(int,input().split())
  X.append(x)
  Y.append(y)

print(sorted(list(set(X))))
Xdict = {x:i+1 for i,x in enumerate(sorted(list(set(X))))}
Ydict = {y:i+1 for i,y in enumerate(sorted(list(set(Y))))}

print(Xdict)
print(Ydict)

for i in range(N):
  print(Xdict[X[i]], Ydict[Y[i]])