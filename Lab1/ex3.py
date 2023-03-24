import turtle
N=360
ang=180-((N-2)*180)/N
a=1
for i in range(N):
    turtle.forward(a)
    turtle.left(ang)
turtle.mainloop()