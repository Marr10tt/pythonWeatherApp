import requests
from datetime import datetime

userAPI = ('e435fe87b015546cf0e0ee1228b79dd4')
location = input("Enter city name: ")

completeAPILink = "https://api.openweathermap.org/data/2.5/weather?q="+(location)+"&appid="+(userAPI)

APILink = requests.get(completeAPILink)
APIData = APILink.json()


if APIData['cod'] == '404':
    print("invalid city name")
else:
    cityTemp = ((APIData['main']['temp']) - 273.15)
    cityTempFeelsLike = ((APIData)['main']['feels_like'] - 273.15)
    cityHumidity = ((APIData['main']['humidity']))
    cityWeatherDescription = ((APIData['weather'][0]['description']))
    cityWindSpeed = ((APIData['wind']['speed']))

    cityTemp = str(cityTemp)
    cityTempFeelsLike = str(cityTempFeelsLike)
    cityHumidity = str(cityHumidity)
    cityWeatherDescription = str(cityWeatherDescription)
    cityWindSpeed = str(cityWindSpeed)

    print("The current temperature in "+(location)+" is: "+(cityTemp[:4])+"°C") 
    print("The current temperature in "+(location)+" feels like: "+(cityTempFeelsLike[:4])+"°C")
    print("The current humidity in "+(location)+" is: "+(cityHumidity))
    print("The current weather in "+(location)+" is described as: "+(cityWeatherDescription))
    print("The current wind speed in "+(location)+" is "+(cityWindSpeed)+"mph")
