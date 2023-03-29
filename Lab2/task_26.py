#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    def cross():
        move_right(1)
        fill_cell()
        move_down()
        fill_cell()
        move_right(1)
        fill_cell()
        move_left(2)
        fill_cell()
        move_right(1)
        move_down(1)
        fill_cell()
        move_up(2)
        move_left(1)

    for i in range(5):
        for j in range(10):
            cross()
            if j != 9:
                move_right(4)
        if i != 4:
            move_down(4)
        move_left(4*9)

if __name__ == '__main__':
    run_tasks()
