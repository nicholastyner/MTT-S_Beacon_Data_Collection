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
latitude_tx, longitude_tx, latitude_rx, longitude_rx = user_input.get_input()

# calculating the distance between the points Haversine formula
distance = haversine_formula.calculate_distance(latitude_tx, longitude_tx, latitude_rx, longitude_rx)

distance_between_midpoints = distance / (COUNT_MIDPOINTS - 1)

# midpoints
midpoints = midpoints.calculate_midpoints(latitude_tx, longitude_tx, latitude_rx, longitude_rx, distance, COUNT_MIDPOINTS)
print(midpoints)



# sunrise sunset API
sunrise, sunset = sunrise_sunset.sunrise_sunset(latitude_tx, longitude_tx)

print(sunrise, sunset)

# Weather
weather_dict = weather.weather(latitude_tx, longitude_rx)

# Altitude and azimuth
elevation_dict = sunrise_sunset.elevation(latitude_tx, longitude_tx)

write_to_csv.csv_headers(weather_dict)
write_to_csv.to_csv(weather_dict)

datetime.now()

time.sleep(60)