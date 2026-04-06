import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

IPGEOLOCATION_API_KEY = os.getenv("IPGEOLOCATION_API_KEY")

def sunrise_sunset(lat, lon):
    # TODO
    # do the sunrise sunset in the midpoint/at both sides
    # calculate the time zones in the middle
    # military time
    sunrise_sunset_input = {
        "lat" : lat,
        "lng" : lon,
    }
    sunrise_sunset_response = requests.get(url = "https://api.sunrise-sunset.org/json", params=sunrise_sunset_input)
    sunrise_sunset_json = sunrise_sunset_response.json()
    sunrise_sunset_dict = sunrise_sunset_json["results"]
    
    # extract useful information
    sunrise = sunrise_sunset_dict["sunrise"]
    sunset = sunrise_sunset_dict["sunset"]
    
    return sunrise, sunset

def elevation(lat, lon):
    url = f"https://api.ipgeolocation.io/v3/astronomy?apiKey={IPGEOLOCATION_API_KEY}&lat={lat}&long={lon}"
    elevation_response = requests.request("GET", url)
    elevation_json = elevation_response.json()
    
    elevation_dict = {
        "altitude": elevation_json["astronomy"]["sun_altitude"],
        "azimuth": elevation_json["astronomy"]["sun_azimuth"]
    }
    return elevation_dict