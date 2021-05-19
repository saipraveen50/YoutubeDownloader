from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from pytube import YouTube
from tkinter import messagebox

# Main Window
root = tk.Tk()
root.geometry('650x500')
root.resizable(600, 500)
root.configure(bg='#368BC1')
root.title("Youtube video downloader")

# Combobox
video_types = ['360p', '480p', '720p', '1080p', 'mp3']
video_list = ttk.Combobox(root, width=7, values=video_types, font='Arial 21')


# Combobox class
class DropDownList(ttk.Combobox):
    def __init__(self, parent):
        ttk.Combobox.__init__(self, parent)  # init widget
        self.current(0)  # index of values for current table
        self.place(x=50, y=153)  # place drop down box


# Label
Label(root, text='Youtube Video Downloader', font='arial 20 bold', bg='#368BC1').pack()

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
        messagebox.showerror("Url Error", "Please provide correct URL")
    else:
        try:
            url = YouTube(str(link.get()))
            Label(root, text='Title:', font='arial 12').place(x=50, y=200)
            Label(root, text=url.title, font='arial 12', wraplength=300, justify="center").place(x=100, y=200)

        except:
            messagebox.showerror("Error", "Contact Administrator")

# Download
def Download():
    global video
    file_path = filedialog.askdirectory()
    if file_path == '':
        messagebox.showerror("Error", "Please Select a path")
    else:
        path.insert(tk.END, file_path)
    selected = video_list.get()
    if len(link.get()) < 1:
        messagebox.showerror("Url Error", "Please provide correct URL")
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
                video = url.streams.get_by_itag(251)
            Label(root, text='Size:', font='arial 12').place(x=50, y=250)
            Label(root, text=video.filesize, font='arial 12').place(x=130, y=250)
            try:
                if file_path != '':
                    video.download(file_path)
                else:
                    messagebox.showerror("Error", "Please Select a path")
                Label(root, text='DOWNLOADING...', font='arial 15', fg='blue').place(x=80, y=300)
                Label(root, text='DOWNLOADED', font='arial 15', fg='green').place(x=80, y=350)

            except:
                messagebox.showerror("Error", "Contact Administrator")
        except:
            messagebox.showerror("Error", "Contact Administrator")


# button
Button(root, text='Start', foreground='white', width=20, height=2, bg='red', command=Load_Video).place(x=473, y=47)
Button(root, text='Download', foreground='white', width=20, height=2, bg='red', command=Download).place(x=250, y=270)

video_list.place(x=110, y=272)
tk.mainloop()
