import pymongo
from tkinter import Tk, Label, Entry, Button


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Weather_db"]
weather_collection = db["data"]

def get_weather():
    city = city_entry.get()
    city = city.lower()
    weather_data = weather_collection.find_one({"city": {"$regex": f'^{city}$', "$options": 'i'}})

    if weather_data:
        weather_info = f"Weather: {weather_data['conditions']}\nTemperature: {weather_data['temperature']}°C\nHumidity: {weather_data['humidity']}%"
        weather_label.config(text=weather_info)
    else:
        weather_label.config(text=f"Error: Weather data not available for {city.capitalize()}.")

root = Tk()



root.geometry("500x500")
root.title("Weather Dashboard")

city_label = Label(root, text="Enter city:")
city_label.pack()

city_entry = Entry(root)
city_entry.pack()

get_weather_button = Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack()

weather_label = Label(root, text="")
weather_label.pack()

root.mainloop()
