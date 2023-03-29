#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)

def task_4_11():
    move_right(1)
    for i in range(14):
        for j in range(i):
            fill_cell()
            move_right(1)
        if i != 0 :
            move_left(i)
        move_down(1)


if __name__ == '__main__':
    run_tasks()
