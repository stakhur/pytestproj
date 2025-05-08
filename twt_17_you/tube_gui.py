import tkinter as tk
from tkinter import filedialog, ttk

import tools

class App(tk.Tk):
    def __init__(self, url="", path=""):
        super().__init__()
        self.url = url
        self.save_path = path
        self.build_structure()

    def build_structure(self):
        self.title = "Video downloader"

        frm_input = tk.Frame()
        frm_input.pack(fill=tk.BOTH, expand=True)
        tk.Label(master=frm_input, text="Link:").pack(side=tk.LEFT, padx=5, pady=5)
        self.ent_link = tk.Entry(master=frm_input)
        self.ent_link.insert(0, self.url)
        self.ent_link.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)
        btn_getData = tk.Button(master=frm_input, text="Get Data", command=self.get_data)
        btn_getData.pack(side=tk.RIGHT, padx=5, pady=5)
        
        self.title_var = tk.StringVar(name="Title", value="")
        self.ent_title = tk.Entry(state="readonly", textvariable=self.title_var)
        self.ent_title.pack(fill=tk.X)

        frm_streams = tk.LabelFrame(text="Streams")
        frm_streams.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        tk.Label(master=frm_streams, text="Video: ").pack(side=tk.LEFT, padx=5, pady=5)
        self.cmb_video = ttk.Combobox(master=frm_streams, state="readonly")
        self.cmb_video.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)
        tk.Label(master=frm_streams, text="Audio: ").pack(side=tk.LEFT, padx=5, pady=5)
        self.cmb_audio = ttk.Combobox(master=frm_streams, state="readonly")
        self.cmb_audio.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)

        frm_output = tk.Frame()
        frm_output.pack(fill=tk.BOTH, expand=True)
        tk.Label(master=frm_output, text="Save to: ").pack(side=tk.LEFT, padx=5, pady=5)
        self.ent_dir = tk.Entry(master=frm_output)
        self.ent_dir.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)
        self.ent_dir.insert(0, self.save_path)
        btn_chooseFolder = tk.Button(master=frm_output, text="...", command=self.get_dir_to_save)
        btn_chooseFolder.pack(side=tk.RIGHT, padx=5, pady=5)
        
        frm_btns = tk.Frame()
        frm_btns.pack(fill=tk.BOTH)
        btn_quit = tk.Button(master=frm_btns, text="Quit", command=self.destroy)
        btn_quit.pack(side=tk.LEFT, padx=5, pady=5)
        btn_save = tk.Button(master=frm_btns, text="Save", command=self.save)
        btn_save.pack(side=tk.RIGHT, padx=5, pady=5)

        self.ent_status = tk.Entry(state="readonly")
        self.ent_status.pack(fill=tk.X)


    def get_data(self):
        try:
            url = self.ent_link.get()
            self.title = tools.get_title(url)
            self.streams = tools.get_all_streams(url)

            self.title_var.set(self.title)

            video_streams = tools.get_stream_names(self.streams, "video")
            self.cmb_video["values"] = video_streams
            self.cmb_video.current(0)

            audio_streams = tools.get_stream_names(self.streams, "audio")
            self.cmb_audio["values"] = audio_streams
            self.cmb_audio.current(0)
        except Exception as e:
            print(e)
        
    
    def get_dir_to_save(self):
        folder = filedialog.askdirectory()
        if folder:
            self.ent_dir.delete(0, tk.END)
            self.ent_dir.insert(0, folder)
            self.save_path = folder

    
    def save(self):
        try:
            selected_video_stream = self.cmb_video.get()
            video_stream = self.streams[selected_video_stream][0]

            selected_audio_stream = self.cmb_audio.get()
            audio_stream = self.streams[selected_audio_stream][0]

            tools.save_streams_to_file(self.save_path, video_stream, audio_stream, self.title)
        except Exception as e:
            print(e)


def main(url="https://www.youtube.com/watch?v=TkvRsGstk-w", path=None):
    app = App(url, path)
    app.mainloop()


if __name__== "__main__":
    main()
