#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_6():
    if wall_is_beneath() and not wall_is_above():
        fill
    pass


if __name__ == '__main__':
    run_tasks()
