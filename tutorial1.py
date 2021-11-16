import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(10, 10, "hello world", curses.A_UNDERLINE)
    stdscr.addstr(15, 25, "tim is great!")
    stdscr.refresh()
    stdscr.getch()


wrapper(main)