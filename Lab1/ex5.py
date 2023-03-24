import turtle

N=5
a=50
turtle.shape("turtle")
for i in range(N):
    turtle.forward(a)
    turtle.stamp()
    turtle.backward(a)
    turtle.left(360/N)
turtle.mainloop()
