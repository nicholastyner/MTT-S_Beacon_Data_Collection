import requests

# sunrise sunset API
latitude = 136.204823
longitude = 138.252930

sunrise_sunset_input = {
    "lat" : latitude,
    "lng" : longitude,
}
sunrise_sunset_response = requests.get(url = "https://api.sunrise-sunset.org/json", params=sunrise_sunset_input)
print(sunrise_sunset_response.json())