from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from pytube import YouTube

# Main Window
root = tk.Tk()
root.geometry('650x500')
root.resizable(600, 500)
root.title("Youtube video downloader")

# Combobox
video_types = ['360p', '480p', '720p', '1080p', 'mp3']
video_list = ttk.Combobox(root, width="10", values=video_types)


# Combobox class
class DropDownList(ttk.Combobox):
    def __init__(self, parent):
        ttk.Combobox.__init__(self, parent)  # init widget
        self.current(0)  # index of values for current table
        self.place(x=50, y=153)  # place drop down box


# Label
Label(root, text='Youtube Video Downloader', font='arial 20 bold').pack()

# link textbox
link = StringVar()
link_enter = Entry(root, width=70, textvariable=link).place(x=23, y=50, height=37)

# Text and label
path = Text(root, height=1, width=67)
file_path = ''
path.place(x=83, y=103)
Label(root, text='Path', font='arial 13', width=5, height=1, foreground='white', bg='red').place(x=23, y=100)

global video

# To load video details
def Load_Video():
    selected = video_list.get()
    if len(link.get()) < 1:
        Label(root, text='Please provide correct URL', font='arial 15', foreground='white', bg='red').place(x=210,
                                                                                                            y=200)

    else:
        try:
            url = YouTube(str(link.get()))
            Label(root, text=url.title, font='arial 12').place(x=100, y=200)
            # Label(root, text=url.description, font='arial 12').place(x=100, y=230)
        except:
            Label(root, text='Error', font='arial 15').place(x=80, y=300)

# To Download
def Download():
    global video
    file_path = filedialog.askdirectory()
    path.insert(tk.END, file_path)
    selected = video_list.get()
    if len(link.get()) < 1:
        Label(root, text='Please provide correct URL', font='arial 15', foreground='white', bg='red').place(x=210,
                                                                                                            y=200)
    else:
        try:
            url = YouTube(str(link.get()))
            print(url.streams)
            if selected == video_types[0]:
                video = url.streams.filter(res="360p").first()
            elif selected == video_types[1]:
                video = url.streams.filter(res="480p").first()
            elif selected == video_types[2]:
                video = url.streams.filter(res="720p").first()
            elif selected == video_types[3]:
                video = url.streams.filter(res="1080p").first()
            elif selected == video_types[4]:
                video = url.streams.filter(only_audio=True).first()

            try:
                video.download(file_path)
                Label(root, text='DOWNLOADING...', font='arial 15', fg='blue').place(x=80, y=300)
                Label(root, text='DOWNLOADED', font='arial 15', fg='green').place(x=80, y=350)

            except:
                Label(root, text='Error', font='arial 15').place(x=80, y=300)
        except:
            Label(root, text='Error', font='arial 15').place(x=80, y=300)


# button
Button(root, text='Start', foreground='white', width=20, height=2, bg='red', command=Load_Video).place(x=473, y=47)
Button(root, text='Download', foreground='white', width=20, height=2, bg='red', command=Download).place(x=250, y=250)

video_list.place(x=20, y=150)
tk.mainloop()
