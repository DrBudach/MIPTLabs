import turtle
import math

R0 = 10
N0 = 360
M = 10
step = 5


def draw(R, N, x, y):
    a = 2 * R * math.sin(math.pi / N)
    turtle.penup()
    turtle.goto(x, y)
    turtle.forward(R)
    turtle.right(90)
    turtle.pendown()
    for i in range(N):
        turtle.forward(a)
        turtle.right(180 - ((N - 2) * 180) / N)


for i in range(M):
    draw(R0 + step * i, N0, R0 + step * i, 0)
    draw(R0 + step * i, N0, -R0 - step * i, 0)
