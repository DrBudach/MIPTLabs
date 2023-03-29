#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    while not wall_is_beneath():
        move_down(1)

    while wall_is_beneath():
        move_right(1)

    move_down(1)
    move_left(1)

    while not wall_is_on_the_left():
        move_left(1)


if __name__ == '__main__':
    run_tasks()
