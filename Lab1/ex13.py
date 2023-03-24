import turtle
import math


def star(A, N, x0, y0):
    ang = 360 / 2 / N
    turtle.penup()
    turtle.goto(x0, y0)
    turtle.forward(A / 2 / math.cos(ang / 2 / 180 * math.pi))
    turtle.left(180 - ang / 2)
    turtle.pendown()
    for i in range(N):
        turtle.forward(A)
        turtle.left(180 - ang)


star(100, 8, -100, 0)
#star(100, 11, 100, 0)

turtle.mainloop()
