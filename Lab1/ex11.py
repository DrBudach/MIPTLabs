import turtle
import math

R0 = 50
R1 = 10
N0 = 100
M = 10


def arc(R, N):
    a = 2 * R * math.sin(math.pi / N)
    for j in range(N // 2):
        turtle.forward(a)
        turtle.right(180 - ((N - 2) * 180) / N)


turtle.left(90)
for i in range(M):
    arc(R0, N0)
    arc(R1, N0)
turtle.mainloop()
