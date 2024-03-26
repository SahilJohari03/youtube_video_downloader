from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry(f'400x250')
root.title("Youtube Video Downloader")
THEME_COLOR = "#E72929"
Label(root, text='Youtube Video Downloader', font=('Arial', 16) ).pack()

link = StringVar()
filename = StringVar()

Label(root, text='Enter Youtube Video Link Here:',font=('Arial', 10)).place(x=100, y=40)
link_enter = Entry(root, width=45, textvariable=link).place(x=50,y=90)

def download():

    Label(root, text="Downloading", font='Arial, 10').place(x = 180, y  = 210)

    url = YouTube(str(link.get()))

    video = url.streams.get_highest_resolution()

    video.download()

    Label(root, text="Downloaded", font= 'arial, 15').place(x = 180, y =210)

Button(root, text='Download', font= 'arial, 15',padx= 1, command=download).place(x=140, y= 150)

root.mainloop()