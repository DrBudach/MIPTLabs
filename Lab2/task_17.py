#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():
    while not cell_is_filled():
        move_up(1)
    if not wall_is_on_the_right():
        move_right(1)
        if not cell_is_filled():
            move_left(2)
    else:
        move_left(1)

if __name__ == '__main__':
    run_tasks()
