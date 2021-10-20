def f(p1, p2, p3):
  return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def intersect(p1, p2, p3, p4):
  t1 = f(p1, p2, p3)
  t2 = f(p1, p2, p4)
  t3 = f(p3, p4, p1)
  t4 = f(p3, p4, p2)
  return t1 * t2 < 0.0 and t3 * t4 < 0.0


N, M = map(int, input().split())


points = []
for _ in range(M):
    a, b = map(int, input().split())
    points.append([(a, 0), (b, 1)])

ans = 0
for i in range(M):
    cnt = 0
    p1, p2 = points[i]
    for j in range(M):
        p3, p4 = points[j]
        if p1 == p3 or p1 == p4 or p2 == p3 or p2 == p4:
            continue
        if not intersect(p1, p2, p3, p4):
            cnt += 1
    if cnt > ans:
        ans = cnt
 
print(ans)