import turtle
import math

N=8
M=10
a=50
b=10
ang=180-((N-2)*180)/N
step=b/2/math.sin(math.pi/N)
for i in range(M):
    for j in range(N):
        turtle.forward(a)
        turtle.left(ang)
    a=a+b
    turtle.penup()
    turtle.right(90+ang/2)
    turtle.forward(step)
    turtle.left(90+ang/2)
    turtle.pendown()
turtle.mainloop()