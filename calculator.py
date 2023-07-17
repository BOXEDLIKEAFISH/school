# Kris Kuo
# Calculator GUI Assignment
# does not run properly in replit
# download and run python file
# November 16, 2022
# ICS4U1
# Ms. Townshend
from tkinter import *   # import tkinter 
from pygame import mixer

grey =  '#2C3333'   #colour and font variables
lightgrey = '#3F4E4F'
inputfont = ('helvetica', 20, 'bold')

mixer.init()   # initialize mixer 

bert = mixer.Sound('BertAudio.wav')  # load sound file

def button_press(num):  # when button is pressed
  global calcinput  # make variable global
  calcinput = calcinput + str(num)  # add inputted number to the equation text
  calcdisplay.set(calcinput)    # set display as the equation

def equals():   # when equal button is pressed
  global calcinput  # make variable global
  
  if calcinput == '4/8/2005':
    mixer.Sound.play(bert)

  try:
    output = str(eval(calcinput))   # evaluate equation text
    calcdisplay.set(output) # display output
    calcinput = output  # change equation variable to the evaluated output

  except SyntaxError:   # if equation has syntax error
    calcdisplay.set("Syntax Error") # display syntax error
    calcinput = ""  # reset equation text to blank

  except ZeroDivisionError: # if equation has a number divided by 0
    calcdisplay.set("Cannot Divide By Zero")    # display cannot divide by zero
    calcinput = ""  # reset equation text to blank

def clear():    # when clear button is pressed
  global calcinput  # make variable global
  calcinput = ""    # reset equation text to blank
  calcdisplay.set("")   # clear display

window = Tk()   # create window
window.title("Calculator")  # title window as calculator
window.geometry("364x500")  # set window size

calcinput = ""  # equation text

calcdisplay = StringVar()   # display text

label = Label(window, textvariable=calcdisplay, font= inputfont, bg= grey, fg = 'white', width=24, height=2)    # display variables
label.pack()    

frame = Frame(window)
frame.pack()

# all button variables

uno = Button(frame, text = 1, height = 4, width = 9, font = 35, bg = grey, fg = 'white', activebackground = lightgrey, activeforeground = 'white', command = lambda: button_press(1))
uno.grid(row = 3, column = 0)

dos = Button(frame, text = 2, height = 4, width = 9, font = 35, bg = grey, fg = 'white', activebackground = lightgrey, activeforeground = 'white', command = lambda: button_press(2))
dos.grid(row = 3, column = 1)

tres = Button(frame, text = 3, height = 4, width = 9, font = 35, bg = grey, fg = 'white', activebackground = lightgrey, activeforeground = 'white', command = lambda: button_press(3))
tres.grid(row = 3, column = 2)

quatro = Button(frame, text = 4, height = 4, width = 9, font = 35, bg = grey, fg = 'white', activebackground = lightgrey, activeforeground = 'white', command = lambda: button_press(4))
quatro.grid(row = 2, column = 0)

cinco = Button(frame, text = 5, height = 4, width = 9, font = 35, bg = grey, fg = 'white', activebackground = lightgrey, activeforeground = 'white', command = lambda: button_press(5))
cinco.grid(row = 2, column = 1)

seis = Button(frame, text = 6, height = 4, width = 9, font = 35, bg = grey, fg = 'white', activebackground = lightgrey, activeforeground = 'white', command = lambda: button_press(6))
seis.grid(row = 2, column = 2)

siete = Button(frame, text = 7, height = 4, width = 9, font = 35, bg = grey, fg = 'white', activebackground = lightgrey, activeforeground = 'white', command = lambda: button_press(7))
siete.grid(row = 1, column = 0)

ocho = Button(frame, text = 8, height = 4, width = 9, font = 35, bg = grey, fg = 'white', activebackground = lightgrey, activeforeground = 'white', command = lambda: button_press(8))
ocho.grid(row = 1, column = 1)

nueve = Button(frame, text = 9, height = 4, width = 9, font = 35, bg = grey, fg = 'white', activebackground = lightgrey, activeforeground = 'white', command = lambda: button_press(9))
nueve.grid(row = 1, column = 2)

cero = Button(frame, text = 0, height = 4, width = 9, font = 35, bg = grey, fg = 'white', activebackground = lightgrey, activeforeground = 'white', command = lambda: button_press(0))
cero.grid(row = 4, column = 1)

decimal = Button(frame, text = '.', height = 4, width = 9, font = 35, bg = grey, fg = 'white', activebackground = lightgrey, activeforeground = 'white', command = lambda: button_press('.'))
decimal.grid(row = 4, column = 2)

clear = Button(frame, text = 'CLR', height = 4, width = 9, font = 35, bg = grey, fg = 'white', activebackground = lightgrey, activeforeground = 'white', command = clear)
clear.grid(row = 4, column = 0)

multiply = Button(frame, text = 'X', height = 4, width = 9, font = 35, bg = grey, fg = 'white', activebackground = lightgrey, activeforeground = 'white', command = lambda: button_press('*'))
multiply.grid(row = 0, column = 3)

divide = Button(frame, text = '÷', height = 4, width = 9, font = 35, bg = grey, fg = 'white', activebackground = lightgrey, activeforeground = 'white', command = lambda: button_press('/'))
divide.grid(row = 1, column = 3)

addition = Button(frame, text = '+', height = 4, width = 9, font = 35, bg = grey, fg = 'white', activebackground = lightgrey, activeforeground = 'white', command = lambda: button_press('+'))
addition.grid(row = 2, column = 3)

subtraction = Button(frame, text = '-', height = 4, width = 9, font = 35, bg = grey, fg = 'white', activebackground = lightgrey, activeforeground = 'white', command = lambda: button_press('-'))
subtraction.grid(row = 3, column = 3)

leftbracket = Button(frame, text = '(', height = 4, width = 9, font = 35, bg = grey, fg = 'white', activebackground = lightgrey, activeforeground = 'white', command = lambda: button_press('('))
leftbracket.grid(row = 0, column = 0)

rightbracket = Button(frame, text = ')', height = 4, width = 9, font = 35, bg = grey, fg = 'white', activebackground = lightgrey, activeforeground = 'white', command = lambda: button_press(')'))
rightbracket.grid(row = 0, column = 1)

power = Button(frame, text = '^', height = 4, width = 9, font = 35, bg = grey, fg = 'white', activebackground = lightgrey, activeforeground = 'white', command = lambda: button_press('**'))
power.grid(row = 0, column = 2)

equal = Button(frame, text = '=', height = 4, width = 9, font = 35, bg = grey, fg = 'white', activebackground = lightgrey, activeforeground = 'white', command = equals)
equal.grid(row = 4, column = 3)



window.mainloop()   # loops program