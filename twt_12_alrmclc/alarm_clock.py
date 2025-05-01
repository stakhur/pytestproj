# https://www.fesliyanstudios.com/royalty-free-sound-effects-download/alarm-203
# https://en.wikipedia.org/w/index.php?title=ANSI_escape_code

import os
import time

from playsound import playsound


CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


def get_alarm_file(filename):
    proj_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(proj_dir, filename)
    return file_path


def show_time_left(initial_seconds, time_left):
    minutes_left = time_left // 60
    seconds_left = time_left % 60

    print(f"{CLEAR_AND_RETURN}Alarm was set to {initial_seconds} seconds")
    print(f"Alarm will sound in {minutes_left:02d}:{seconds_left:02d}")


def alarm(seconds):
    time_elapsed = 0
    print(CLEAR)

    show_time_left(seconds, seconds)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        show_time_left(seconds, seconds - time_elapsed)

    playsound(get_alarm_file("alarm.mp3"))


def main():
    minutes = int(input("Hom many minutes to wait: "))
    seconds = int(input("Hom many seconds to wait: "))
    total_seconds = minutes * 60 + seconds
    alarm(total_seconds)


if __name__ == "__main__":
    main()