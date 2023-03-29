#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
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

    move_down(1)
    for i in range(5):
        cross()
        if i != 4:
            move_right(4)



if __name__ == '__main__':
    run_tasks()
