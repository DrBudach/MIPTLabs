import turtle
import math


def circ(R, N, x, y, clr):
    a = 2 * R * math.sin(math.pi / N)
    turtle.penup()
    turtle.goto(x, y)
    turtle.forward(R)
    turtle.right(90)
    turtle.pendown()
    turtle.fillcolor(clr)
    turtle.begin_fill()
    for i in range(N):
        turtle.forward(a)
        turtle.right(180 - ((N - 2) * 180) / N)
    turtle.end_fill()


def arc(R, N, x, y, clr):
    a = 2 * R * math.sin(math.pi / N)
    turtle.color(clr)
    turtle.penup()
    turtle.goto(x, y)
    turtle.forward(R)
    turtle.right(90)
    turtle.pendown()
    for i in range(N // 2):
        turtle.forward(a)
        turtle.right(180 - ((N - 2) * 180) / N)
    turtle.color("black")


circ(90, 100, 0, 0, "yellow")
circ(20, 100, 30, 30, "blue")
circ(20, 100, -30, 30, "blue")

turtle.penup()
turtle.width(3)
turtle.goto(0, -8)
turtle.pendown()
turtle.goto(0, 8)

turtle.right(90)
arc(50, 100, 0, 0, "red")

turtle.mainloop()
