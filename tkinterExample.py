import tkinter
from tkinter import *
import tkinter.font as font 
from tkintermapview import TkinterMapView

highlightedLocation = "Doncaster England"

#configuration of the main screen of the app
screen = tkinter.Tk() 
myfont = font.Font(family = 'american typewriter') #creates a font variable to be used
screen.geometry("1920x1080") #window size
screen.title("brighter futures bus application") #window title
screen.config(bg="#8D16D8")

#function to create the map, this is changeable with numerical values to fit any size
#function takes 5 parameters, location to place marker, height and width of window, height and width of the map border
def createMap(Location, windowWidth, windowHeight, bordWidth, bordHeight):
    #defines the border of the map
    border = Label(bg="yellow")
    border.config(width=bordWidth, height=bordHeight)
    border.place(relx=0.2, rely=0.53, anchor=CENTER)
    #defines the map and places it
    map_widget = TkinterMapView(screen, width=windowWidth, height=windowHeight, corner_radius=0)
    map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
    map_widget.set_address(Location, marker=True)
    map_widget.place(relx=0.2, rely=0.53, anchor=CENTER)

#creates an empty white header and places it at the top of the screen
def createHeader():
    header = Label(bg="white")
    header.config(width=500, height=3)
    header.place(relx=0.5, rely=0, anchor=N)

#calls the header and map functions
func=createHeader()
func=createMap(highlightedLocation, 400, 600, 45, 38)

screen.mainloop() #required to start instructions