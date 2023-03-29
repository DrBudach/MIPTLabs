#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    t=0

    move_right(1)
    while not wall_is_on_the_right():
        for i in range(t):
            if wall_is_on_the_right():
                break
            move_right(1)
        if not wall_is_on_the_right():
            fill_cell()
        t+=1




if __name__ == '__main__':
    run_tasks()
