import datetime
import os
import shutil
import time

import schedule


# source_dir = input("Input path to directory to set backup dir: ")
source_dir = "/home/anon/Pictures/Screenshots"
backup_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "backup")

try:
    os.mkdir(backup_dir)
except FileExistsError:
    pass

def backup_directory(source, dest):
    today = datetime.date.today()
    # timestamp_now = int(datetime.datetime.timestamp(datetime.datetime.now()))
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")

schedule.every().day.at("6:55").do(lambda: backup_directory(source_dir, backup_dir))
# schedule.every().minute.at(":30").do(lambda: backup_directory(source_dir, backup_dir))

while True:
    schedule.run_pending()
    time.sleep(60)