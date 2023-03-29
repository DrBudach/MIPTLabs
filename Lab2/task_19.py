#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
    while wall_is_above() and not wall_is_on_the_right():
        move_right(1)
    else:
        while wall_is_above() and not wall_is_on_the_left():
            move_left(1)
        else:
            while wall_is_above() and not wall_is_on_the_right():
                move_right(1)

    while not wall_is_above():
        move_up(1)
        while not wall_is_on_the_left():
            move_left(1)



if __name__ == '__main__':
    run_tasks()
