import turtle
import math

R0 = 50
N0 = 100
M = 10


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
    draw(R0, N0, R0 * math.cos(2 * math.pi / M * i), R0 * math.sin(2 * math.pi / M * i))

turtle.mainloop()
