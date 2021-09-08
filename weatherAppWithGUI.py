import tkinter
from tkinter import *
import tkinter.font as font
import tkinter.messagebox
import requests
from tkinter import messagebox
from tkinter.ttk import *

##API and location data##
userAPI = ('e435fe87b015546cf0e0ee1228b79dd4')
location = ('doncaster')

completeAPILink = ("https://api.openweathermap.org/data/2.5/weather?q="+(location)+"&appid="+(userAPI))

APILink = requests.get(completeAPILink)
APIData = APILink.json()


if APIData['cod'] == '404':
    print("invalid city name")

##weather data pull##
cityTemp = ((APIData['main']['temp']) - 273.15)
cityTempFeelsLike = ((APIData)['main']['feels_like'] - 273.15)
cityHumidity = ((APIData['main']['humidity']))
cityWeatherDescription = ((APIData['weather'][0]['description']))
cityWindSpeed = ((APIData['wind']['speed']))

##convert data into strings##
cityTemp = str(cityTemp)
cityTempFeelsLike = str(cityTempFeelsLike)
cityHumidity = str(cityHumidity)
cityWindSpeed = str(cityWindSpeed)

##update weather function##
def weatherUpdate():
    cTempLabel = Label(wethWindow, text = ("current temperature: "+(cityTemp[:4]+"ºC"))).place(relx = 0.5, rely = 0.3, relwidth = 0.9, relheight = 0.1, anchor = CENTER)
    cFeelLabel = Label(wethWindow, text = ("It currently feels like: "+(cityTempFeelsLike[:4]+"ºC"))).place(relx = 0.5, rely = 0.4, relwidth = 0.9, relheigh = 0.1, anchor = CENTER)
    cHumidity = Label(wethWindow, text = ("The current humidity is: "+(cityHumidity))).place(relx = 0.5, rely = 0.5, relwidth = 0.9, relheight = 0.1, anchor = CENTER)
    cDescLabel = Label(wethWindow, text = ("The current weather is: "+(cityWeatherDescription))).place(relx = 0.5, rely = 0.6, relwidth = 0.9, relheight = 0.1, anchor = CENTER)
    cWindSpeed = Label(wethWindow, text = ("The current wind speed is: "+(cityWindSpeed+"mph"))).place(relx = 0.5, rely = 0.7, relwidth = 0.9, relheight = 0.1, anchor = CENTER)

##window declaration##
wethWindow = tkinter.Tk()

##font declaration##
myfont = font.Font(family = 'Helvetica')

##window settings##
wethWindow.title("Current Weather")
wethWindow.geometry("400x400")
wethWindow.configure(bg = 'light blue')
cTempLabel = Label(wethWindow, text = ("current temperature: "+(cityTemp[:4]+"ºC"))).place(relx = 0.5, rely = 0.3, relwidth = 0.9, relheight = 0.1, anchor = CENTER)
cFeelLabel = Label(wethWindow, text = ("It currently feels like: "+(cityTempFeelsLike[:4]+"ºC"))).place(relx = 0.5, rely = 0.4, relwidth = 0.9, relheight = 0.1, anchor = CENTER)
cHumidity = Label(wethWindow, text = ("The current humidity is: "+(cityHumidity))).place(relx = 0.5, rely = 0.5, relwidth = 0.9, relheight = 0.1, anchor = CENTER)
cDescLabel = Label(wethWindow, text = ("The current weather is: "+(cityWeatherDescription))).place(relx = 0.5, rely = 0.6, relwidth = 0.9, relheight = 0.1, anchor = CENTER)
cWindSpeed = Label(wethWindow, text = ("The current wind speed is: "+(cityWindSpeed+"mph"))).place(relx = 0.5, rely = 0.7, relwidth = 0.9, relheight = 0.1, anchor = CENTER)

##update button##
updateButton = tkinter.Button(wethWindow, text="update forecast", font = myfont, bd = 7, fg = 'blue', activeforeground = 'red', height = 2, command = weatherUpdate)
updateButton.place(relx = 0.5, rely = 0.8, anchor = CENTER)

##program run function##
mainloop()