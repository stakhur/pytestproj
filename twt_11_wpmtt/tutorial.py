import curses
import os
import random
import time

from curses import wrapper, window, error


def start_screen(stdscr: window):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()


def display_text(stdscr: window, target, current, wpm=0):
    stdscr.addstr(0, 0, f"{target}")
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    for id, char in enumerate(current):
        color_pair_id = 4
        if id < len(target):
            correct = target[id]
            if char == correct:
                color_pair_id = 1
            else:
                color_pair_id = 2
        
        stdscr.addch(0, id, char, curses.color_pair(color_pair_id))


def load_text(stdscr: window, filename="test.txt"):
    text = ""

    proj_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(proj_dir, filename)

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            text = random.choice(lines).strip()
    except Exception as e:
        text = "This is my long text which I have to type!"

    return text


def wpm_test(stdscr: window):
    target_text = load_text(stdscr)
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / max(current_text.count(" "), 5))

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except error as e:
            continue

        if key in("KEY_BACKSPACE", '\b', "\x7f"):
            if current_text:
                current_text.pop()
        elif ord(key) == 27: # ESC
            stdscr.nodelay(False)
            return 1
        else:
            current_text.append(key)
    
    return 0


def main(stdscr: window):    
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    start_screen(stdscr)

    while True:
        if (wpm_test(stdscr) == 1):
            break

        stdscr.addstr(2, 0, "You completed the test! Press any key to continue...")
        key = stdscr.getkey()
        if ord(key) == 27:
            break


wrapper(main)