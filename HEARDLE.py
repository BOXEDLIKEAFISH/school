# Kris Kuo
# GUI Trivia Game
# Heardle
# November 23, 2022
# ICS4U1
# Ms. Townshend

from tkinter import *   # import libraries
import tkinter.ttk as ttk
import time
import random
from pygame import mixer
from PIL import ImageTk, Image

black = '#121212'   # hex codes for colours
grey = '#BEBDB8'
green = '#00FF00'
red = '#FF0000'

gameovermessage = ['Unlucky tbh💀x7', 'Nice try!', 'Michael moment.', 'Good effort!', 'Better luck next time!', 'You can do better!', 'That\'s barely a pass.', 'Almost there!', 'Nice!', 'Almost perfect!', 'Perfect!']

songs = [
['bert.wav', 'bertyyyyyyyyyyyyyyy', 'charles', 'ryan', 'miggle', green, red, red, red, 7],
['bert.wav', 'fishy', 'shesh', 'ri call ryna', 'migga', red, red, green, red, 7]
]

songorder = random.sample(range(len(songs)), len(songs))
buttonorder = random.sample(range(1, 5), 4)


a = songorder[0]   # variable for song number


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
    global buttonorder
    if songs[a][4 + buttonorder[buttonpressed - 1]] == green:
        points.set(int(points.get()) + 1)
    if len(songorder) > 1:
        del(songorder[0])
        a = songorder[0]
        buttonorder = random.sample(range(1, 5), 4)
        uno.config(text = songs[a][buttonorder[0]], activebackground = songs[a][buttonorder[0] + 4])
        dos.config(text = songs[a][buttonorder[1]], activebackground = songs[a][buttonorder[1] + 4])
        tres.config(text = songs[a][buttonorder[2]], activebackground = songs[a][buttonorder[2] + 4])
        quatro.config(text = songs[a][buttonorder[3]], activebackground = songs[a][buttonorder[3] + 4])
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

    amogus = ImageTk.PhotoImage(Image.open('amogus.png'))
    amoguslabel = Label(image = amogus, background = black)
    amoguslabel.image = amogus
    amoguslabel.grid(column = 0, row = 6)


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


playbutton = Button(window, width = 8, height = 1, text = 'Play', command = lambda: movebar(songs[a][0], songs[a][9]))
playbutton.place(x = 30, y = 95)


uno = Button(window, width = 70, height = 2, font = ('Times New Roman', 10), text = songs[a][buttonorder[0]], background = black, foreground = 'white', activebackground = songs[a][4 + buttonorder[0]], command = lambda: answer(1))
uno.grid(row = 3, column = 0, padx = 10, pady = 15)

dos = Button(window, width = 70, height = 2, font = ('Times New Roman', 10), text = songs[a][buttonorder[1]], background = black, foreground = 'white', activebackground = songs[a][4 + buttonorder[1]], command = lambda: answer(2))
dos.grid(row = 4, column = 0, padx = 10, pady = 15)

tres = Button(window, width = 70, height = 2, font = ('Times New Roman', 10), text = songs[a][buttonorder[2]], background = black, foreground = 'white', activebackground = songs[a][4 + buttonorder[2]], command = lambda: answer(3))
tres.grid(row = 5, column = 0, padx = 10, pady = 15)

quatro = Button(window, width = 70, height = 2, font = ('Times New Roman', 10), text = songs[a][buttonorder[3]], background = black, foreground = 'white', activebackground = songs[a][4 + buttonorder[3]], command = lambda: answer(4))
quatro.grid(row = 6, column = 0, padx = 10, pady = 15)
    
window.mainloop()