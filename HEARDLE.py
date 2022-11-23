from tkinter import *
import tkinter.ttk as ttk
import time
import random
from pygame import mixer

grey = '#121212'
green = '#00FF00'

a = 0

def movebar(song, audiolength):
    global a
    progressbar['value'] = 0
    sound = mixer.Sound(song)
    mixer.Sound.play(sound)
    increment = 100/audiolength
    for i in range(audiolength):
        progressbar['value'] += increment
        window.update_idletasks()
        time.sleep(1)

def answer(buttonpressed):
    global a
    global points
    if buttonpressed == songs[a][5]:
        points.set(int(points.get()) + 1)
    if a < len(songs):
        a += 1
    
    uno.config(text = songs[a][1])
    dos.config(text = songs[a][2])
    tres.config(text = songs[a][3])
    quatro.config(text = songs[a][4])



mixer.init()
window = Tk()
window.grid()
frame = Frame(window)
window.title('Heardle')
window.geometry('550x500')
window.configure(background = grey)

points = StringVar(value = 0)

style = ttk.Style()
style.configure('fish', foreground = 'black', background = 'white')

progressbar = ttk.Progressbar(window, orient = HORIZONTAL, length = 400, mode = 'determinate')
progressbar.grid(column = 0, row = 1, columnspan = 1, padx = 10, pady = 20)


logo = Label(window, width = 10, height = 2,text = 'Heardle', font = ('Times New Roman', 40), background = grey, foreground = 'white')
logo.grid(column=0, row=0, columnspan=3, padx = 10)

pointcountertext = Label(window, width = 5, height = 1, text = 'Points:', font = ('Times New Roman', 20), bg = grey, foreground = 'white')
pointcountertext.place(x = 350, y = 85)

pointcounter = Label(window, width = 1, height = 1, textvariable = points, font = ('Times New Roman', 20), background = grey, foreground = 'white')
pointcounter.place(x = 450, y = 85)


songs = [['bert.wav', 'bertyyyyyyyyyyyyyyy', 'charles', 'ryan', 'miggle', 1, 7], ['bert.wav', 'FISH', 'charles', 'ryan', 'miggle', 1, 7]]
#order = [random.randint(0, len(songs)-1) for i in range(len(songs))] 


buttonpress = 0

playbutton = Button(window, width = 8, height = 1, text = 'Play', command = lambda: movebar(songs[a][0], songs[a][6]))
playbutton.place(x = 30, y = 95)


uno = Button(window, width = 70, height = 2, font = ('Times New Roman', 10), text = songs[a][1], background = grey, foreground = 'white', command = lambda: answer(1))
uno.grid(row = 3, column = 0, padx = 10, pady = 15)

dos = Button(window, width = 70, height = 2, font = ('Times New Roman', 10), text = songs[a][2], background = grey, foreground = 'white', command = lambda: answer(2))
dos.grid(row = 4, column = 0, padx = 10, pady = 15)

tres = Button(window, width = 70, height = 2, font = ('Times New Roman', 10), text = songs[a][3], background = grey, foreground = 'white', command = lambda: answer(3))
tres.grid(row = 5, column = 0, padx = 10, pady = 15)

quatro = Button(window, width = 70, height = 2, font = ('Times New Roman', 10), text = songs[a][4], background = grey, foreground = 'white', command = lambda: answer(4))
quatro.grid(row = 6, column = 0, padx = 10, pady = 15)
    
window.mainloop()