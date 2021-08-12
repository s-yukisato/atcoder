a, b, c = map(int, input().split())
n = int(input())

schedule = []
for _ in range(n):
    h, m = map(int, input().split())
    schedule.append((8 - h) * 60 + (60 - m))

ride_time = 0
for time in schedule[::-1]:
    if time >= b + c + 1:
        ride_time = time
        break
ans = ride_time + a
hh = 8 - (ans // 60)
mm = 60 - (ans % 60)
print("{:02}:{:02}".format(hh, mm))