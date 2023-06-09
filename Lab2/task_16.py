#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_22():
    while not wall_is_above():
        move_up(1)
    else:
        if not wall_is_on_the_right():
            while not wall_is_on_the_right():
                move_right(1)
        elif not wall_is_on_the_left():
            while not wall_is_on_the_left():
                move_left(1)


if __name__ == '__main__':
    run_tasks()
