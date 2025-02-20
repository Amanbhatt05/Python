from tkinter import *
from tkinter import ttk
import requests
from PIL import ImageTk, Image

def get_data():
    city = city_name.get()
    try:
        data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=9121f1d1c9e8620cc4e3a06dc12b9575").json()
        weather_description_place_value.config(text=data["weather"][0]["description"])
        temp_place_value.config(text=str(int(data["main"]["temp"] - 273.15)) + " °C")  # Corrected conversion
        country_place_value.config(text=data["sys"]["country"])
        pressure_place_value.config(text=str(data["main"]["pressure"]) + " hPa")
        wind_place_value.config(text=str(int(data["wind"]["speed"] * 3.6)) + " kph")
        humidity_place_value.config(text=str(data["main"]["humidity"]) + " %")
    except KeyError:
        weather_description_place_value.config(text="Invalid city or API error.")

win = Tk()
win.title("WEATHER")
win.geometry("700x500")

# Use the correct image file
image_bg = Image.open("bgforecast.jpeg")  # Use your image file
bg_image = ImageTk.PhotoImage(image_bg)
img = Label(win, image=bg_image)
img.place(x=0, y=0)

title = Label(win, text="WEATHER FORECASTING", font=("Times New Roman", 30, "italic"))
title.place(x=100, y=50, height=50, width=500)

list_places = ["New Delhi", "Mumbai", "Chennai", "Kolkata", "Bangalore", "Hyderabad", "Pune", "Ahmedabad", "Lucknow"]
city_name = StringVar()
search_box = ttk.Combobox(win, values=list_places, font=("Times New Roman", 24, "italic"), textvariable=city_name)
search_box.place(x=100, y=150, height=45, width=350)

weather_description_place = Label(win, text="Weather Description:", font=("Arial", 15))
weather_description_place.place(x=100, y=230, height=30, width=250)
weather_description_place_value = Label(win, text="", font=("Arial", 15))
weather_description_place_value.place(x=360, y=230, height=30, width=200)

temp_place = Label(win, text="Temperature:", font=("Arial", 15))
temp_place.place(x=100, y=270, height=30, width=250)
temp_place_value = Label(win, text="", font=("Arial", 15))
temp_place_value.place(x=360, y=270, height=30, width=200)

country_place = Label(win, text="Country:", font=("Arial", 15))
country_place.place(x=100, y=310, height=30, width=250)
country_place_value = Label(win, text="", font=("Arial", 15))
country_place_value.place(x=360, y=310, height=30, width=200)

pressure_place = Label(win, text="Pressure:", font=("Arial", 15))
pressure_place.place(x=100, y=350, height=30, width=250)
pressure_place_value = Label(win, text="", font=("Arial", 15))
pressure_place_value.place(x=360, y=350, height=30, width=200)

wind_place = Label(win, text="Wind Speed:", font=("Arial", 15))
wind_place.place(x=100, y=390, height=30, width=250)
wind_place_value = Label(win, text="", font=("Arial", 15))
wind_place_value.place(x=360, y=390, height=30, width=200)

humidity_place = Label(win, text="Humidity:", font=("Arial", 15))
humidity_place.place(x=100, y=430, height=30, width=250)
humidity_place_value = Label(win, text="", font=("Arial", 15))
humidity_place_value.place(x=360, y=430, height=30, width=200)

search_button = Button(win, text="Search", command=get_data, font=("Times New Roman", 28, "bold"))
search_button.place(x=470, y=150, height=45, width=130)

win.mainloop()
