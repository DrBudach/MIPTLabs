#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    x=1
    y=1
    max=1
    while not wall_is_on_the_right():
        move_right(1)
        max+=1
    while not wall_is_on_the_left():
        move_left(1)

    while not wall_is_beneath():
        if not wall_is_on_the_right():
            while not wall_is_on_the_right():
                if x != y and x+y != max+1:
                    fill_cell()
                move_right()
                x+=1
            if x != y and x + y != max + 1:
                fill_cell()
        else:
            while not wall_is_on_the_left():
                if x != y and x+y != max+1:
                    fill_cell()
                move_left()
                x-=1
            if x != y and x + y != max + 1:
                fill_cell()
        move_down()
        y+=1
    else:
        if not wall_is_on_the_right():
            while not wall_is_on_the_right():
                if x != y and x+y != max+1:
                    fill_cell()
                move_right()
                x+=1
            if x != y and x + y != max + 1:
                fill_cell()
        else:
            while not wall_is_on_the_left():
                if x != y and x+y != max+1:
                    fill_cell()
                move_left()
                x-=1
            if x != y and x + y != max + 1:
                fill_cell()
    while not wall_is_on_the_left():
        move_left()


if __name__ == '__main__':
    run_tasks()
