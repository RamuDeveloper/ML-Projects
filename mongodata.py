from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["Weather_db"]
collection = db["data"]

# Sample weather data (replace this with actual weather data)
weather_data = [
    {"city": "New York", "temperature": 20, "humidity": 50, "conditions": "Cloudy"},
    {"city": "Los Angeles", "temperature": 25, "humidity": 60, "conditions": "Sunny"},
    {"city": "Chicago", "temperature": 15, "humidity": 55, "conditions": "Rainy"},
{"city": "WashingtonDC", "temperature": 25, "humidity": 35, "conditions": "Haze"}
]

# Insert weather data into MongoDB
collection.insert_many(weather_data)

print("Weather data inserted successfully.")
