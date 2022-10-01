from ast import pattern
from msilib.schema import ListBox
import tkinter as tk
import fnmatch
import os

from pygame import mixer 

canvas = tk.Tk()
canvas.title("Music player")
canvas.geometry("600x800")
canvas.config(bg='yellow')
rootpath= "C:\\Users\dell\Desktop\music"
pattern="*.mp3"



mixer.init()

def select():
    lable.config(text=ListBox.get("anchor"))
    mixer.music.load(rootpath + "\\" + ListBox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    ListBox.select_clear('active')

def play_next():
    next_song = ListBox.curselection()
    next_song=next_song[0]+1
    next_song_name=ListBox.get(next_song)  
    lable.config(text=next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    ListBox.select_clear(0,'end')
    ListBox.activate(next_song)
    ListBox.select_set(next_song)

def play_prev():
    next_song = ListBox.curselection()
    next_song=next_song[0]-1
    next_song_name=ListBox.get(next_song)  
    lable.config(text=next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    ListBox.select_clear(0,'end')
    ListBox.activate(next_song)
    ListBox.select_set(next_song)

def pause_song():
    if pauseButton["text"]=="Pause":
        mixer.music.pause()
        pauseButton["text"]="Play"
    else:
        mixer.music.unpause()
        pauseButton["text"]="Pause"    




ListBox=tk.Listbox(canvas,fg="black" , bg="white" , width=100 , font=('Times',14))
ListBox.pack(padx=15 , pady=15)

lable = tk.Label(canvas,text='',bg='red' ,fg='white',font=('Times',18))
lable.pack(pady=15)

top = tk.Frame(canvas,bg='yellow')
top.pack(padx=10,pady=5,anchor='center')

prevButton=tk.Button(canvas,text="Prev", command=play_prev)
prevButton.pack(pady=15,in_=top,side='left')

stopButton=tk.Button(canvas,text="Stop", command=stop)
stopButton.pack(pady=15,in_=top,side='left')

playButton=tk.Button(canvas,text="Play" , command=select)
playButton.pack(pady=15,in_=top,side='left')

pauseButton=tk.Button(canvas,text="Pause" , command=pause_song)
pauseButton.pack(pady=15,in_=top,side='left')

nextButton=tk.Button(canvas,text="Next" , command=play_next)
nextButton.pack(pady=15,in_=top,side='left')



for root , dirs,files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        ListBox.insert('end',filename)


canvas.mainloop()