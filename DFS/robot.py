
s_x, s_y = map(int, input().split())
d_f, d_r, d_b, d_l = map(int, input().split())
n = int(input())


class Robot:
    def __init__(self, x, y, d_f, d_r, d_b, d_l):
        self.x = x
        self.y = y
        self.front = 0
        self.d_f = d_f
        self.d_r = d_r
        self.d_b = d_b
        self.d_l = d_l

    def move(self, direction):
        if self.front == 0: # y方向
            if direction == "F":
                self.y += self.d_f
            elif direction == "R":
                self.x += self.d_r
            elif direction == "B":
                self.y -= self.d_b
            elif direction == "L":
                self.x -= self.d_l
        elif self.front == 1: # x方向
            if direction == "F":
                self.x += self.d_f
            elif direction == "R":
                self.y -= self.d_r
            elif direction == "B":
                self.x -= self.d_b
            elif direction == "L":
                self.y += self.d_l
        elif self.front == 2: # -y方向
            if direction == "F":
                self.y -= self.d_f
            elif direction == "R":
                self.x -= self.d_r
            elif direction == "B":
                self.y += self.d_b
            elif direction == "L":
                self.x += self.d_l
        elif self.front == 3: # -x方向
            if direction == "F":
                self.x -= self.d_f
            elif direction == "R":
                self.y += self.d_r
            elif direction == "B":
                self.x += self.d_b
            elif direction == "L":
                self.y -= self.d_l

    def rotate(self, direction):
        if direction == "R":
            self.front = (self.front + 1) % 4
        elif direction == "B":
            self.front = (self.front + 2) % 4
        elif direction == "L":
            self.front = (self.front + 3) % 4
        else:
            self.front = (self.front) % 4


r = Robot(s_x, s_y, d_f, d_r, d_b, d_l)

for _ in range(n):
    e, c = input().split()
    if e == "m":
        r.move(c)
    elif e == "t":
        r.rotate(c)
    print(r.x, r.y)
else:
    print(r.x, r.y)
