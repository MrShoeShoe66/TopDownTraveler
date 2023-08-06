import curses
import re


def PrintAsColorInternal(win, y, x, s):
    def specialcharcheck(letter):
        if letter == 'z':
            return "#"
        return letter
    colors = {'z': curses.COLOR_RED, 'W': curses.COLOR_GREEN, 'P': curses.COLOR_BLUE}
    win.move(y, x)
    pattern = r'({0:s})'.format(
        '|'.join(r'\b{0:s}\b'.format(word) for word in colors.keys()))
    s = re.split(pattern, s)
    for s in s:
        win.addstr(specialcharcheck(s), curses.color_pair(colors.get(s, 0)))


def PrintAsColor(stdscr, string):
    curses.init_pair(curses.COLOR_RED,
                     curses.COLOR_RED,
                     curses.COLOR_BLACK)
    curses.init_pair(curses.COLOR_GREEN,
                     curses.COLOR_GREEN,
                     curses.COLOR_BLACK)
    curses.init_pair(curses.COLOR_BLUE,
                     curses.COLOR_BLUE,
                     curses.COLOR_BLACK)

    PrintAsColorInternal(stdscr,
                     4,
                     0,
                     string)
    stdscr.refresh()
    stdscr.getch()

# def main(stdscr):
#     PrintAsColor(stdscr, "z W P")

# curses.wrapper(main)
