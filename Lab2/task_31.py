#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    end = False
    flag = 0
    while not end:
        while wall_is_beneath():
            if not wall_is_on_the_right() and wall_is_beneath():
                while not wall_is_on_the_right() and wall_is_beneath():
                    move_right(1)
            if not wall_is_on_the_left() and wall_is_beneath():
                while not wall_is_on_the_left() and wall_is_beneath():
                    move_left(1)
            if wall_is_beneath() and wall_is_on_the_left():
                end = True
                break
        if not end:
            move_down(1)




if __name__ == '__main__':
    run_tasks()
