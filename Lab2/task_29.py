#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    t = 0

    while t != 3:
        if cell_is_filled():
            t += 1
        else:
            t = 0
        if t != 3 and not wall_is_on_the_right():
            move_right(1)
        else:
            break


if __name__ == '__main__':
    run_tasks()
