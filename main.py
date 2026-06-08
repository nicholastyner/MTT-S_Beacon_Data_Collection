import haversine_formula
import midpoints
import sunrise_sunset
import weather
import write_to_csv
import time
import user_input
from datetime import datetime

# number of midpoints (includes endpoints)
COUNT_MIDPOINTS = 5

# Get latitude and longitude of tx and rx
# latitude_tx, longitude_tx, latitude_rx, longitude_rx = user_input.get_input()
# FIXME
latitude_tx = 30.0923
longitude_tx = 32.0923
latitude_rx = 34.0923
longitude_rx = 36.0923

# FIXME
# signal strength
rf_strength = -54.3

# calculating the distance between the points Haversine formula
distance = haversine_formula.calculate_distance(latitude_tx, longitude_tx, latitude_rx, longitude_rx)

distance_between_midpoints = distance / (COUNT_MIDPOINTS - 1)

# midpoints
midpoints = midpoints.calculate_midpoints(latitude_tx, longitude_tx, latitude_rx, longitude_rx, distance, COUNT_MIDPOINTS)

data_dict = {
    "general" : {},
    0 : {},
    1 : {},
    2 : {},
    3 : {},
    4 : {}
}

data_dict["general"].update({"RF strength (dB)" : rf_strength,
                            "Time (HH:MM:SS)" :  datetime.now().strftime("%H:%M:%S")})

for i in range(COUNT_MIDPOINTS):
    
    values = data_dict[i]
    
    # add locations
    values.update({"latitude (deg)" : midpoints[i][0],
                   "longitude (deg)" : midpoints[i][1]})
    
    # sunrise sunset API
    sunrise, sunset = sunrise_sunset.sunrise_sunset(latitude_tx, longitude_tx)
    
    # Altitude and azimuth
    elevation_dict = sunrise_sunset.elevation(latitude_tx, longitude_tx)
    
    # Weather
    weather_dict = weather.weather(latitude_tx, longitude_rx)

    values.update({"sunrise (HH:MM:SS)" : sunrise,
                   "sunset (HH:MM:SS)" : sunset,})
    values.update(elevation_dict)
    values.update(weather_dict)

write_to_csv.csv_headers(data_dict)
write_to_csv.to_csv(data_dict)