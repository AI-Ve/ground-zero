import curses
from random import randint
from typing import List


def food(snake: List, sh: int, sw: int) -> List:
    position = None
    while position is None:
        position = [randint(1, sh - 1), randint(1, sw - 1)]
        if position in snake:
            position = None
    return position


def c_main(scr: "curses._CursesWindow") -> int:
    curses.curs_set(0)

    scr.clear()

    window_height, window_length = scr.getmaxyx()
    name = ""

    while True:
        new_food = food([[1, 1], [1, 2], [1, 3]], window_height, window_length)
        scr.addstr(new_food[0], new_food[1], "*")
        name = scr.get_wch()

        if name == "q":
            break

        scr.addstr(new_food[0], new_food[1], "")

    return 0


if __name__ == "__main__":
    curses.wrapper(c_main)
    SystemExit(0)
