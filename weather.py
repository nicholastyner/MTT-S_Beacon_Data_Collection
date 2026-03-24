import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

OPEN_WEATHER_API_KEY = os.getenv("OPEN_WEATHER_API_KEY")

def weather(lat, lon):
    weather_response = requests.get(url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={OPEN_WEATHER_API_KEY}")
    weather_json = weather_response.json()
    weather_dict = {
        "temperature": weather_json["main"]["temp"],
        "pressure" : weather_json["main"]["pressure"],
        "wind" : weather_json["wind"]["speed"],
        "rain" : 0,
        "humidity" : weather_json["main"]["humidity"]        
    }
    try:
        weather_dict["rain"] = weather_json["rain"]["1h"]
    except:
        pass
    return weather_dict