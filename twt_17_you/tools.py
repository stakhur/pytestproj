import os
import ffmpeg
from pytubefix import YouTube, Stream

def what_to_look(s: Stream):
    if s.type == "video":
        return s.resolution
    elif s.type == "audio":
        return s.abr
    else:
        return s.type

def print_streams(streams, filter=None):
    if filter is None:
        for s in streams:
            print(s)

def get_streams(streams, filter=None):
    strs = streams

    if filter is not None:
        if filter == "video":
            strs = {k:v for k,v in streams.items() if "0p" in k}
        elif filter == "audio":
            strs = {k:v for k,v in streams.items() if "kbps" in k}
    
    return strs


def get_title(url):
    title = ""

    try:
        yt = YouTube(url)
        title = yt.title
    except Exception as e:
        print(e)

    return title


def get_all_streams(url):
    available_streams = {}
    
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=False).asc()
        for s in streams:
            key = what_to_look(s)

            if key in available_streams:
                available_streams[key].append(s)
            else:
                available_streams[key] = [s]
    except Exception as e:
        print(e)

    return available_streams


def get_stream_names(streams, type=""):
    filtred_streams = list(get_streams(streams, type).keys())
    filtred_streams.sort(key = lambda x: int(x[:-1]) if x[:-1].isdigit() else int(x[:-4]), reverse=True)
    return filtred_streams


def save_streams_to_file(save_path, video_stream, audio_stream, title=""):
    try:
        print(f"Downloading: {title} - {video_stream.resolution}/{audio_stream.abr} ")

        video_file = video_stream.download(output_path=save_path)
        audio_file = audio_stream.download(output_path=save_path)

        video_stream = ffmpeg.input(video_file)
        audio_stream = ffmpeg.input(audio_file)
        output_filename = f"{save_path}/{title}_merged.mp4"
        ffmpeg.output(audio_stream, video_stream, output_filename).run()

        os.remove(video_file)
        os.remove(audio_file)

        os.rename(output_filename, video_file)

        print(f"Video downloaded successfully to {output_filename}!")
    except Exception as e:
        print(e)


def download_video(url, save_path):    
    try:
        streams = get_all_streams(url)
        video_stream = streams["1080p"][0]
        audio_stream = streams["70kbps"][0]
        title = get_title(url)

        save_streams_to_file(save_path, video_stream, audio_stream, title)
    except Exception as e:
        print(e)
