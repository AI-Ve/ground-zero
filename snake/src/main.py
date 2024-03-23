import snake
import curses


def c_main(scr: "curses._CursesWindow") -> int:
    scr.clear()


def main() -> int:
    return curses.wrapper(c_main)


if __name__ == "__main__":
    exit(main())
