#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    t=0

    while t != 5:
        if cell_is_filled():
            t+=1
        if t != 5:
            move_right(1)


if __name__ == '__main__':
    run_tasks()
