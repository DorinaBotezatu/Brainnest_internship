''' The goal of this project is to create a weather app that shows the current weather conditions and forecast for a specific location.

Here are the steps you can take to create this project:

    Use the requests library to make an API call to a weather service (e.g. OpenWeatherMap) to retrieve the weather data for a specific location.

    Use the json library to parse the JSON data returned by the API call.

    Use the tkinter library to create a GUI for the app, including widgets such as labels, buttons and text boxes.

    Use the Pillow library to display the weather icons.

    Use the datetime library to display the current time and date. '''

# First, let us begin by importing the requests package.

import requests
from PIL import ImageTk, Image
from tkinter import Button, Label, Tk, PhotoImage, StringVar, Entry, messagebox
from _datetime import datetime

app = Tk()
app.title("Weather App")
app.geometry('600x600')
# app.resizable(0, 0)
color = '#fff'
titlebar_icon = PhotoImage(file='icons/weather-forecast.png')
app.configure(bg=color)
app.iconphoto(False, titlebar_icon)

# Location of the image
now = datetime.now()
date_time = now.strftime("%d/%m/%Y %H:%M:%S")


def weather_forecast(city):
    api_key = "681737ecb135f0b4891774e98167e67d"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    req = requests.get(url)
    weather_info_from_api = req.json()
    try:
        city = weather_info_from_api["name"]
        country = weather_info_from_api["sys"]["country"]
        city_country = f"{city}, {country}"
        type_weather = weather_info_from_api["weather"][0]["main"]
        temperature = weather_info_from_api["main"]["temp"]
        humidity = weather_info_from_api["main"]["humidity"]
        temperature = temperature - 273.15
        return city_country, type_weather, temperature, humidity
    except Exception as e:
        print(e)


def set_weather_image(weather_type):
    weather_img = Image.open(f"Icons/{weather_type}.png").resize((100, 100))
    img = ImageTk.PhotoImage(weather_img)
    image_lbl.image(img) # throws 'Label' object has no attribute 'image' for some reason, 'image' is present in documentation however
    image_lbl.configure(image=img)


def search():
    city = city_text.get()
    try:
        weather = weather_forecast(city)
        if weather:
            weather_type = weather[1]
            datetime_lbl["text"] = date_time
            location_lbl['text'] = weather[0]
            temp_lbl['text'] = '{:.2f}°C,'.format(weather[2])
            weather_lbl['text'] = weather_type
            humidity_lbl["text"] = "Humidity: " + str(weather[3])
            set_weather_image(weather_type)
        else:
            messagebox.showerror('Error', 'Cannot Find City {}'.format(city))
    except requests.exceptions.ConnectionError:
        messagebox.showerror('Error', 'Connection error')


city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_btn = Button(app, text='Get Weather Info', width=15, command=search)
search_btn.pack()

image_lbl = Label(app)
image_lbl.pack()

datetime_lbl = Label(app, text='', font=("Calibri", 22, 'bold'))
datetime_lbl.pack()

location_lbl = Label(app, text='', font=('Calibri', 22, 'bold'))
location_lbl.pack()

temp_lbl = Label(app, text='', font=("Calibri", 22, 'bold'))
temp_lbl.pack()

weather_lbl = Label(app, text='', font=("Calibri", 22, 'bold'))
weather_lbl.pack()

humidity_lbl = Label(app, text='', font=("Calibri", 22, 'bold'))
humidity_lbl.pack()

app.mainloop()
