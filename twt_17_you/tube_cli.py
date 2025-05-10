import tools


def get_url():
    url = input("Enter video url to download: ")


def get_data(url):
    title = tools.get_title(url)
    streams = tools.get_all_streams(url)
    return title, streams


def get_stream(streams, type):
    l = len(streams)
    while True:
        print(f"Choose {type} stream (1-{l-1}):")
        for i, name in enumerate(streams):
            print(f"{i}: {name}")
        
        inp = input("> ")
        if not inp or not inp.isdigit() or int(inp) not in range(1,l):
            continue

        return streams[int(inp)] 


def get_streams(title, streams):
    print(title)

    video = tools.get_stream_names(streams, "video")
    video = get_stream(video ,"video")

    audio = tools.get_stream_names(streams, "audio")
    audio = get_stream(audio, "audio")

    return video, audio


def get_dir_to_download() -> str:
    dir = input("Enter directory to download: ")
    return dir


def download(dir, video_stream, audio_stream, title):
    tools.save_streams_to_file(dir, video_stream, audio_stream, title)


def main(url=None, path=None):
    if url is None:
        url = get_url()

    title, streams = get_data(url)
    video, audio = get_streams(title, streams)

    if path is None:
        path = get_dir_to_download()

    download(path, streams[video][0], streams[audio][0], title)


if __name__ == "__main__":
    main()
