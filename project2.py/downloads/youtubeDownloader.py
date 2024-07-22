from pytube import YouTube
import pytube
from pytube import Playlist
from tkinter import *

window = Tk()
window.config(background="red")
window.title("YouTube Downloader")

def video_download():
    video_url = entry.get()
    vt = YouTube(video_url)
    print(f"Downloading {vt.title}")
    stream = vt.streams.get_highest_resolution()
    stream.download()
    print(f"Successfully downloaded {vt.title}")
    
def playlist_download():
    playlist_url = entry.get()
    yt = Playlist(playlist_url)
    print(f"Downloading {yt.title}\n")
    
    for x in yt.video:
        print(f"Downloading {x.title()}")
        x.streams.get_highest_resolution().download()
        print(f"Succefully downloaded {x.title}")
    print(f"Successfully downloaded {yt.title}")
    
def clearing():
    entry.delete(0, END)
    
label = Label(window,
              bg="#000",
              fg="red",
              text="Input the url of the video in the field blew:")

entry = Entry(window,
              bg="grey",
              fg="blue")

video_button = Button(window,
                      bg="#000",
                      fg="red",
                      command=video_download,
                      text="Download video")
clear = Button(window,
               text="Clear",
               bg="green",
               fg="red",
               command=clearing)
playlist_button = Button(window,
                         bg="#000",
                         fg="red",
                         command=playlist_download,
                         text="Download Playlist")

label.pack()
entry.pack()
video_button.pack()
playlist_button.pack()
clear.pack()
window.mainloop()