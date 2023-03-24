import turtle
import math

R0 = 10
N0 = 3
M = 10
step = 10


def draw(R, N):
    turtle.penup()
    turtle.goto(R, 0)
    turtle.pendown()
    turtle.left(180 - ((N - 2) * 180) / N / 2)
    for i in range(N):
        turtle.forward(2 * R * math.sin(math.pi / N))
        turtle.left(180 - ((N - 2) * 180) / N)
    turtle.right(180 - ((N - 2) * 180) / N / 2)


for i in range(M):
    draw(R0, N0)
    R0 += step
    N0 += 1

turtle.mainloop()
