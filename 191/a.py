v, t, s, d = map(int, input().split())

print("Yes" if not v * t <= d <= v * s else "No")