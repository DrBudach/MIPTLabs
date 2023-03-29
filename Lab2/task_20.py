#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    for i in range(12):
        for j in range (27):
            if i % 2 == 0 :
                move_right(1)
            else:
                move_left(1)
            fill_cell()
        if i % 2 == 0 and i != 11  :
            move_right(1)
        elif i != 11 :
            move_left(1)
        move_down(1)



if __name__ == '__main__':
    run_tasks()
