from tkinter import *
import tkinter.ttk as ttk
import time
import random
from pygame import mixer

black = '#121212'
grey = '#BEBDB8'
green = '#00FF00'
red = '#FF0000'

gameovermessage = ['Unlucky!', 'Nice try!', 'Michael moment.', 'Good effort!', 'Better luck next time!', 'You can do better!', 'That\'s barely a pass.', 'Almost there!', 'Nice!', 'Almost perfect!', 'Perfect!']

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
    if songs[a][buttonpressed + 4] == green:
        points.set(int(points.get()) + 1)
    if a < len(songs):
        a += 1
    if a < len(songs):
        uno.config(text = songs[a][1], activebackground = songs[a][5])
        dos.config(text = songs[a][2], activebackground = songs[a][6])
        tres.config(text = songs[a][3], activebackground = songs[a][7])
        quatro.config(text = songs[a][4], activebackground = songs[a][8])
    else:
        gameover()
        
def gameover():
    progressbar.destroy()
    playbutton.destroy()
    pointcounter.destroy()
    pointcountertext.destroy()
    uno.destroy()
    dos.destroy()
    tres.destroy()
    quatro.destroy()
    gameovertext = Label(window, text = gameovermessage[int(points.get())], font = ('Times New Roman', 40), bg = black, fg = grey)
    gameovertext.grid(column = 0, row = 4)
    gameovertext2 = Label(window, text = 'Points:' + str(points.get()) + '/10', font = ('Times New Roman', 40), bg = black, fg = grey)
    gameovertext2.grid(column = 0, row = 5)


mixer.init()
window = Tk()
window.grid()
frame = Frame(window)
window.title('Heardle')
window.geometry('550x500')
window.configure(background = black)

points = StringVar(value = 0)

style = ttk.Style()
style.configure('fish', foreground = 'black', background = 'white')

progressbar = ttk.Progressbar(window, orient = HORIZONTAL, length = 400, mode = 'determinate')
progressbar.grid(column = 0, row = 1, columnspan = 1, padx = 10, pady = 20)


logo = Label(window, width = 10, height = 2, text = 'Heardle', font = ('Times New Roman', 40), background = black, foreground = 'white')
logo.grid(column = 0, row = 0, columnspan = 1, padx = 120)

pointcountertext = Label(window, width = 5, height = 1, text = 'Points:', font = ('Times New Roman', 20), bg = black, foreground = 'white')
pointcountertext.place(x = 350, y = 85)

pointcounter = Label(window, width = 1, height = 1, textvariable = points, font = ('Times New Roman', 20), background = black, foreground = 'white')
pointcounter.place(x = 450, y = 85)


songs = [
['bert.wav', 'bertyyyyyyyyyyyyyyy', 'charles', 'ryan', 'miggle', green, red, red, red, 7],
['bert.wav', 'fishy', 'shesh', 'ri call ryna', 'migga', red, red, green, red, 7]
]

#order = [random.randint(0, len(songs)-1) for i in range(len(songs))] 


playbutton = Button(window, width = 8, height = 1, text = 'Play', command = lambda: movebar(songs[a][0], songs[a][9]))
playbutton.place(x = 30, y = 95)


uno = Button(window, width = 70, height = 2, font = ('Times New Roman', 10), text = songs[a][1], background = black, foreground = 'white', activebackground = songs[a][5], command = lambda: answer(1))
uno.grid(row = 3, column = 0, padx = 10, pady = 15)

dos = Button(window, width = 70, height = 2, font = ('Times New Roman', 10), text = songs[a][2], background = black, foreground = 'white', activebackground = songs[a][6], command = lambda: answer(2))
dos.grid(row = 4, column = 0, padx = 10, pady = 15)

tres = Button(window, width = 70, height = 2, font = ('Times New Roman', 10), text = songs[a][3], background = black, foreground = 'white', activebackground = songs[a][7], command = lambda: answer(3))
tres.grid(row = 5, column = 0, padx = 10, pady = 15)

quatro = Button(window, width = 70, height = 2, font = ('Times New Roman', 10), text = songs[a][4], background = black, foreground = 'white', activebackground = songs[a][8], command = lambda: answer(4))
quatro.grid(row = 6, column = 0, padx = 10, pady = 15)
    
window.mainloop()