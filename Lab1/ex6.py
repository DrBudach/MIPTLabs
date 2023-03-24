import turtle
import math

N = 3
times = 10

alph = ((N - 2) * 180) / N / 2
ang = 180 - 2 * alph
step = 20
dr = 5
dang = 0
for i in range(times * N):
    turtle.forward(step)
    turtle.right(dang)
    dang = 180 * math.asin(dr / step * math.sin(math.pi * (180 - alph) / 180)) / math.pi
    ang = 180 - 2 * alph - dang
    turtle.right(ang)
    step = (step ** 2 + dr ** 2 - 2 * step * dr * math.cos(math.pi * (180 - alph) / 180)) ** 0.5
turtle.mainloop()
