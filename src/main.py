import curses
from random import randint
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

from snake import Snake


GAME_OVER = 'Game Over!'
QUIT = 'EXIT GAME!'


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



def main(stdscr: "curses._CursesWindow") -> None:
    curses.curs_set(0)
    stdscr.nodelay(True)
    sh, sw = stdscr.getmaxyx()

    w = curses.newwin(sh, sw, 0, 0)
    box = [[1, 1], [sh - 1, sw - 1]]
    w.keypad(True)
    w.border()


    snake = Snake(height=sh, width=sw)
    food = create_food(snake=snake.body, box=box)
    w.addch(food[0], food[1], '*')

    while True:
        w.border()
        w.addstr(0, 2, f"Score: {str(snake.score)} ")
        w.timeout(150 - snake.speed)

        event = w.getch()

        if event == 'q':
            w.addch(sh // 2, sw // 2 - len(QUIT) // 2, QUIT)
        elif event in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]:
            snake.direction = event
        else:
            pass

        snake.update()

        if snake.game_over(box=box):
            w.clear()
            w.border()
            w.addstr(sh // 2, sw // 2 - len(GAME_OVER) // 2, GAME_OVER)
            w.addstr(sh // 2 + 1, sw // 2 - len('Final Score: ') // 2, f'Final Score: {snake.score}')
            w.nodelay(False)
            w.getch()
            break

        if snake.eat_food(food=food):
            snake.score += 1
            food = create_food(snake=snake.body, box=box)
            w.addch(food[0], food[1], '*')
        else:
            tail = snake.body.pop()
            w.addch(tail[0], tail[1], " ")
        
        w.addch(snake.body[0][0], snake.body[0][1], "#")



if __name__ == "__main__":
    curses.wrapper(main)
