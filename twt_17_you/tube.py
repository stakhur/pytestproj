import os
import tkinter as tk

from tkinter import filedialog

from pytubefix import YouTube


def download_video(url, save_path):
    try:
        yt = YouTube(url)
        # stream = yt.streams.get_highest_resolution()
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        stream = streams.get_highest_resolution()
        print(f"Downloading: {yt.title} - {stream.resolution}")
        stream.download(output_path=save_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print(e)


def test():
    # url = "https://www.youtube.com/watch?v=p-vqh0KBtHM"
    url = "https://www.youtube.com/watch?v=aMgB018o71U"
    save_path = os.path.dirname(os.path.abspath(__file__))
    download_video(url, save_path)


def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder


def main():
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter a YouTube url: ")
    save_dir = open_file_dialog()
    if save_dir:
        download_video(video_url, save_dir)
    else:
        print("Invalid save location")


if __name__ == "__main__":
    main()