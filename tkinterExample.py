import tkinter
from tkinter import *
import tkinter.font as font 
import tkinter.messagebox

def messageCall():
    tkinter.messagebox.showinfo("hello world", "hello world")
screen = tkinter.Tk() 
myfont = font.Font(family = 'american typewriter') #creates a font variable to be used
screen.geometry("250x250") #window size
screen.title("window title") #window title
b = tkinter.Button(screen, text="Click here", font = myfont, bd = 7, fg = 'blue', activeforeground = 'red', height = 2, command = messageCall) #creates a button variable
b.place(relx = 0.5, rely = 0.5, anchor = CENTER) #places the button variable
screen.mainloop() #required to start instructions