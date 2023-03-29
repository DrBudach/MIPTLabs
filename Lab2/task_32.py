#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    mem = 0
    while not wall_is_on_the_right():
        while not wall_is_above():
            move_up(1)
            if cell_is_filled():
                mem+=1
            else:
                fill_cell()
        while not wall_is_beneath():
            move_down()
        if wall_is_beneath() and wall_is_above() and cell_is_filled():
            mem+=1
        elif wall_is_beneath() and wall_is_above():
            fill_cell()
        move_right(1)
    mov('ax',mem)

if __name__ == '__main__':
    run_tasks()
