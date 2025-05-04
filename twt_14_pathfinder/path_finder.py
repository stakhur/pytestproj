import curses
import queue
import time

from curses import wrapper, window

from maze import maze

START_CHAR = "O"
ROUTE_CHAR = "O"
FINISH_CHAR = "X"
WALL_CHAR = "#"


def print_maze(maze, stdscr: window, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            stdscr.addch(i, j*2, value, BLUE)

    for (row, col) in path:
        stdscr.addch(row, col*2, ROUTE_CHAR, RED)

    stdscr.refresh()


def get_start_pos(maze):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == START_CHAR:
                return (i, j)
    return (-1, -1)


def check_next_pos(maze, pos):
    if pos == (-1, -1):
        return None
    
    row, col = pos
    return maze[row][col] == FINISH_CHAR


def get_available_movements(maze, pos):
    row, col = pos
    movements = []

    if (row > 0) and (maze[row-1][col] != WALL_CHAR):
        movements.append((row-1, col))
    if (row < len(maze) - 1) and (maze[row+1][col] != WALL_CHAR):
        movements.append((row+1, col))
    if (col > 0) and (maze[row][col-1] != WALL_CHAR):
        movements.append((row, col-1))
    if (col < len(maze[0]) - 1) and (maze[row][col+1] != WALL_CHAR):
        movements.append((row, col+1))

    return movements


def main(stdscr: window):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    available_positions = queue.Queue()
    start_pos = get_start_pos(maze)
    if start_pos == (-1, -1):
        stdscr.addstr(0, 0, "Invalid maze.")
        stdscr.getch()
        return

    available_positions.put(start_pos)
    path = [start_pos]

    while True:
        print_maze(maze, stdscr, path)

        next_pos = available_positions.get()
        path.append(next_pos)

        if (check_next_pos(maze, next_pos)):
            print_maze(maze, stdscr, path)
            break

        movements = get_available_movements(maze, next_pos)
        for movement in movements:
            if movement not in path:
                available_positions.put(movement)

        time.sleep(0.05)
    
    stdscr.getch()


wrapper(main)