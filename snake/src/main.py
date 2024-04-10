import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint


def create_food(snake, box):
    food = None
    while food is None:
        food = [
            randint(box[0][0] + 1, box[1][0] - 1),
            randint(box[0][1] + 1, box[1][1] - 1),
        ]
        if food in snake:
            food = None
    return food


def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1)
    w.timeout(100)

    box = [[3, 3], [sh - 3, sw - 3]]
    w.border()

    snake = [[sh // 2, sw // 2 + 1], [sh // 2, sw // 2], [sh // 2, sw // 2 - 1]]
    direction = KEY_RIGHT

    food = create_food(snake, box)
    w.addch(food[0], food[1], "*")

    score = 0

    while True:
        w.border()
        w.addstr(0, 2, "Score : " + str(score) + " ")
        w.addstr(0, 27, " SNAKE ")
        w.timeout(150 - (len(snake) // 5 + len(snake) // 10) % 120)

        prev_key = direction
        event = w.getch()
        direction = event if event != -1 else direction

        if direction == ord(" "):
            direction = -1

        if direction not in [KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN, ord(" ")]:
            direction = prev_key

        new_head = [snake[0][0], snake[0][1]]

        if direction == KEY_RIGHT:
            new_head[1] += 1
        elif direction == KEY_LEFT:
            new_head[1] -= 1
        elif direction == KEY_DOWN:
            new_head[0] += 1
        elif direction == KEY_UP:
            new_head[0] -= 1
        elif direction == -1:
            pass

        snake.insert(0, new_head)

        if (
            snake[0] in snake[1:]
            or snake[0][0] in [box[0][0], box[1][0]]
            or snake[0][1] in [box[0][1], box[1][1]]
        ):
            msg = "Game Over!"
            w.nodelay(0)
            w.addstr(sh // 2, sw // 2 - len(msg) // 2, msg)
            w.refresh()
            w.getch()
            break

        if snake[0] == food:
            score += 1
            food = create_food(snake, box)
            w.addch(food[0], food[1], "*")
        else:
            tail = snake.pop()
            w.addch(tail[0], tail[1], " ")

        w.addch(snake[0][0], snake[0][1], "#")


curses.wrapper(main)
