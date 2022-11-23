from tkinter import *
from tkinter.ttk import *
import time
import random
from pygame import mixer

buttonlocations = [[100, 100], [200, 100], [100, 200], [200, 200]]

def step(audiolength):
    for i in range(audiolength):
        window.update_idletasks()
        progressbar['value'] += (100/audiolength)
        time.sleep(1)

mixer.init()
window = Tk()
frame = Frame(window)

progressbar = Progressbar(window, orient = HORIZONTAL, length = 100, mode='indeterminate')
progressbar.pack(expand = True)

window.title("Heardle")
window.geometry("700x500")

bert = mixer.Sound('bert.wav')

songs = [['bert.wav', 'bert', 'charles', 'ryan', 'miggle', 1, 7]]
songsplayed = [i for i in range(len(songs))]

for a in range(len(songs)):
    for b in range(4):
        uno = Button(frame, text = songs[a][b + 1])
        uno.place(x = 100, y = 100)
    step(songs[a][6])
        


mixer.Sound.play(bert)


window.mainloop()