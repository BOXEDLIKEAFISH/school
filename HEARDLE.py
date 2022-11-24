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

gameovermessage = ['unlucky tbh💀x7', 'nt brotha go next', 'michael moment(alliteration)', 'nt.', '💀',  # list of game over messages
 'passing grade', 'barely a pass💀', 'michael on derivatives', 'nt close game', 'sheeah', 'sheesh']

    # list of songs, text for each button (4), colours of each button when clicked (4), and the duration of the song
songs = [
    ['bert.wav', 'bertyyyyyyyyyyyyyyy', 'charles', 'ryan', 'miggle', green, red, red, red, 7],
    ['bert.wav', 'fishy', 'shesh', 'ri call ryna', 'migga', red, red, green, red, 7]
]

songorder = random.sample(range(len(songs)), len(songs))    # generates random order for the songs
buttonorder = random.sample(range(1, 5), 4) # generates random order for the buttons

a = songorder[0]   # variable for song number

def movebar(song, audiolength): # function for the progress bar
    global a
    progressbar['value'] = 0
    sound = mixer.Sound(song)   # plays the song
    mixer.Sound.play(sound)
    increment = 100/audiolength # calculates the increment for the progress bar
    for i in range(audiolength):
        progressbar['value'] += increment   # increments the progress bar
        window.update_idletasks()   # updates the progress bar
        time.sleep(1)
    progressbar['value'] = 0

def answer(buttonpressed):  # function for when a button is pressed
    global a
    global points
    global buttonorder
    if songs[a][4 + buttonorder[buttonpressed - 1]] == green:   # if the button pressed is the correct answer
        points.set(int(points.get()) + 1)   # add a point
    if len(songorder) > 1:  # if there are more songs
        del(songorder[0])   # delete the song that was just played from list of songs
        a = songorder[0]    # set the song number to the next song
        buttonorder = random.sample(range(1, 5), 4) # generate a new random order for the buttons
        uno.config(text = songs[a][buttonorder[0]], activebackground = songs[a][buttonorder[0] + 4])    # change the text and pressed colour of the buttons
        dos.config(text = songs[a][buttonorder[1]], activebackground = songs[a][buttonorder[1] + 4])
        tres.config(text = songs[a][buttonorder[2]], activebackground = songs[a][buttonorder[2] + 4])
        quatro.config(text = songs[a][buttonorder[3]], activebackground = songs[a][buttonorder[3] + 4])
    else:
        gameover()  # if there are no more songs, end the game

def gameover(): # function for when the game ends
    progressbar.destroy()   # destroy all buttons and progress bar
    playbutton.destroy()
    pointcounter.destroy()
    pointcountertext.destroy()
    uno.destroy()
    dos.destroy()
    tres.destroy()
    quatro.destroy()
    gameovertext = Label(window, text = gameovermessage[int(points.get())], font = ('Times New Roman', 40), bg = black, fg = grey)  # display the game over message from the list
    gameovertext.grid(column = 0, row = 4)
    gameovertext2 = Label(window, text = 'Points:' + str(points.get()) + '/10', font = ('Times New Roman', 40), bg = black, fg = grey)  # display the points
    gameovertext2.grid(column = 0, row = 5)

    amogus = ImageTk.PhotoImage(Image.open('amogus.png'))   # display the amogus image
    amoguslabel = Label(image = amogus, background = black)
    amoguslabel.image = amogus
    amoguslabel.grid(column = 0, row = 6)


mixer.init()    # initialize mixer
window = Tk()   # initialize window
window.grid()   # grid the window
window.title('Heardle') # title of the window
window.geometry('550x500')  # size of the window
window.configure(background = black)    # background colour of the window

points = StringVar(value = 0)   # variable for the points


progressbar = ttk.Progressbar(window, orient = HORIZONTAL, length = 400, mode = 'determinate')  # progress bar
progressbar.grid(column = 0, row = 1, columnspan = 1, padx = 10, pady = 20)


logo = Label(window, width = 10, height = 2, text = 'Heardle', font = ('Times New Roman', 40), background = black, foreground = 'white')    # Heardle text at the top
logo.grid(column = 0, row = 0, columnspan = 1, padx = 120)

pointcountertext = Label(window, width = 5, height = 1, text = 'Points:', font = ('Times New Roman', 20), bg = black, foreground = 'white') # points text
pointcountertext.place(x = 350, y = 85)

pointcounter = Label(window, width = 1, height = 1, textvariable = points, font = ('Times New Roman', 20), background = black, foreground = 'white')    # points counter
pointcounter.place(x = 450, y = 85)


playbutton = Button(window, width = 8, height = 1, text = 'Play', command = lambda: movebar(songs[a][0], songs[a][9]))  # play button
playbutton.place(x = 30, y = 95)



uno = Button(window, width = 70, height = 2, font = ('Times New Roman', 10), text = songs[a][buttonorder[0]], background = black,   # button 1
 foreground = 'white', activebackground = songs[a][4 + buttonorder[0]], command = lambda: answer(1))
uno.grid(row = 3, column = 0, padx = 10, pady = 15)

dos = Button(window, width = 70, height = 2, font = ('Times New Roman', 10), text = songs[a][buttonorder[1]], background = black,   # button 2
 foreground = 'white', activebackground = songs[a][4 + buttonorder[1]], command = lambda: answer(2))
dos.grid(row = 4, column = 0, padx = 10, pady = 15)

tres = Button(window, width = 70, height = 2, font = ('Times New Roman', 10), text = songs[a][buttonorder[2]], background = black,  # button 3
 foreground = 'white', activebackground = songs[a][4 + buttonorder[2]], command = lambda: answer(3))
tres.grid(row = 5, column = 0, padx = 10, pady = 15)

quatro = Button(window, width = 70, height = 2, font = ('Times New Roman', 10), text = songs[a][buttonorder[3]], background = black,    # button 4
 foreground = 'white', activebackground = songs[a][4 + buttonorder[3]], command = lambda: answer(4))
quatro.grid(row = 6, column = 0, padx = 10, pady = 15)
    
window.mainloop()   # main loop