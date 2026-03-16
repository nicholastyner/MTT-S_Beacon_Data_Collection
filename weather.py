import os
import requests
import json

OPEN_WEATHER_API_KEY = os.getenv("OPEN_WEATHER_API_KEY")

def weather(lat, lon):
    weather_response = requests.get(url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPEN_WEATHER_API_KEY}&units=metric")
    weather_json = weather_response.json()
    print(weather_json)
    # FIXME remove above line and uncomment below once API key functioning
    # weather_dict = {
    #     "temperature": weather_json["main"]["temp"],
    #     "pressure" : weather_json["main"]["pressure"],
    #     "wind" : weather_json["wind"]["speed"],
    #     "rain" : weather_json["rain"]["1h"],
    #     "humidity" : weather_json["main"]["humidity"]        
    # }