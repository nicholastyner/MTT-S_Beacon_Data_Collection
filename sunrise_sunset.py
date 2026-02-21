import requests
import json

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
