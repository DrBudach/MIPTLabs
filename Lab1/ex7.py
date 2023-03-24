import turtle

times = 10
a = 50
step = 5

for i in range(times * 4):
    turtle.forward(a)
    turtle.right(90)
    a = a + step
turtle.mainloop()
