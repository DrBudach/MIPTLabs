#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    move_right(1)
    while not wall_is_on_the_right():
        while not wall_is_above():
            move_up(1)
            fill_cell()
        while not wall_is_beneath():
            move_down()
        move_right(1)
    else:
        while not wall_is_above():
            move_up(1)
            fill_cell()
        while not wall_is_beneath():
            move_down()
    while wall_is_above() or wall_is_beneath():
        move_left(1)


if __name__ == '__main__':
    run_tasks()
