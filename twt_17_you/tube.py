import argparse

import tube_cli
try:
    import tube_gui
    gui_ready=True
except:
    gui_ready=False

def main():
    parser = argparse.ArgumentParser(description="Video downloader")
    parser.add_argument("--gui", action='store_true', help="An optional - run gui")
    parser.add_argument("--url", type=str, help="An optional link to the video")
    parser.add_argument("--path", type=str, help="An optional path to save video")
    args = parser.parse_args()

    gui = args.gui
    url = args.url
    if url is None:
        url = ""
    path = args.path
    if path is None:
        path = ""

    if gui:
        if gui_ready:
            tube_gui.main(url, path)
            return
        else:
            print("Cannot import gui. Running cli...")
    tube_cli.main(url, path)

if __name__ == "__main__":
    main()
